from openai import OpenAI
import os 

def translate_text_with_chatgpt(source_file, target_file, source_language="English", target_language="Simplified Chinese"):
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
            api_key=os.environ.get("OPENAI_API_KEY"),
    )

    with open(source_file) as fi, open(target_file, "w") as fo:
        text = fi.readlines()
        lines = len(text)
        batch_size = 100
        i = 0
        while True:
            start, end = i * batch_size, min((i + 1) * batch_size, lines)
            print(f"current start {start}, current end {end}, total lines {lines}")
            i += 1

            try:
                stream = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    { "role": "user", "content": f"Translate the following text from {source_language} to {target_language}: \n\n{text[start: end]}"}, 
                ],
                stream=True,
                )
                
                for chunk in stream:
                    fo.write(chunk.choices[0].delta.content or "")
                
            except Exception as e:
                print(f"An error occurred: {e}")
                return ""
            
            if end == lines:
                break

# Example usage
if __name__ == "__main__":
    for idx in ["08", "09", "10"]:
        source_file = f"./ch{idx}_en.md"
        target_file = f"./ch{idx}_cn.md"

        translated_text = translate_text_with_chatgpt(source_file, target_file, "English", "Simplified Chinese")
