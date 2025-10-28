from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
import enum

Base = declarative_base()

class SeverityEnum(str, enum.Enum):
    critical = "Critical"
    major = "Major"
    minor = "Minor"
    observation = "Observation"

class QualityIssue(Base):
    __tablename__ = "quality_issues"

    id = Column(Integer, primary_key=True, index=True)
    reported_by = Column(String, index=True)
    issue_description = Column(Text)
    reported_date = Column(DateTime)
    identified_date = Column(DateTime)
    initial_severity = Column(Enum(SeverityEnum))
    escalation_required = Column(Boolean, default=False)
    triage_by = Column(String, nullable=True)
    final_severity = Column(Enum(SeverityEnum), nullable=True)
    impacted_department = Column(String, nullable=True)
    impact_detail = Column(Text, nullable=True)
    root_cause = Column(Text, nullable=True)
    containment = Column(Text, nullable=True)
    capa = Column(Text, nullable=True)
    effectiveness_check = Column(Boolean, default=False)
    assigned_to = Column(String, index=True)
    status = Column(String, default="pending")  # pending, closed, etc.

    # Add file uploads, timestamps, etc. as needed