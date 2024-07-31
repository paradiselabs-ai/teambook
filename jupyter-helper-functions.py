# Helper Functions for AutoGen Jupyter Notebook Assistant

import base64
from IPython.display import display, Image
import matplotlib.pyplot as plt
from PIL import Image as PILImage
import io

def display_image(image_path):
    """
    Display an image in the Jupyter notebook.
    
    Args:
    image_path (str): Path to the image file
    """
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    display(Image(data=base64.b64decode(encoded_image)))

def analyze_image(image_path):
    """
    Analyze an image and display it in the notebook.
    
    Args:
    image_path (str): Path to the image file
    
    Returns:
    str: A description of the image (placeholder for actual analysis)
    """
    image = PILImage.open(image_path)
    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    
    # Placeholder for image analysis
    return "Image analysis: This function would typically use a pre-trained model to analyze the image content."

def code_executor(code):
    """
    Execute Python code and capture the output.
    
    Args:
    code (str): Python code to execute
    
    Returns:
    str: Output of the executed code
    """
    output = io.StringIO()
    sys.stdout = output
    try:
        exec(code)
        result = output.getvalue()
    except Exception as e:
        result = f"Error: {str(e)}"
    finally:
        sys.stdout = sys.__stdout__
    return result

# Explanation of helper functions:
# 1. display_image: Uses base64 encoding to display images directly in the notebook.
#    This is useful for visualizing data or results.
#
# 2. analyze_image: A placeholder function that displays an image and returns a 
#    description. In a full implementation, this would use a pre-trained model
#    for actual image analysis.
#
# 3. code_executor: Safely executes Python code passed as a string and captures
#    the output. This allows the AI to generate and run code, then see the results.
#
# These functions enhance the capabilities of our Jupyter notebook assistant,
# allowing it to work with images and execute code snippets dynamically.
