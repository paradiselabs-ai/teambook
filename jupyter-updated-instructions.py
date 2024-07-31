def enhanced_interactive_session():
    """
    Start an enhanced interactive session with the AI assistant.
    """
    print("Welcome to the Enhanced AutoGen Jupyter Assistant!")
    print("You can:")
    print("- Ask questions or request code examples")
    print("- Upload files by typing 'upload: <file_path>'")
    print("  Supported file types: .txt, .py, .md, .jpg, .jpeg, .png, .gif")
    print("- Type 'exit' to end the session")
    print("\n" + "-"*50 + "\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        clear_output(wait=True)
        enhanced_run_assistant(user_input)
        print("\n" + "-"*50 + "\n")

# The rest of the code remains the same...
