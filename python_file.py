import os

from groq import Groq

client = Groq(
    api_key="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",
)

# prompt = input("lf: ")

def generate(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

# p = input("------>")
# print(generate(p))