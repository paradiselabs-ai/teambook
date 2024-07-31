# Add this at the beginning of your script
conversation_history = []

def enhanced_run_assistant(prompt):
    global conversation_history
    
    # Add the current prompt to the history
    conversation_history.append(f"User: {prompt}")
    
    # Create a context string from the last few interactions
    context = "\n".join(conversation_history[-5:])  # Last 5 interactions
    
    # Combine the context with the RAG query
    rag_context = rag_query(prompt)
    enhanced_prompt = f"Conversation history:\n{context}\n\nRelevant information:\n{rag_context}\n\nBased on this context, respond to: {prompt}"
    
    # ... (rest of the function remains the same)
    
    # Add the assistant's response to the history
    conversation_history.append(f"Assistant: {assistant_response}")

# ... (rest of the code remains the same)
