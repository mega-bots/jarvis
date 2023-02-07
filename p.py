import os
import openai
from actions import speak
openai.api_key = "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"
def play(ask):
    #ask =input("Questions: ")
    response = openai.Completion.create(
    model="text-davinci-003",     
    prompt= "simplify the sentence " +ask + " into this format:  song name : platform on which it is asked to play",
    temperature=0.5,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    text = response['choices'][0]['text']   
    text = text.split(":")
    song  = text[-2].split()[0]
    plat = text[-1].strip(" ")
    return song.strip(" ")+":"+plat.strip(" ")
def open(ask):
    #ask =input("Questions: ")
    response = openai.Completion.create(
    model="text-davinci-003",     
    prompt= ask,
    temperature=1,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    text = response['choices'][0]['text']
    print(text)   
    return text