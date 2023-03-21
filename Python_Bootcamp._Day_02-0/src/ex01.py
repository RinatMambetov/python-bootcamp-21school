import random
from collections import Counter
import sys


class Game(object):
    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        moves_history = {'player1': [], 'player2': []}
        self.registry[player1.name] = self.registry.get(player1.name, 0)
        self.registry[player2.name] = self.registry.get(player2.name, 0)
        for match in range(self.matches):
            p1 = player1.decide(moves_history['player2'])
            p2 = player2.decide(moves_history['player1'])
            if p1:
                if p2:
                    self.registry[player1.name] += 2
                    self.registry[player2.name] += 2
                else:
                    self.registry[player1.name] -= 1
                    self.registry[player2.name] += 3
            elif p2:
                self.registry[player1.name] += 3
                self.registry[player2.name] -= 1
            moves_history['player1'].append(p1)
            moves_history['player2'].append(p2)

    def top3(self):
        for top_player in self.registry.most_common(3):
            print(top_player[0], top_player[1])

    def default_game(self, players, clear_registry=False):
        if clear_registry:
            self.registry = Counter()
        for n, player1 in enumerate(players):
            for player2 in players[n + 1:]:
                self.play(player1, player2)
        self.top3()


class Player:
    def __init__(self, name='random_player'):
        self.name = name

    def decide(self, history):
        return random.choice([True, False])


class Cheater(Player):
    def __init__(self):
        super().__init__(name='cheater')

    def decide(self, history):
        return False


class Cooperator(Player):
    def __init__(self):
        super().__init__(name='cooperator')

    def decide(self, history):
        return True


class Copycat(Player):
    def __init__(self):
        super().__init__(name='copycat')

    def decide(self, history):
        if history:
            return history[-1]
        else:
            return True


class Grudger(Player):
    def __init__(self):
        super().__init__(name='grudger')

    def decide(self, history):
        if False in history:
            return False
        return True


class Detective(Player):
    def __init__(self):
        super().__init__(name='detective')

    def decide(self, history):
        rounds = len(history)
        if not history or rounds in (0, 2, 3):
            return True
        elif rounds == 1:
            return False
        elif False in history[:4]:
            return history[-1]
        return False


class Copykitten(Player):
    def __init__(self):
        super().__init__(name='copykitten')

    def decide(self, history):
        if len(history) > 1 and history[-1] is False and history[-2] is False:
            return False
        else:
            return True


class Insider(Player):
    def __init__(self):
        super().__init__(name='insider')

    def decide(self, history):
        matches = sys._getframe(2).f_locals['self'].matches
        if not history:
            return True
        if history and len(history) < matches - 1:
            return history[-1]
        return False


class Inspector(Player):
    def __init__(self):
        super().__init__(name='inspector')

    def decide(self, history):
        player_types = (type(sys._getframe(2).f_locals['player1']).__name__,
                        type(sys._getframe(2).f_locals['player2']).__name__)
        if "Detective" in player_types:
            if len(history) <= 3:
                return False
            else:
                return True
        elif "Cooperator" in player_types or "Cheater" in player_types:
            return False
        else:
            return True


class NSA(Player):
    def __init__(self):
        super().__init__(name='NSA')

    def decide(self, history):
        matches = sys._getframe(2).f_locals['self'].matches
        if len(history) == matches - 1:
            return False
        player_types = (type(sys._getframe(2).f_locals['player1']).__name__,
                        type(sys._getframe(2).f_locals['player2']).__name__)
        if "Detective" in player_types:
            if len(history) <= 3:
                return False
            else:
                return True
        elif "Cooperator" in player_types or "Cheater" in player_types:
            return False
        else:
            return True

if __name__ == '__main__':
    game = Game()
    players = [Cheater(), Cooperator(), Copycat(), Grudger(), Detective()]
    print("+++ default: 5x1, 10 matches:")
    game.default_game(players)
    print(game.registry)
    assert game.registry == Counter({'copycat': 57, 'grudger': 46, 'cheater': 45, 'detective': 45, 'cooperator': 29})

    print("+++ default: 5x1, 100 matches:")
    game.matches = 100
    game.default_game(players, clear_registry=True)
    print(game.registry)

    print("+++ default: 5x1, 1000 matches:")
    game.matches = 1000
    game.default_game(players, clear_registry=True)
    print(game.registry)

    print("+++ default: 5x10, 100 matches:")
    players *= 10
    game.matches = 100
    game.default_game(players, clear_registry=True)
    print(game.registry)

    print("+++ default: 5x10, 10 matches each:")
    game.matches = 10
    game.default_game(players, clear_registry=True)
    print(game.registry)

    print("---------------------------------------")
    players = [Cheater(), Cooperator(), Copycat(), Grudger(), Detective(), Copykitten()]
    print("+++ default + copykitten: 6x1, 10 matches:")
    game.matches = 10
    game.default_game(players)
    print(game.registry)

    print("+++ default + copykitten: 6x1, 100 matches:")
    game.matches = 100
    game.default_game(players, clear_registry=True)
    print(game.registry)

    print("+++ default + copykitten: 6x1, 1000 matches:")
    game.matches = 1000
    game.default_game(players, clear_registry=True)
    print(game.registry)

    print("+++ default + copykitten: 6x10, 100 matches:")
    players *= 10
    game.matches = 100
    game.default_game(players, clear_registry=True)
    print(game.registry)

    print("+++ default + copykitten: 6x10, 10 matches each:")
    game.matches = 10
    game.default_game(players, clear_registry=True)
    print(game.registry)

    print("---------------------------------------")
    game2 = Game()
    players2 = [Cheater(), Cooperator(), Copycat(), Grudger(), Detective(), Insider(), Inspector(), NSA()]

    print("+++ new: 6x1, 10 matches:")
    game2.default_game(players2, clear_registry=True)
    print(game2.registry)

    print("+++ new: 6x1, 100 matches:")
    game2.matches = 100
    players2[5].matches = 100
    players2[7].matches = 100
    game2.default_game(players2, clear_registry=True)
    print(game2.registry)

    print("+++ new: 6x1, 1000 matches:")
    game2.matches = 1000
    players2[5].matches = 1000
    players2[7].matches = 1000
    game2.default_game(players2, clear_registry=True)
    print(game2.registry)

    players2[5].matches = 10
    players2[7].matches = 10
    players2 *= 10

    # print("+++ new: 6x10, 100 matches:")    #
    # game2.matches = 100
    # game2.default_game(players2, clear_registry=True)
    # print(game2.registry)

    print("+++ new: 6x10, 10 matches:")
    game2.matches = 10
    game2.default_game(players2, clear_registry=True)
    print(game2.registry)
