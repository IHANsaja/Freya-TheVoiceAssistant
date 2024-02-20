import speech_recognition as sr
import pyaudio as pa
import pywhatkit as pwk
import pyttsx3
import subprocess
import pickle
import json
import nltk
import numpy as np
import random

from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

model = load_model('Freya v2.11.h5')
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
lem = WordNetLemmatizer()

#freyage katahada
def speak(talk):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)
    engine.setProperty('voice', voices[1].id)
    engine.say(talk)
    engine.runAndWait()

#koyana eka store karanawa
def getAudio():
    rec = sr.Recognizer()
    mic_aud = None
    with sr.Microphone() as Mic:
        print("Say something...")
        mic_aud = rec.listen(Mic, phrase_time_limit=5)
        text = rec.recognize_google(mic_aud)
        print("did You said: " + text)
        return text

#Freya v2.11 model
def get_chatbot_response(user_input):
    input_bag = preprocess_input(user_input)
    predictions = model.predict(np.array([input_bag]))  # Pass a single input to the model
    predicted_class_index = np.argmax(predictions)
    predicted_class = classes[predicted_class_index]
    response = get_response(predicted_class)
    return response


def preprocess_input(user_input):
    input_words = nltk.word_tokenize(user_input)
    input_words = [lem.lemmatize(word.lower()) for word in input_words]

    bag = [1 if word in input_words else 0 for word in words]
    return np.array(bag)

responses_dict = {
    "greetings": ["Hi!", "Hey!", "Hello!", "Hi! how are you?", "Hello! how are you?", "Hey! how are you", "Hi! what's up?", "Hey! what's up?", "Hello! what's up?", "Hi! What’s going on?", "Hello! What’s going on?", "Hi! nice to meet you", "Hello! nice to meet you", "Hi! pleased to meet you", "Hello! pleased to meet you", "Hello there!"],
    "mornings": ["Good morning! have a great day to you!, very good morning!", "Morning! Good day to you!", "Morning! Wishing you the best for the day ahead!"],
    "nights": ["Good night, I hope only sweet dreams find you at night!", "Wishing you a peaceful sleep tonight!", "Good night! sweet dreams!", "Good night, sleep tight, can’t wait to see your smile in the morning so bright!"],
    "goodbyes": ["Good bye!", "Bye!", "Farewell mate!", "Happy to meet you! see you again!", "Happy to see you! take care!"]
}

def get_response(predicted_class):
    if predicted_class in responses_dict:
        return random.choice(responses_dict[predicted_class])
    else:
        return "I'm not sure how to respond to that."

valorant = r""
photoshop = r""
illustrator = r""
edge = r""
word = r""
powerpoint = r""
outlook = r""
steam = r""
discord = r""
telegram = r""
valheim = r""
work = r""

