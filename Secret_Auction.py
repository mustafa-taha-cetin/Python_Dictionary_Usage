
names = {
}

bets = {
}

start = "yes"
order = 0
print("--------------------------------------")
print("Welcome to the secret auction program.")
print("--------------------------------------")

while start == "yes":
    order += 1

    name = str(input("What is your name? \n"))
    bet = int(input("What's your bid? \n"))

    names[order] = name
    bets[order] = bet

    start = str(input("Are they any other bidders? Type 'yes' or 'no'. \n")).lower()
    print("                                              ")


start_bet = list(bets.values())[0]

for key in bets:

    if start_bet > bets[key]:
        start_bet = start_bet
    elif start_bet < bets[key]:
        start_bet = bets[key]

name_order = next((k for k, v in bets.items() if v == start_bet), None)

print(f"The winner is {names[name_order]} with a bid of ${bets[name_order]}.")

