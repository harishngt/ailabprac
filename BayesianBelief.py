import random

def monty_hall_simulation(num_trials):
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_trials):
        # print("")
        # print(f"{_} iteration ")
        doors = ['A', 'B', 'C']
        bike_location = random.choice(doors)
        # print("Bike location : ",bike_location)
        initial_choice = random.choice(doors)
        # print("player choice: ",initial_choice)
        doors.remove(initial_choice)

        if bike_location in doors:
            doors.remove(bike_location)
        monty_choice = random.choice(doors)

        # print("Monty's choice : ", monty_choice)
        doors = [d for d in ['A', 'B', 'C'] if d != monty_choice and d != initial_choice]
        final_choice = doors[0]

        stay_wins += (initial_choice == bike_location)
        switch_wins += (final_choice == bike_location)

    stay_win_prob = stay_wins / num_trials
    switch_win_prob = switch_wins / num_trials

    print(f"Probability of winning by staying: {stay_win_prob:.2f}")
    print(f"Probability of winning by switching: {switch_win_prob:.2f}")

# Number of trials
num_trials = 10

# Run simulation
monty_hall_simulation(num_trials)
