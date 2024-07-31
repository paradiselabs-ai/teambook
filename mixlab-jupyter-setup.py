import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

# Now you can import from MixLab
from mixlab import your_module  # Replace with actual MixLab modules

# Rest of your imports
import autogen
from dotenv import load_dotenv
# ... other imports as needed

# Load environment variables
load_dotenv()

print("MixLab N_AnthGroqiLlamPyter_otebook initialized!")
