
user_w = input("enter:").upper()

user_word = list(user_w)

for letter in user_word:
    if letter == "A":
        user_word.remove(letter)
    elif letter == "E":
        user_word.remove(letter)
    elif letter == "I":
        user_word.remove(letter)
    elif letter == "O":
        user_word.remove(letter)
    elif letter == "U":
        user_word.remove(letter)
    else:
        continue

print(user_word)