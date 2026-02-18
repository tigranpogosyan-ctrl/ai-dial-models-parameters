from task.app.main import run

user_request = "What is entropy in LLM's responses?"

# Example 1: Negative presence penalty (less topic diversity)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    presence_penalty=-2.0  # LLM may stick to a narrower topic
)

# Example 2: Neutral presence penalty (default)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    presence_penalty=0.0  # Default behavior
)

# Example 3: High presence penalty (more topic diversity)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    presence_penalty=2.0  # Encourages LLM to bring in new related topics
)
