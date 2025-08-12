import random
#from flask import Flask
import requests
from pokemon import Pokemon
from conversion import height, weight


def select_level():
    while True:
        level = input("Select level:\n(1) - Easy\n(2) - Hard\n>>> ")
        if level in ('1', '2'):
            return level            
        else:
            print("Invalid Input.")

def max_guesses(n):
    if n == '1':
        return 20
    elif n == '2':
        return 10
    
def play_again():
    while True:
        restart = input("Play Again?:\n(Y) - YES\n(N) - NO\n>>>").lower()
        if restart in ('y', 'n'):
            return restart == 'y'


pokemon_id = random.randint(1, 150)
random_pk_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/")
random_pk_species_response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}/")
random_pk = random_pk_response.json()
random_pk_species = random_pk_species_response.json()

def main():
    play_game = True 
    while play_game:
        pokemon_id = random.randint(1, 150)
        random_pk_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/")
        random_pk_species_response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}/")
        random_pk = random_pk_response.json()
        random_pk_species = random_pk_species_response.json()

        hidden_pokemon = Pokemon(name=random_pk['name'],
                                 height=random_pk['height'],
                                 weight=random_pk['weight'],
                                 poketype=random_pk['types'][0]['type']['name'],
                                 color=random_pk_species['color']['name'])

        level = select_level()
        max_guesses = max_guesses(level)
        guesses = 0

        while guesses < max_guesses:




    