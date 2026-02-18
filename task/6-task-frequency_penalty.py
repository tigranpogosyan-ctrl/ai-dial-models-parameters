from task.app.main import run

user_request = "Explain the water cycle in simple terms for children"

# Example 1: Lower penalty (more repetition possible)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    frequency_penalty=-2.0  # Can produce more repetitive text
)

# Example 2: Neutral (default behavior)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    frequency_penalty=0.0  # Default, moderate repetition
)

# Example 3: Higher penalty (less repetition)
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    frequency_penalty=2.0  # Strong penalty, less repeated words
)
