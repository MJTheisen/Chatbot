import openai
import time

openai.api_key = "yourapikeyhere!"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].text.strip()

while True:
    prompt = input("You: ")
    response = generate_response(prompt)
    print("Chatbot: " + response)
    time.sleep(1)
