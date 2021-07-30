#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Exer

Generate a first name, last name and nickname based on the names of Brazilian football players.
Names sourced from: https://pt.wikipedia.org/wiki/Apelidos_do_futebol

"""
import random
import sys

def main():
    """Choose a first name, nickname, last name at random and print to the screen."""
    first_name = ("Ademir", "Adílio", "Adriano", "Alcinho", "Aldair",
    "Alecsandro", "Alex", "Aloíso", "Amaral", "Amarildo", "Baltazar",
    "Bino", "Coutinho", "Carlos", "Cafu", "Didi", "Dirceu", "Donizete",
    "Douglas", "Dunga", "Edmundo", "Everton", "Ézio", "Falcão", "Friaça",
    "Garrincha", "Hernane", "Idário", "Jael", "Julio", "Junior", "Kaká",
    "Kerlon", "Leandro", "Leônidas", "Magno", "Marcos", "Marinho", "Luizinho",
    "Neto", "Nunes", "Pedro", "Paulo", "Oberdan", "Obina", "Pelé", "Ronaldinho",
    "Reinaldo", "Rogério", "Romário", "Romeu", "Ronaldo", "Basíliom", "Pepe",
    "Sávio", "Toninho", "Tiago", "Sócrates", "Tostão", "Vavá", "Vampeta",
    "Walter", "Tuffy", "Zagallo", "Zé", "Zico", "Zizinho")

    nickname = ("Divino", "Queixada", "Neguinho Bom de Bola", "L'Imperatore",
    "Bugre", "Bugre Xucro", "Imperador", "Pluto", "Alecgol", "Pirulito",
    "Boi Bandido", "Coveiro", "O Possesso", "Tromba", "Biro-Biro", "Pé de Anjo",
    "Cabecinha de Ouro", "Monstro do Maracanã", "Alegria nas Pernas",
    "Gato Preto", "General", "Capitão", "Predador", "Capita", "São Castilho",
    "Leiteria", "Anjo aos 45", "O Gerente", "Príncipe", "Maravilha", "Beija-flor",
    "Peito de Aço", "Príncipe Etíope", "Folha Seca", "Formiguinha", "Pantera",
    "Capitão", "Bomba de Vespasiano", "Capetinha", "Cavalo", "Animal",
    "O Garoto de Ouro", "Filho do Vento", "Cebolinha", "Rei de Roma",
    "Maravilha Negra", "Touro Sentado", "Caça-Rato", "Gigante de Ébano",
    "Alegria do Povo", "Anjo das Pernas Tortas", "Mané", "Messias",
    "O Muro Invisível", "Canhotinha de Ouro", "Ceifador", "Brocador",
    "Profeta", "Sangue Azul", "O Cruel", "Reizinho da Colina", "A Fera",
    "Capacete", "Foquinha", "Peixe-frito", "Homem Borracha", "Pelé Branco",
    "Fabuloso", "Pequeno Polegar", "Magnata", "Mago", "Diabo Loiro", "R10",
    "Canhão do Nordeste", "Xodó da Fiel", "Craque Neto","João Danado",
    "Pingo de Ouro", "Diabo Loiro", "Viola", "Tupãzinho", "Baixinho", "M1to",
    "Talismã da Fiel", "Lela", "Rei", "Patada Atômica", "Rei das Pedaladas",
    "Cambalhota", "Fenômeno", "Bruxo", "R9", "O Bailarino", "Mineirinho de Ouro",
    "O Satanás", "Formiguinha", "Galinho de Quintino", "Velho Lobo",
    "Coração Valente")


    last_name = ("da Guia", "Menezes", "Silva", "Martha de Freitas",
    "Santos do Nascimento", "José da Silva Filho", "Friedenreich",
    "Alberto Torres", "Fabian", "Morais", "dos Santos", "Jorge de Lima",
    "Aleixo", "Augusto do Nascimento", "Barbosa", "Silva", "Freitas",
    "Dourado", "Baptista", "Pernanbucano", "da Silva", "Flávi", "Fabiano",
    "Carioca", "Chagas", "Santos", "Cattani", "Nunes", "Sérgio Rosa",
    "Francisco", "Grané", "Garcia", "Felisbino", "Rocha", "Ceni", "Gaúcho",
    "Cerezo", "Casagrande", "Washington", "Oliveira")

    print("Your name as a Brazilian football player is:")
    print("Seu nome de jogador de futebol brasileiro é:\n")

    while True:
        first = random.choice(first_name)
        nick = random.choice(nickname)
        last = random.choice(last_name)

        print(f'{first} "{nick}" {last}\n', file=sys.stderr)

        try_again = input("Try again? (Type 'no' to quit)\n")
        if try_again.lower() == "no":
            break
    print("Até mais!")

if __name__ == "__main__":
    main()
