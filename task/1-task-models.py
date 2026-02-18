from task.app.main import run

# User message to test the LLM
user_request = "What LLMs can do?"

# Models you can try:
# - 'gpt-4o'
# - 'claude-3-7-sonnet@20250219'
# - 'gemini-2.5-pro'

run(
    deployment_name='gpt-4o',  # Replace with another model if you want to test
    print_request=True,         # True shows the request sent to the API
    print_only_content=False,   # False prints full response including metadata
)
