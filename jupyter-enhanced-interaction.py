# Enhanced Interaction Loop for AutoGen Jupyter Notebook Assistant

def enhanced_run_assistant(prompt):
    """
    Run the AI assistant with enhanced capabilities including RAG.
    
    Args:
    prompt (str): User's input prompt
    """
    # Check if it's a file upload request
    if prompt.startswith("upload:"):
        file_path = prompt.split(":")[1].strip()
        result = upload_file(file_path)
        display(Markdown(f"**System:** {result}"))
        return

    # Perform RAG query
    rag_context = rag_query(prompt)
    
    # Combine RAG context with user prompt
    enhanced_prompt = f"{rag_context}\n\nBased on this context, {prompt}"
    
    # Initiate the chat with the enhanced prompt
    response = user_proxy.initiate_chat(
        manager,
        message=enhanced_prompt
    )
    
    # Extract and display the assistant's response
    assistant_response = response.summary
    display(Markdown(f"**AI Assistant:** {assistant_response}"))
    
    # Check if there's any code in the response
    if "```python" in assistant_response:
        code_blocks = assistant_response.split("```python")
        for block in code_blocks[1:]:
            code = block.split("```")[0].strip()
            display(Markdown("**Executing code:**"))
            display(Markdown(f"```python\n{code}\n```"))
            result = code_executor(code)
            display(Markdown("**Output:**"))
            display(Markdown(f"```\n{result}\n```"))

def enhanced_interactive_session():
    """
    Start an enhanced interactive session with the AI assistant.
    """
    print("Welcome to the Enhanced AutoGen Jupyter Assistant!")
    print("You can upload files by typing 'upload: <file_path>'")
    print("Type 'exit' to end the session.")
    print("\n" + "-"*50 + "\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        clear_output(wait=True)
        enhanced_run_assistant(user_input)
        print("\n" + "-"*50 + "\n")

# Explanation:
# - enhanced_run_assistant now includes RAG capabilities
# - It checks for file upload requests and handles them separately
# - For regular queries, it performs a RAG query to provide context
# - The assistant's response is then generated based on this enhanced context
# - Code execution remains the same as in the previous version
# - enhanced_interactive_session provides instructions for file upload

# To start the enhanced interactive session, run:
# enhanced_interactive_session()
