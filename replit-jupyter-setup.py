# Cell 1: Imports and Setup
import os
import autogen
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

# Cell 2: Model Configurations
model_configs = {
    "claude": {"model": "claude-3-sonnet-20240229", "client": anthropic_client, "name": "Claude"},
    "groq": {"model": "llama2-70b-4096", "client": groq_client, "name": "Groq"},
    "gpt": {"model": "gpt-4o", "client": openai, "name": "GPT"},
    "salesforce": {"model": "salesforce/codegen-6B-mono", "client": hf_client, "name": "Salesforce"}
}

# Cell 3: Create Agents
def create_model_agent(model_config, role):
    return autogen.AssistantAgent(
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

# Cell 4: Create Group Chat
groupchat = autogen.GroupChat(
    agents=[claude_agent, groq_agent, gpt_agent, salesforce_agent],
    messages=[],
    max_round=5
)

manager = autogen.GroupChatManager(groupchat=groupchat)

# Cell 5: Interactive Function
def run_assistant(prompt):
    response = manager.initiate_chat(
        autogen.UserProxyAgent(name="user"),
        message=prompt
    )
    print(f"AI Assistant Group: {response.summary}")

# Cell 6: Test the Assistant
run_assistant("Explain the concept of recursion and provide a simple Python example.")
