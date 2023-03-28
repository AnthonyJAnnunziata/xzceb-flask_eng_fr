"""
This is a module that has functions to translate English strings to French, 
and French strings to English.
"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

"""
This is a function the translates an English string to a French string.
It takes a string "english_text" and translates it to French and returns it 
as "french_text" at the end.
"""
def english_to_french(english_text):
    if english_text is None:
        french_text = "Error: Input parameter is null"
    else: 
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()['translations'][0]['translation']

    return french_text

"""
This is a function the translates a French string to an English string.
It takes a string "french_text" and translates it to English and returns it 
as "english_text" at the end.
"""
def french_to_english(french_text):
    if french_text is None:
        english_text = "Error: Input parameter is null"
    else: 
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()['translations'][0]['translation']

    return english_text
    