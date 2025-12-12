import random

def monty_hall_problem(switch):
    doors = ['car','goat','goat']
    random.shuffle(doors)
    initial_choice = random.choice(range(3))
    reveal_choices=[ i for i in range(3) if i != initial_choice and doors[i]!= 'car']
    reveal_choice = random.choice(reveal_choices)

    if switch:
        final_choice = [i for i in range(3) if i != initial_choice and i != reveal_choice][0]
    else:
        final_choice = initial_choice  

    return doors[final_choice] == 'car'      


def simulate_game(num_of_game):
    num_of_win_without_switch = sum(monty_hall_problem(switch=False) for _ in range(num_of_game))
    num_of_win_with_switch = sum(monty_hall_problem(switch=True) for _ in range(num_of_game))
    return num_of_win_without_switch, num_of_win_with_switch


example = simulate_game(1000000)
print(example)