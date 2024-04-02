from openai import OpenAI

def translate_text_with_chatgpt(text, source_language="English", target_language="Simplified Chinese"):
    """
    Translates text using ChatGPT from a source language to a target language.
    
    Parameters:
    - text: The text to be translated.
    - source_language: The language of the input text.
    - target_language: The language to translate the text into.
    
    Returns:
    The translated text.
    """
    client = OpenAI(
    )
    
    try:
        stream = client.chat.completions.create(
          model="gpt-4",
          messages=[
              { "role": "user", "content": f"Translate the following text from {source_language} to {target_language}: \n\n{text}"}, 
          ],
          stream=True,
        )
        
        for chunk in stream:
            print(chunk.choices[0].delta.content or "", end="")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

# Example usage
if __name__ == "__main__":
    original_text = "Hello, how are you?"
    translated_text = translate_text_with_chatgpt(original_text, "English", "Simplified Chinese")
