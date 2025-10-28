from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import async_session
from app.models.quality_issue import QualityIssue, SeverityEnum, Base
from sqlalchemy.future import select

router = APIRouter()

# Example: Dashboard bucket endpoint
@router.get("/dashboard/{username}")
async def get_dashboard_buckets(username: str, session: AsyncSession = Depends(async_session)):
    # Query for pending issues assigned to this user, grouped by severity
    counts = {s.value: 0 for s in SeverityEnum}
    result = await session.execute(
        select(QualityIssue).where(QualityIssue.assigned_to == username, QualityIssue.status == "pending")
    )
    for issue in result.scalars():
        counts[issue.initial_severity.value] += 1
    return counts

# Example: Create new Quality Issue
@router.post("/")
async def create_quality_issue(data: dict, session: AsyncSession = Depends(async_session)):
    # TODO: Add validation, AI integration, etc.
    issue = QualityIssue(**data)
    session.add(issue)
    await session.commit()
    await session.refresh(issue)
    return issue