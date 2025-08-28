import sys
import random
import requests
from pokemon import Pokemon


def select_level():
    while True:
        level = input("Select level:\n(1) - Easy\n(2) - Hard\n>>> ")
        if level in ('1', '2'):
            return level            
        else:
            print("Invalid Input.")

def number_of_guesses(n):
    if n == '1':
        return 20
    elif n == '2':
        return 10
    
def play_again():
    while True:
        restart = input("Play Again?:\n(Y) - YES\n(N) - NO\n>>>").lower()
        if restart in ('y', 'n'):
            return restart == 'y'
        else:
            print("Invalid Input.")

def main():
    play_game = True

    level = select_level()
    guesses = 0
    max_guesses = number_of_guesses(level)
    guesses_list = ['o' for g in range(max_guesses)]

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


        while guesses < max_guesses:
            win = False

            print("Guesses -> |", end=' ')
            for i in guesses_list:
                print(i, end=' | ')
            print()
            
            guess = input("Guess who I am: ").lower()
            try:
                guessed_pk_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{guess}/")
                guessed_pk_species_response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{guess}/")
                guessed_pk = guessed_pk_response.json()
                guessed_pk_species = guessed_pk_species_response.json()
                pkmn = Pokemon(name=guessed_pk['name'],
                               height=guessed_pk['height'],
                               weight=guessed_pk['weight'],
                               poketype=guessed_pk['types'][0]['type']['name'],
                               color=guessed_pk_species['color']['name'])

            except AttributeError:
                print(f"{guess.capitalize()}...? I don't know that pokemon...\nCheck the spelling and try again. I won't count that as a guess.")
                continue

            else:
                guesses_list[guesses] = 'X'
                guesses += 1


            if hidden_pokemon.check_guess(pkmn):
                win = True
                break
            else:
                pkmn.declare_height_and_weight()
                print("So...")
                if hidden_pokemon.is_taller_than(pkmn):
                    print("I am taller and",  end=' ')
                else:
                    print("I am shorter and", end=' ')
                if hidden_pokemon.is_heavier_than(pkmn):
                    print(f"heavier than {pkmn.name}\n")
                else:
                    print(f"lighter than {pkmn.name}\n")
                if (not hidden_pokemon.poketype_revealed) and (hidden_pokemon.has_same_type_as(pkmn)):
                    hidden_pokemon.reveal_type(pkmn)
                if (not hidden_pokemon.color_revealed) and (hidden_pokemon.has_same_color_as(pkmn)):
                    hidden_pokemon.reveal_color(pkmn)
        if win:
            print(f"You're right!! I am {hidden_pokemon.name}")
            print(f"You found me with {guesses} guesses\n")
        else:
            print(f"You lost... I'm {hidden_pokemon.name}\n")
        
        play_game = play_again()
    
    sys.exit("Thanks for playing!!!")


if __name__ == "__main__":
    main()