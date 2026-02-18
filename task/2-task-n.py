from task.app.main import run

# User message
user_request = "Why is the snow white?"

# Example: try with 3 completions for gpt-4o
run(
    deployment_name="gpt-4o",  # Choose the model
    n=3,                       # Number of completions to generate
    print_request=True,         # See the full request
    print_only_content=False,   # See structured response, including all choices
)
