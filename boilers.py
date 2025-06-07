name = input("Please tell me your name:")

if name != "Jerry":
    portions = int(input("How many portions of soup?"))

    total = round(portions * 5.9, 2)

    print(f"The total cost is {total}")

print("Next please!")