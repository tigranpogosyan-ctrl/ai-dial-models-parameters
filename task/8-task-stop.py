from task.app.main import run

user_request = "Explain the key components of a Large Language Model architecture"

# Example 1: Stop generation at double newlines
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    stop="\n\n"  # LLM will stop once it generates two consecutive newlines
)

# Example 2: Stop generation when specific LLM architecture sections appear
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    stop=["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]
)

# Optional: To see full JSON and finish_reason
run(
    deployment_name='gpt-4o',
    print_only_content=False,
    stop=["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]
)
