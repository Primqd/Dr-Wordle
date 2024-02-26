from openai import OpenAI
from diseases import getDisease
from dotenv import load_dotenv
import os
# import streamlit as st

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# OPENAI_API_KEY = st.getenv(st.secrets[openai_api])

client = OpenAI(api_key=OPENAI_API_KEY)

disease = getDisease()

def reload():
    global disease # I don't like global, but I can't see a way of modifying on refresh :/
    disease = getDisease()

def guess(guessed_disease):
    """
    Guessed 'guessed_disease' as the disease.
    """
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "user", "content": 
        f"Return a common characteristic shared between {disease} and {guessed_disease} without mentioning the word {disease}. If {guessed_disease} and {disease} are the same, print the statement 'True' instead. If {guessed_disease} is not a disease, then print the statement 'False' instead."
        }
    ]
    )
    return (response.choices[0].message.content)

def hint():
    """
    Return a hint about the disease to the user.
    """
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "user", "content": f"Return a defining characteristic of {disease}. Do not include the word {disease} in your response."}
    ]
    )
    return (response.choices[0].message.content)


def give_up():
    """
    The user has given up on trying to guess the disease.
    """
    return disease

def fun_fact():
    """
    Returns fun facts about the disease.
    """
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "user", "content": f"Give me two sentences about {disease}; one about the symptoms, one about how to prevent the disease."}
    ]
    )
    return (response.choices[0].message.content)
