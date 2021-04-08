#!/usr/bin/ env python3
# 05/03/2020
# @uthor Drake Greeott
# Create a program that allows you to store the data for players of a game.

import db
from business import Player

def display_title():
    print("Player Manager")
    print()
    display_menu()

def display_menu():
    print("COMMAND MENU")
    print("view - View players")
    print("add - Add a player")
    print("del - Delete a player")
    print("exit - Exit program")
    print()

def display_players():
    line_format = "{:25s} {:10s} {:10s} {:10s} {:10s}"
    print(line_format.format("Name", "Wins", "Losses", "Ties", "Games"))
    print("-" * 64)
    players = db.get_stats()
    for player in players:
        print(line_format.format(player.name, str(player.wins),
                                 str(player.losses), str(player.ties),
                                 str(player.games)))
    print()

def add_player():
    name = input("Name: ")
    wins = input("Wins: ")
    losses = input("Losses: ")
    ties = input("Ties: ")

    new_add = Player(name=name.capitalize(), wins=wins, losses=losses, ties=ties)
    db.add_player(new_add)
    print(name.capitalize(), "was added to database.")
    print()


def delete_player():
    name = input("Name: ")
    db.delete_player(name.capitalize())
    print(name.capitalize(), "was deleted from database.")
    print()

def main():
    db.connect()
    display_title()
    while True:
        command = input("Command: ")
        if command == "view":
            display_players()
        elif command == "add":
            add_player()
        elif command == "del":
            delete_player()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")


if __name__ == "__main__":
    main()