while True:
    try:
        txt = getAudio()
        if "youtube" in txt.lower():
            speak("sure! here what you looking for...")
            cutYT = txt.lower().replace("youtube", "").strip()
            pwk.playonyt(cutYT)
        elif "what is your name" in txt.lower():
            speak("My name is Freya")
        elif "who are you" in txt.lower():
            speak("I am an artificial intelligence that developed to help for ihan's day-to-day life. "
                  "This is my second version. my first version was failed. "
                  "May be ihan will expand my capabilities in some day. after that, you will see my powerful version in the near future")
        elif "google" in txt.lower():
            speak("sure! these are the results I got from the google...")
            cutGoo = txt.lower().replace("google", "").strip()
            pwk.search(cutGoo)
        elif "open riot" in txt.lower():
            try:
                subprocess.Popen([valorant])
                speak("Valorant is launching...")
            except Exception as e:
                speak("Error in launching Valorant. check your internet connection")
        elif "close riot" in txt.lower():
            try:
                subprocess.Popen("TASKKILL /F /IM RiotClientServices.exe")
                subprocess.Popen("TASKKILL /F /IM VALORANT.exe")
                speak("valorant is closing...")
            except Exception as e:
                speak("Error in closing valorant")
        elif "shutdown" in txt.lower():
            speak("yeah sure. your computer will shutdown in 30 second...")
            pwk.shutdown(30)
        elif "open photoshop" in txt.lower():
            try:
                subprocess.Popen([photoshop])
                speak("photoshop is launching...")
            except Exception as e:
                speak("Error in launching photoshop")
        elif "close photoshop" in txt.lower():
            try:
                subprocess.Popen("TASKKILL /F /IM Photoshop.exe")
                speak("Photoshop is closing...")
            except Exception as e:
                speak("Error in closing Photoshop")
        elif "open illustrator" in txt.lower():
            try:
                subprocess.Popen([illustrator])
                speak("illustrator is launching...")
            except Exception as e:
                speak("Error in launching illustrator")
        elif "close illustrator" in txt.lower():
            try:
                subprocess.Popen("TASKKILL /F /IM Illustrator.exe")
                speak("Illustrator is closing...")
            except Exception as e:
                speak("Error in closing Illustrator")
        elif "open edge" in txt.lower():
            try:
                subprocess.Popen([edge])
                speak("microsoft edge is launching... ")
            except Exception as e:
                speak("Error in launching edge browser. check your internet connection")
        elif "close edge" in txt.lower():
            try:
                subprocess.Popen("TASKKILL /F /IM msedge.exe")
                speak("microsoft edge is closing...")
            except Exception as e:
                speak("Error in closing microsoft edge")
        elif "open word" in txt.lower():
            try:
                subprocess.Popen([word])
                speak("microsoft word is launching...")
            except Exception as e:
                speak("Error in launching word")
        elif "close word" in txt.lower():
            try:
                subprocess.Popen("TASKKILL /F /IM WINWORD.EXE")
                speak("microsoft word is closing...")
            except Exception as e:
                speak("Error in closing microsoft word")
        elif "open powerpoint" in txt.lower():
            try:
                subprocess.Popen([powerpoint])
                speak("microsoft powerpoint is launching...")
            except Exception as e:
                speak("Error in launching powerpoint")
        elif "close powerpoint" in txt.lower():
            try:
                subprocess.Popen("TASKKILL /F /IM POWERPNT.EXE")
                speak("microsoft powerpoint is closing...")
            except Exception as e:
                speak("Error in closing microsoft powerpoint")
        elif "open outlook" in txt.lower():
            try:
                subprocess.Popen([outlook])
                speak("outlook is launching...")
            except Exception as e:
                speak("Error in launching outlook")
        elif "close outlook" in txt.lower():
            try:
                subprocess.Popen("TASKKILL /F /IM OUTLOOK.EXE")
                speak("microsoft outlook is closing...")
            except Exception as e:
                speak("Error in closing microsoft outlook")
        elif "open steam" in txt.lower():
            try:
                subprocess.Popen([steam])
                speak("steam is launching... happy gaming!")
            except Exception as e:
                speak("Error in launching steam. check your internet connection")
        elif "close steam" in txt.lower():
            try:
                subprocess.Popen("TASKKILL /F /IM steam.exe")
                speak("steam is closing...")
            except Exception as e:
                speak("Error in closing steam")
        elif "open discord" in txt.lower():
            try:
                subprocess.Popen([discord])
                speak("discord is launching... happy gaming!")
            except Exception as e:
                speak("Error in launching discord. check your internet connection")
        elif "close discord" in txt.lower():
            try:
                subprocess.Popen("TASKKILL /F /IM Update.exe")
                speak("discord is closing...")
            except Exception as e:
                speak("Error in closing discord")
        elif "open telegram" in txt.lower():
            try:
                subprocess.Popen([telegram])
                speak("telegram is launching... ")
            except Exception as e:
                speak("Error in launching telegram. check your internet connection")
        elif "close telegram" in txt.lower():
            try:
                subprocess.Popen("TASKKILL /F /IM steam.exe")
                speak("telegram is closing...")
            except Exception as e:
                speak("Error in closing telegram")
        elif "open viking" in txt.lower():
            try:
                subprocess.Popen([valheim])
                speak("valheim is launching... enjoy your viking life!")
            except Exception as e:
                speak("Error in launching valheim. please open steam first!")
        elif "close viking" in txt.lower():
            try:
                subprocess.Popen("TASKKILL /F /IM valheim.exe")
                speak("valheim is closing...")
            except Exception as e:
                speak("Error in closing valheim")
        elif "open work" in txt.lower():
            try:
                subprocess.Popen(['explorer', work])
                speak("work folder is opening... work hard for success your dreams!")
            except Exception as e:
                speak("Error in opening work folder. may be you have deleted it!")
        elif "screenshot" in txt.lower():
            speak("here is your screenshot of the current program")
            path = r"Z:\Desktop\S1"
            pwk.take_screenshot(path)
            speak("I think it's pretty good")
        elif "show history" in txt.lower():
            pwk.show_history()
        elif any(keyword in txt.lower() for keyword in ["hi", "hello", "hey", "what's up", "hey baby", "hey girl", "hello baby", "hello girl", "hi baby", "hi girl","nice to meet you","Pleased to meet you","Whats new?" , "Whats going on?", "Good to see you", "Nice to see you", "Long time no see", "Its been a while", "Yo!", "Alright mate?","Howdy!", "Whazzup?", "Hello there!", "Sup?", "Hiya!", "Ahoy!", "Hello stranger!","Whats up buttercup"]):
                chatbot_response = get_chatbot_response(txt)
                speak(chatbot_response)
        elif any(keyword in txt.lower() for keyword in ["Good morning", "good day", "morning"]):
                chatbot_response = get_chatbot_response(txt)
                speak(chatbot_response)
        elif any(keyword in txt.lower() for keyword in ["good night", "night"]):
                chatbot_response = get_chatbot_response(txt)
                speak(chatbot_response)
        elif any(keyword in txt.lower() for keyword in ["Good bye!", "Bye!", "farewell", "see you", "take care", "happy farewell", "bye take care", "bye see you soon", "bye see you", "Good bye take care", "good bye see you soon", "good bye see you again", "goodbye", "bye", "by"]):
                chatbot_response = get_chatbot_response(txt)
                speak(chatbot_response)
        elif "self destruction" in txt.lower():
            speak("closing the project Freya... farewell!")
            break
        else:
            speak("sorry I cannot understand you, repeat it again!")
    except sr.UnknownValueError:
        continue



