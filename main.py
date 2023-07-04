import random

def simulate_flips(starting_amount, bet, flips, win_probability):
    balance = starting_amount

    for _ in range(flips):
        coin_flip = random.random()  # Returns a random float number between 0.0 to 1.0
        if coin_flip < win_probability:
            balance += bet
        else:
            balance -= bet

    return balance

starting_amount = 15000
bet = 300
flips = 80
win_probability = 0.66  # 66%

final_balance = simulate_flips(starting_amount, bet, flips, win_probability)

#Get the average of 1000 simulations
simulations = 1000
ending_balances = []
for _ in range(simulations):
    ending_balances.append(simulate_flips(starting_amount, bet, flips, win_probability))

average_ending_balance = sum(ending_balances) / len(ending_balances)
print("Average ending balance: ", average_ending_balance)
