import os
from groq import Groq
from dotenv import load_dotenv

groq_api_key = os.getenv('GROQ_API_KEY')
client = Groq(api_key=groq_api_key)

import ollama
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


from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_groq import ChatGroq
from typing import List

class Filename(BaseModel):
    filename: List[str] = Field(description="The name of the files after the colon. Ignore the image description")

def get_file_name(context):
    model = ChatGroq()
    structured_llm = model.with_structured_output(Filename)
    answer = structured_llm.invoke(context)
    return answer.filename

