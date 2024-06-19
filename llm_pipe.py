import os
import ollama
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')
client = Groq(api_key=groq_api_key)

# for generating descriptions from images
def moondream_pipeline(image_bytes, prompt):
    stream = ollama.chat(
        model="moondream", 
        messages=[{
            "role": "user", 
            "content": prompt,
            "images": [image_bytes]
        }],
        stream=False
    )
    answer = stream["message"]["content"]
    answer = answer.replace("\n", "")
    return answer

# for generating responses from user queries
def groq_pipeline(question, context):
    formatted_prompt = f"You are an AI designed to help answer questions about what the user has seen. Question: {question}\n\nWhat the user has seen: {context}. Keep your answer very brief"
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": formatted_prompt,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content
