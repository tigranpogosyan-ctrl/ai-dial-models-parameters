from task.app.main import run

# User message
user_request = "What is token when we are working with LLM?"

run(
    deployment_name='gpt-4o',
    max_tokens=10,           # Limit the response to 10 tokens
    print_only_content=True  # Only print the generated content
)
