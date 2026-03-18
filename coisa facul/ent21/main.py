import random

# ----- Configuração -----

CARD_VALUES = list(range(1, 12))

class Player:
    def __init__(self, name, classe):
        self.name = name
        self.classe = classe
        self.hand = []
        self.trumps = 3
        self.used_power = False
        self.standing = False

    def total(self):
        return sum(self.hand)

    def show_hand(self):
        return f"{self.hand} (Total: {self.total()})"


# ----- Baralho -----

def create_deck():
    deck = CARD_VALUES.copy()
    random.shuffle(deck)
    return deck


def draw_card(deck):
    if not deck:
        deck.extend(create_deck())
    return deck.pop()


# ----- Habilidades de Classe -----

def blindfold(player, opponent, deck):
    if player.trumps < 3 or player.used_power:
        print("Não pode usar Blindfold.")
        return

    player.trumps -= 3
    player.used_power = True

    card = draw_card(deck)
    opponent.hand.append(card)

    print(f"{opponent.name} comprou uma carta sem ver!")


def scissors(player, deck):
    if player.trumps < 2 or player.used_power:
        print("Não pode usar Scissors.")
        return

    player.trumps -= 2
    player.used_power = True

    value = int(input("Escolha um valor para remover do baralho: "))

    while value in deck:
        deck.remove(value)

    print(f"Todas as cartas {value} foram removidas.")


def gambler(player, deck):
    if player.trumps < 2 or player.used_power:
        print("Não pode usar Gambler.")
        return

    player.trumps -= 2
    player.used_power = True

    c1 = draw_card(deck)
    c2 = draw_card(deck)

    print(f"Cartas sorteadas: {c1} e {c2}")

    choice = int(input("Escolha qual manter (1 ou 2): "))

    if choice == 1:
        player.hand.append(c1)
    else:
        player.hand.append(c2)


# ----- Turno -----

def player_turn(player, opponent, deck):

    while not player.standing:

        print(f"\nTurno de {player.name}")
        print(player.show_hand())
        print(f"Trunfos: {player.trumps}")

        action = input("1-Hit | 2-Stand | 3-Habilidade: ")

        if action == "1":
            card = draw_card(deck)
            player.hand.append(card)
            print(f"Comprou {card}")

            if player.total() > 21:
                print("BUST! Passou de 21.")
                return

        elif action == "2":
            player.standing = True

        elif action == "3":

            if player.classe == "Blindfold":
                blindfold(player, opponent, deck)

            elif player.classe == "Scissors":
                scissors(player, deck)

            elif player.classe == "Gambler":
                gambler(player, deck)

        else:
            print("Ação inválida")


# ----- Jogo -----

def play():

    deck = create_deck()

    p1 = Player("Jogador 1", input("Classe Jogador 1: "))
    p2 = Player("Jogador 2", input("Classe Jogador 2: "))

    for p in [p1, p2]:
        p.hand.append(draw_card(deck))
        p.hand.append(draw_card(deck))

    player_turn(p1, p2, deck)
    player_turn(p2, p1, deck)

    print("\n--- Resultado ---")

    if p1.total() > 21 and p2.total() > 21:
        print("Todos perderam.")

    elif p1.total() > 21:
        print("Jogador 2 vence")

    elif p2.total() > 21:
        print("Jogador 1 vence")

    else:
        if p1.total() > p2.total():
            print("Jogador 1 vence")
        elif p2.total() > p1.total():
            print("Jogador 2 vence")
        else:
            print("Empate")


play()