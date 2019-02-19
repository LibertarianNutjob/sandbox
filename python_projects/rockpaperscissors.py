p_1 = raw_input("Player 1, select paper, rock, or scissors\n\n").lower()
p_2 = raw_input("Player 2, select paper, rock, or scissors\n\n").lower()

choices = list(['paper', 'rock', 'scissors'])

if p_1 == p_2:
    print("It's a draw!")

if choices.index(p_1) == (choices.index(p_2) + 1) % 3:
    print("Player 2 wins!")
if choices.index(p_2) == (choices.index(p_1) + 1) % 3:
    print("Player 1 wins!")
