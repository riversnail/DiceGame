import random
import time

class Dice:
    def __init__(self):
        self.val = 0
    def throw(self):
        self.val = random.randint(1, 6)

class Game:
    def __init__(self,num_dices):
        self.dices = [Dice() for i in range(num_dices)]
        self.num_dices = num_dices
        self.score = 0
    def roll(self):
        min_score = [float('inf'),0]
        three_index = []
        for index, dice in enumerate(self.dices):
            dice.throw()
            if dice.val == 3:
                three_index.append(index)
            elif dice.val < min_score[0]:
                min_score[0] = dice.val
                min_score[1] = index
        if len(three_index) > 0:
            for index in reversed(three_index):
                del self.dices[index]
                self.num_dices -= 1
        else:
            self.score += min_score[0]
            del self.dices[min_score[1]]
            self.num_dices -= 1

    def play(self):
        while self.num_dices > 0:
            self.roll()
        return self.score

def simulate_game(iterations,num_dices):
    result = [0] * int(num_dices*6+1)
    for i in range(iterations):
        game = Game(num_dices)
        game.play()
        result[game.score] += 1
    return result

def main():
    num_dices = 5
    num_iterations = 10000
    start_time = time.time()
    result_lst = simulate_game(num_iterations,num_dices)
    print(f'Number of simulations was {num_iterations} using {num_dices} dice.')
    for i in range(len(result_lst)):
        if result_lst[i] >0:
            print(f'Total {i} occurs {result_lst[i]/num_iterations} occurred {result_lst[i]} times.')
    time_elapsed = round(time.time() - start_time, 2)
    print(f'Total simulation took {time_elapsed} seconds.')
if __name__ == "__main__":
    main()
