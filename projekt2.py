'''
FILNAMN.PY: Beskrivning av fil/program

__author__  = "David Berno"
__version__ = "1.0.0"
__email__   = "David.berno@elev.ga.ntig.se"
'''

# skapade en tom lista för vännerna
from msvcrt import getwch


friends_list = []

# koden för att lägga till en vän
def add_friend():
    friend = input("Ange namnet på din vän: ")
    friends_list.append(friend)
    print(f"{friend} har lagts till i din vänlista.")

# koden för att ta bort en vän
def remove_friend():
    print("Din vänlista:")
    for i, friend in enumerate(friends_list):
        print(f"{i + 1}. {friend}")
    choice = input("Ange numret på vännen du vill ta bort: ")
    try:
        choice = int(choice)
        if choice > 0 and choice <= len(friends_list):
            removed_friend = friends_list.pop(choice - 1)
            print(f"{removed_friend} har tagits bort från din vänlista.")
        else:
            print("Funkar ej.")
    except ValueError:
        print("Skriv ett nummer.")

# koden som visar hur många vänner du har i listan
def show_friends_count():
    print(f"Antal vänner i din vänlista: {len(friends_list)}")

# loopen
while True:
    print("\nVälkommen till min lista")
    print("1. Lägg till en vän")
    print("2. Ta bort en vän")
    print("3. Visa antal vänner")
    print("4. Avsluta programmet")
    print("5. För att visa din lista")

    choice = getwch()
    print("Vad vill du göra?: ")
    if choice == "1":
        add_friend()
    elif choice == "2":
        remove_friend()
    elif choice == "3":
        show_friends_count()
    elif choice == "4":
        print("Programmet avslutas.")
        break
    elif choice =="5":
        print("---Din Lista---\n")
        for i in friends_list:
            print(i)
    else:
        print("Funkar ej. Försök igen.")