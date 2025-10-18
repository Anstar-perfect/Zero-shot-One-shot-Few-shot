import os
from google import genai
from google.genai import types

client = genai.Client(api_key ='AIzaSyBTM5aD8Ngvhg_j0YonkJACURE8Hdb3iWY')

def generate_response(prompt,temperature=0.3):
    try:
        contents = [types.Content(role='user',parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(model='gemini-2.0-flash',contents=contents,config=config_params)
        return response.text
    except Exception as e:
        return f"Error:{str(e)}"
    
def run_acticity():
    print('\n=== ZERO-SHOT, ONE-SHOT, FEW-SHOT LEARNING ACTIVITY === ')

    category=input('Enter a category(e.g. animal,food etc. :)') 
    item = input(f"Enter a specific {category} to classify:")

    #zero shot
    print('\n--- Zero Shot ---')
    zero_shot = f'Is {item} a {category}? Anwer in yes or no.'  
    print(f"Prompt: {zero_shot}") 
    print(f"Response :{generate_response(zero_shot)}")

    #One shot
    print('\n--- One Shot ---')
    one_shot = f"""Determine if the item belongs to the category.

Example:
Category = fruit
item : apple
Answer : Yes, Apple is a fruit

Now you try:
Category = {category}
item : {item}
Answer :"""
    print(f"Response:{generate_response(one_shot)}")

    #few shot
    print('\n--- Few Shot ---')
    few_shot = f"""Determine if the item belongs to the category.
Example 1 :
Category = fruit
item : apple
Answer : Yes, Apple is a fruit

Example 2 :
Category = fruit
item : carort
Answer : No , carrot is not a fruit

Now you try
Category = {category}
item : {item}
Answer :"""
    print(f"Response: {generate_response(few_shot)}")

    print('\n--- Creative Few Shot Example---')
    creative = f"""Write a one sentence story about a given word
Example 1 :
Word:moon
Story : The moon winked at the lovers as they shared their first kiss

Example 2 :
word:computer
Story: the computer signed as another cup of coffee was spilled on its keyboard

word:{item}
Story:"""
    print(f"Response :{generate_response(creative)}")

    #Reflection
    print("1. How did the response differ between zero-shot to few-shot?")
    print('2. Which approach gave the most helpful or accurate response?')
    print("3. How did the examples in the few-shot prompt infulence the model's output?")

if __name__=='__main__':
    run_acticity()    