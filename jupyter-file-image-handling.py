# File and Image Handling for AutoGen Jupyter Notebook Assistant

import os
from IPython.display import display, Image
import matplotlib.pyplot as plt
import io
from PIL import Image as PILImage

def upload_file(file_path):
    """
    Upload a file and add its content to the vector store for RAG.
    
    Args:
    file_path (str): Path to the file to be uploaded
    
    Returns:
    str: Confirmation message
    """
    _, file_extension = os.path.splitext(file_path)
    
    if file_extension.lower() in ['.txt', '.py', '.md']:
        with open(file_path, "r") as file:
            content = file.read()
        
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_text(content)
        
        vector_store.add_texts(texts)
        return f"File {file_path} uploaded, vectorized, and added to RAG system."
    elif file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        return upload_and_analyze_image(file_path)
    else:
        return f"Unsupported file type: {file_extension}"

def upload_and_analyze_image(image_path):
    """
    Upload an image, display it, and perform basic analysis.
    
    Args:
    image_path (str): Path to the image file
    
    Returns:
    str: Description of the image
    """
    try:
        image = PILImage.open(image_path)
        plt.figure(figsize=(10, 10))
        plt.imshow(image)
        plt.axis('off')
        plt.show()
        
        # Basic image analysis (placeholder for more advanced analysis)
        width, height = image.size
        mode = image.mode
        format = image.format
        
        analysis = f"Image analysis:\n"
        analysis += f"- Dimensions: {width}x{height}\n"
        analysis += f"- Color mode: {mode}\n"
        analysis += f"- Format: {format}\n"
        
        # Add image metadata to vector store for potential RAG queries
        vector_store.add_texts([analysis], metadatas=[{"source": image_path}])
        
        return analysis
    except Exception as e:
        return f"Error processing image: {str(e)}"

# Modify the enhanced_run_assistant function to handle file and image uploads
def enhanced_run_assistant(prompt):
    """
    Run the AI assistant with enhanced capabilities including file and image handling.
    
    Args:
    prompt (str): User's input prompt
    """
    # Check if it's a file upload request
    if prompt.lower().startswith("upload:"):
        file_path = prompt.split(":")[1].strip()
        result = upload_file(file_path)
        display(Markdown(f"**System:** {result}"))
        return

    # Rest of the function remains the same...
    # (RAG query, assistant response, code execution, etc.)

# Explanation:
# - upload_file function now handles both text files and images
# - Text files are processed and added to the vector store for RAG
# - Images are displayed and basic analysis is performed
# - Image metadata is also added to the vector store for potential RAG queries
# - The enhanced_run_assistant function is modified to use this new upload_file function
# - Users can upload files by typing "upload: <file_path>" in the interactive session
