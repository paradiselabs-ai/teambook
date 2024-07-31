# Main Interaction Loop for AutoGen Jupyter Notebook Assistant

from IPython.display import display, Markdown

def run_assistant(prompt):
    """
    Run the AI assistant with the given prompt and display the response.
    
    Args:
    prompt (str): User's input prompt
    """
    # Initiate the chat with the user's prompt
    response = user_proxy.initiate_chat(
        manager,
        message=prompt
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

# Interactive prompt using IPython's input
from IPython.display import clear_output

def interactive_session():
    """
    Start an interactive session with the AI assistant.
    """
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        clear_output(wait=True)
        run_assistant(user_input)
        print("\n" + "-"*50 + "\n")

# Explanation of the main interaction loop:
# 1. run_assistant function:
#    - Takes a user prompt and initiates a chat with the AI assistant
#    - Displays the assistant's response using Markdown for better formatting
#    - If the response contains Python code, it extracts and executes the code
#      using our previously defined code_executor function
#    - Displays both the code and its output
#
# 2. interactive_session function:
#    - Provides a continuous loop for user interaction
#    - Uses IPython's input function for compatibility with Jupyter notebooks
#    - Clears previous output for a cleaner interface
#    - Calls run_assistant for each user input
#    - Allows the user to exit the session by typing 'exit'
#
# This setup creates a seamless, interactive coding assistant experience
# within the Jupyter notebook environment.

# To start the interactive session, run:
# interactive_session()
