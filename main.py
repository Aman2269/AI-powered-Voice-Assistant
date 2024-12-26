import speech_recognition
import win32com.client
import webbrowser
import datetime
import openai
import os
from config import apikey
import random


def ai(prompt):
    openai.api_key = apikey
    text = f"openai response from prompt :{prompt} \n .........................\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="write an mail for my resignation to my boss",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response["choices"][0]["text"]
    if not os.path.exists("openai"):
        os.mkdir("openai")

    # with open(f"openai/prompt -{random.randint(1, 21121353432)}", "w") as f:
    with open(f"openai/{''.join(prompt[6:]).strip()}.txt", "w") as f:
        f.write(text)
    speaker.speak(" Aman ,THE email has been saved to your folder please check")


speaker = win32com.client.Dispatch("Sapi.SpVoice")
chatting = ""


def chat(query):
    global chatting
    openai.api_key = apikey
    chatting += f"saurabh: {query}\n talki:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatting,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    speaker.speak(response["choices"][0]["text"])
    # print(response["choices"][0]["text"])
    chatting += f"{response['choices'][0]['text']}\n"
    print(chatting)
    return response["choices"][0]["text"]

    # with open(f"openai/{''.join(prompt[6:]).strip()}.txt", "w") as f:
    #     f.write(text)


def get():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognising")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "some error occurred from my side , I apologise"


if __name__ == '__main__':
    print("welcome to the world of ai")
    s = "Hello I am your assistant and I welcome you to the world of ai"
    speaker.speak(s)
    # speaker.speak("What is your name")
    # name = input()
    # speaker.speak(f"hello {name} , how can I help you ")

    while True:
        print("Listening......")
        text = get()
        sites = [["youtube", "https://www.youtube.com"], ["Wikipedia", "https://www.wikipedia.com"],
                 ["Google", "https://www.google.com/"], ["instagram", "https://www.instagram.com"]]
        if text == "exit":
            speaker.speak("nice talking to you , Thank you sir")
            exit()

        for site in sites:
            if f"open {site[0]}".lower() in text.lower():
                speaker.speak(f"opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "the time" in text:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speaker.speak(f"Sir time is {hour} hours and {min} minutes")
        if "talki".lower() in text.lower():
            ai(prompt=text)

        else:
            p = chat(text)
