# Multi-Model Setup and Integration for AutoGen Jupyter Notebook Assistant

import os
from dotenv import load_dotenv
from anthropic import Anthropic
from groq import Groq
import openai
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()

# Setup model clients
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")
hf_client = InferenceClient(token=os.getenv("HUGGINGFACE_API_KEY"))

# Define model configurations
model_configs = {
    "claude": {
        "model": "claude-3-sonnet-20240229",
        "client": anthropic_client,
        "name": "Claude"
    },
    "groq": {
        "model": "llama2-70b-4096",  # Adjust this to the specific Groq model you're using
        "client": groq_client,
        "name": "Groq"
    },
    "gpt": {
        "model": "gpt-4o",
        "client": openai,
        "name": "GPT"
    },
    "salesforce": {
        "model": "salesforce/codegen-6B-mono",
        "client": hf_client,
        "name": "Salesforce"
    }
}

# Create specialized agents for each model
from autogen import AssistantAgent, UserProxyAgent

def create_model_agent(model_config, role):
    return AssistantAgent(
        name=f"{model_config['name']}_{role}",
        llm_config={
            "config_list": [{
                "model": model_config["model"],
                "api_key": os.getenv(f"{model_config['name'].upper()}_API_KEY")
            }]
        }
    )

claude_agent = create_model_agent(model_configs["claude"], "Assistant")
groq_agent = create_model_agent(model_configs["groq"], "Coder")
gpt_agent = create_model_agent(model_configs["gpt"], "Planner")
salesforce_agent = create_model_agent(model_configs["salesforce"], "CodeReviewer")

# Create a group chat for the agents
from autogen import GroupChat, GroupChatManager

groupchat = GroupChat(
    agents=[claude_agent, groq_agent, gpt_agent, salesforce_agent],
    messages=[],
    max_round=5
)

manager = GroupChatManager(groupchat=groupchat)

# Modify the enhanced_run_assistant function to use the group chat
def enhanced_run_assistant(prompt):
    """
    Run the AI assistant with enhanced capabilities including multi-model interaction.
    
    Args:
    prompt (str): User's input prompt
    """
    # Check if it's a file upload request
    if prompt.lower().startswith("upload:"):
        file_path = prompt.split(":")[1].strip()
        result = upload_file(file_path)
        display(Markdown(f"**System:** {result}"))
        return

    # Perform RAG query
    rag_context = rag_query(prompt)
    
    # Combine RAG context with user prompt
    enhanced_prompt = f"{rag_context}\n\nBased on this context, {prompt}"
    
    # Initiate the group chat
    response = manager.initiate_chat(
        user_proxy,
        message=enhanced_prompt
    )
    
    # Extract and display the final response
    final_response = response.summary
    display(Markdown(f"**AI Assistant Group:** {final_response}"))
    
    # Check if there's any code in the response
    if "```python" in final_response:
        code_blocks = final_response.split("```python")
        for block in code_blocks[1:]:
            code = block.split("```")[0].strip()
            display(Markdown("**Executing code:**"))
            display(Markdown(f"```python\n{code}\n```"))
            result = code_executor(code)
            display(Markdown("**Output:**"))
            display(Markdown(f"```\n{result}\n```"))

# Explanation:
# - We set up clients for each model: Claude, Groq, GPT (via OpenAI), and Salesforce (via Hugging Face)
# - We create specialized agents for each model with specific roles
# - A GroupChat is set up to allow these agents to interact
# - The enhanced_run_assistant function now uses the GroupChatManager to facilitate multi-model interaction
# - Each query will now involve all models, with their responses synthesized into a final output
