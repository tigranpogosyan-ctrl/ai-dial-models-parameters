from task.app.main import run

# User message
user_request = "Describe the sound that the color purple makes when it's angry"

# Example: low randomness (more deterministic)
run(
    deployment_name='gpt-4o',
    temperature=0.0,          # Most deterministic output
    print_only_content=True
)

# Example: medium randomness (default creativity)
run(
    deployment_name='gpt-4o',
    temperature=1.0,          # Default, balanced creativity
    print_only_content=True
)

# Example: high randomness (more creative)
run(
    deployment_name='gpt-4o',
    temperature=2.0,          # Very creative, unusual responses
    print_only_content=True
)

# Optional: Out-of-range test
# run(
#     deployment_name='gpt-4o',
#     temperature=2.1,        # Check what happens if value is beyond allowed range
#     print_only_content=True
# )
