with open("invited_names.txt") as f:
    names = f.readlines()
    names = [name.strip() for name in names]

for name in names:
    with open("starting_letter.txt", mode="r+") as f:
        letter = f.read()
        letter = letter.replace("[name]", name)

    with open(f"./ReadyToSend/letter_to_{name}", mode= "w") as f:
        f.write(letter)
