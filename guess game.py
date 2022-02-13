#guess game

secrete_word = "diamond"
guess = ""

guess_count = 0
guess_limit = 3
out_of_guess = False

while guess!= secrete_word and not(out_of_guess) :
    if guess_count < guess_limit :
        guess = input("guess world : ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess :
    print("lost the game")
else:
    print("won the game !")
