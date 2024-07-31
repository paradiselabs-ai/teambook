# AI Agents Setup for AutoGen Jupyter Notebook Assistant

# Import necessary AutoGen components
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

# Define the AI assistant agent
assistant = AssistantAgent(
    name="AI_Assistant",
    system_message="You are an AI coding assistant. Provide clear, concise, and accurate Python code examples and explanations.",
    llm_config={"config_list": config_list_agent}
)

# Define the user proxy agent
user_proxy = UserProxyAgent(
    name="User_Proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding_workspace",
        "use_docker": False,  # Set to True if you want to use Docker for code execution
    }
)

# Create a group chat
groupchat = GroupChat(agents=[assistant, user_proxy], messages=[], max_round=50)
manager = GroupChatManager(groupchat=groupchat)

# Explanation of the setup:
# 1. AssistantAgent: Represents the AI coding assistant
#    - system_message: Defines the role and behavior of the assistant
#    - llm_config: Uses the previously defined config_list_agent for model settings
#
# 2. UserProxyAgent: Represents the user (you) in the conversation
#    - human_input_mode: Set to "TERMINATE" to allow the agent to run autonomously until terminated
#    - max_consecutive_auto_reply: Limits the number of consecutive automatic replies
#    - is_termination_msg: Defines when to terminate the conversation
#    - code_execution_config: Sets up the environment for code execution
#
# 3. GroupChat: Creates a chat environment with both agents
#
# 4. GroupChatManager: Manages the group chat, facilitating the conversation flow

# This setup allows for an interactive coding session where the AI assistant can provide
# code examples and explanations, and the user proxy can execute the code in a controlled environment.
