name = input("Type your name: ")
print("Welcome", name, "to the adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right.Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or can swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swan accross and get eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = print(
        "You come to a bridge, it looks wobbly, do you want to cross it or head black (cross/back)? ")

else:
    print("Not a valid option. You lose.")
