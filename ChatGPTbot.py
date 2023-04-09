import openai
import os
import time

####################################
###   setx OPENAI_API_KEY 1234   ###
#################################### 

# ...is the command I entered in command prompt to create an environmental 
# variable outside of the code. The os import is so that I can then use 
# this variable as my API key. Now I can save this file to GitHub without 
# the needed to constantly delete my visible API key here in the python 
# code, swaping the 1234 from the command for the actual API code of course. 
# Now, when I call:
 
openai.api_key = os.environ["OPENAI_API_KEY"]

# it will just look for the environment variable OPENAI_API_KEY on my local 
# machine and import it here.

# Generate a response based on the prompt. Made with a little help from the 
# guide regarding Chat completion in the Documentation. I originally used 
# "response = openai.Completion.create(", but that was when I was using 
# "text-davinci-002" instead of the "gpt-3.5-turbo". I plan to make a new 
# version of this instead if I manage to gain access to the ChatGPT-4 API.

def generate_response(prompt):
    response = openai.Completion.create(
        engine ="text-davinci-002",
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
