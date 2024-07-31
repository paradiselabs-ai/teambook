# Modify the enhanced_run_assistant function to include the surprise feature

import random

def enhanced_run_assistant(prompt):
    """
    Run the AI assistant with enhanced capabilities including RAG and surprise optimization.
    
    Args:
    prompt (str): User's input prompt
    """
    # ... (previous code remains the same)
    
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
            
            # Surprise feature: Randomly trigger code optimization
            if random.random() < 0.3:  # 30% chance to trigger
                surprise_code_optimization(code)

# ... (rest of the code remains the same)
