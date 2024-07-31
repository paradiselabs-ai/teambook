# Imports and Initial Setup for AutoGen Jupyter Notebook Assistant
import os
import autogen
from dotenv import load_dotenv
import openai
from autogen import config_list_from_json

# Load environment variables
load_dotenv()

# Set up OpenAI client with OpenRouter
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = os.getenv("OPENROUTER_API_KEY")

# Configure the models
config_list = config_list_from_json(
    env_or_file="OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-4o"]
    }
)

# AutoGen configuration
config_list_agent = [
    {
        "model": "gpt-4o",
        "api_key": os.getenv("OPENROUTER_API_KEY"),
        "base_url": "https://openrouter.ai/api/v1",
    }
]

# Explanation of imports and setup:
# - autogen: The main library for creating AI agents
# - dotenv: Used to load environment variables from a .env file
# - openai: OpenAI's Python client, used here with OpenRouter
# - config_list_from_json: AutoGen function to load configuration from a JSON file or environment variable

# The setup includes:
# 1. Loading environment variables
# 2. Configuring OpenAI client to use OpenRouter
# 3. Setting up the model configuration for AutoGen
# 4. Creating a specific configuration for the AI agents

# Note: Make sure you have a .env file with OPENROUTER_API_KEY and an OAI_CONFIG_LIST file or environment variable set up.
