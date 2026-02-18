from task.app.main import run

# User message for the LLM
user_request = "Name a random animal"

run(
    deployment_name='gpt-4o',
    n=5,        # Generate 5 completion choices
    seed=42,    # Make the output deterministic
    print_only_content=True
)
