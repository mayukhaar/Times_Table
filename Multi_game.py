print("MULTIPLICATION GAME:")
print("*********************")
print("Instructions: Enter the answers in numeric values. ")
print("         ")
invalid = 0
complexity = 10
y = 10
for x in range(y):
    from random import randint
    num_1 = randint(0, complexity)
    from random import randint
    num_2 = randint(0, complexity)
    print(str(num_1) + " * " + str(num_2) + ":")
    answer = input("Answer:")
    correct = num_1 * num_2
    if answer == str(correct):
        print("Correct!")
    else:
        print("Incorrect. :(")
        invalid = invalid + 1
print("_______________________________________________")
print("|Thank you for playing! Here are your results!|")
print("|Number of invalid responses:" + str(invalid) + "                |")
print("|Number of correct responses:" + str(correct) + "/" + str(y) + "             |")
print("_______________________________________________")

#show number of wrong events and number of correct answers/responses