import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class LLMHandler:
    def __init__(self):
        self.groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_response(self, query, context):
        """Generate response using Groq"""
        prompt = f"""You are a helpful assistant. Use the following context to answer the question.
        
Context: {context}

Question: {query}

Answer: """
        
        completion = self.groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            model="mixtral-8x7b-32768",
            temperature=0.5,
        )
        
        return completion.choices[0].message.content 