from openai import OpenAI
from random import randint
import streamlit as st

OPENAI_API_KEY = st.getenv(st.secrets[openai_api])

diseases = [
    "COVID-19",
    "Alzheimer’s disease",
    "Diabetes I",
	"Diabetes II",
    "Influenza",
	"Pneumonia",
    "Kidney Cancer",
    "Liver Cancer",
    # "Hypertension",
    # "Obesity",
    # "Drug overdose",
    "Parkinson’s disease",
    "HIV/AIDS",
    # "Liver cirrhosis",
    # "Osteoarthritis",
    # "Rheumatoid arthritis",
    "Depression",
    # "Gastroesophageal reflux disease",
    "Asthma",
    # "COPD",
    "Epilepsy",
    "Breast cancer",
    # "Prostate cancer",
    # "Colon cancer",
    # "Pancreatic cancer",
    "Leukemia",
    "Lung cancer",
    "Skin cancer",
    # "Hepatitis",
    # "Glaucoma",
    # "Cataracts",
    "Dementia",
    # "Multiple sclerosis",
    # "Endometriosis",
    # "Sickle cell anemia",
    # "Celiac disease",
    # "Crohn’s disease",
    # "Ulcerative colitis",
    # "Lupus",
    # "Fibromyalgia",
    # "Sleep apnea",
    "Osteoporosis",
    "Hemorrhoids",
    # "Gout",
    # "Psoriasis",
    "Tuberculosis",
    # "Lyme disease",
    # "Chlamydia",
    # "Gonorrhea",
    "Syphilis",
    "Herpes",
    # "Human papillomavirus",
    "Measles",
    # "Mumps",
    # "Rubella",
    "Varicella (chickenpox)",
    "Zika virus",
    # "West Nile virus",
    "Ebola",
    "Malaria",
    "Yellow fever",
    "Cholera",
    # "Typhoid fever",
    # "Dengue fever",
    # "Lassa fever",
    # "Hantavirus",
    "Rabies",
    "Tetanus",
    # "Botulism",
    # "Anthrax",
    # "Black Plague",
    # "Smallpox",
    # "Polio",
    # "Norovirus",
    # "Salmonella",
    # "E. coli infection",
    # "Listeria",
    # "Campylobacter",
    # "Toxoplasmosis",
    # "Cryptosporidiosis",
    # "Giardiasis",
    # "Trichomoniasis",
    # "Scabies",
    "Head Lice",
    # "Ringworm infestation",
    # "Pinworm infection",
    "Bedbugs",
    # "MRSA (methicillin-resistant Staphylococcus aureus)",
    # "Clostridioides difficile infection",
    # "Legionnaires’ disease",
    "Tuberculosis",
	"Hepatitis",
    "Syphilis",
    # "Gonorrhea",
    "Chlamydia"
    # "Human papillomavirus (HPV)",
    # "Herpes simplex virus (HSV)",
    # "Trichomoniasis",
    # "Pelvic inflammatory disease (PID)",
    # "Genital warts",
    # "Genital herpes",
    # "Chancroid",
    # "Lymphogranuloma venereum (LGV)",
    # "Granuloma inguinale",
    # "Molluscum contagiosum",
]

def getDisease():
	return diseases[randint(0, len(diseases) - 1)]

client = OpenAI(api_key=OPENAI_API_KEY)
def reload():
    global disease, patient
    disease = getDisease()

disease = getDisease()

thread = client.beta.threads.create()

def guess(tried):
    """
    The user guessed a disease.
    """
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "user", "content": f"Return a common characteristic shared between {disease} and {tried} without mentioning the word {disease}. If {tried} and {disease} are the same, print the statement 'True' instead. If {tried} is not a disease, then print the statement 'False' instead."}
    ]
    )
    return (response.choices[0].message.content)

def hint():
    """
    The user wants a hint
    """
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "user", "content": f"Return a defining characteristic of {disease}. Do not include the word {disease} in your response."}
    ]
    )
    return (response.choices[0].message.content)


def give_up(): return disease

def fun_fact():
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "user", "content": f"Give me two sentences about {disease}; one about the symptoms, one about how to prevent the disease."}
    ]
    )
    return (response.choices[0].message.content)
