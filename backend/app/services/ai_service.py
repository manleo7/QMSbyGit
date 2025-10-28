import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

async def predict_user_name(partial_name: str, directory: list):
    # Simulate AI prediction from directory
    matches = [name for name in directory if partial_name.lower() in name.lower()]
    return matches[:5] # return top 5

async def smart_suggest_issue_description(input_text: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a concise issue description for: {input_text}",
        max_tokens=60
    )
    return response.choices[0].text.strip()