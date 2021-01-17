print("MULTIPLICATION GAME:")
print("*********************")
print("Instructions: Enter the answers in numeric values. ")
print("         ")
repeat = "Y"
invalid = 0
while repeat == "Y" or repeat == "y":

    print("9 x 1 =")
    answer_1 = input("Answer:")
    if answer_1 == "9":
        print("Correct!")
        print("8 x 2 =")
        answer_2 = input("Answer:")
        if answer_2 == "16":
            print("Correct!")
            print("5 x 5 =")
            answer_3 = input("Answer:")
            if answer_3 == "25":
                print("Correct!")
                print("7 x 3 =")
                answer_4 = input("Answer:")
                if answer_4 == "21":
                    print("Correct!")
                    print("2 x 6 =")
                    answer_5 = input("Answer:")
                    if answer_5 == "12":
                        print("Correct!")
                        print("4 x 3 =")
                        answer_6 = input("Answer:")
                        if answer_6 == "12":
                            print("Correct!")
                            print("8 x 9 =")
                            answer_7 = input("Answer:")
                            if answer_7 == "72":
                                print("Correct!")
                                print("3 x 10 =")
                                answer_8 = input("Answer:")
                                if answer_8 == "30":
                                    print("Correct!")
                                    print("5 x 4 =")
                                    answer_9 = input("Answer:")
                                    if answer_9 == "20":
                                        print("Correct!")
                                        print("10 x 10 =")
                                        answer_10 = input("Answer:")
                                        if answer_10 == "100":
                                            print("Correct!")
                                            print("Number of invalid attempts:" + str(invalid))
                                            break
                                        else:
                                            print("Invalid Response.")
                                            invalid = invalid + 1
                                            repeat = input("Do you want to try again? (Y/N)")
                                    else:
                                        print("Invalid Response.")
                                        invalid = invalid + 1
                                        repeat = input("Do you want to try again? (Y/N)")
                                else:
                                    print("Invalid Response.")
                                    invalid = invalid + 1
                                    repeat = input("Do you want to try again? (Y/N)")
                            else:
                                print("Invalid Response.")
                                invalid = invalid + 1
                                repeat = input("Do you want to try again? (Y/N)")
                        else:
                            print("Invalid Response.")
                            invalid = invalid + 1
                            repeat = input("Do you want to try again? (Y/N)")
                    else:
                        print("Invalid Response.")
                        invalid = invalid + 1
                        repeat = input("Do you want to try again? (Y/N)")
                else:
                    print("Invalid Response.")
                    invalid = invalid + 1
                    repeat = input("Do you want to try again? (Y/N)")
            else:
                print("Invalid Response.")
                invalid = invalid + 1
                repeat = input("Do you want to try again? (Y/N)")
        else:
            print("Invalid Response.")
            invalid = invalid + 1
            repeat = input("Do you want to try again? (Y/N)")
    else:
        print("Invalid Response.")
        invalid = invalid + 1
        repeat = input("Do you want to try again? (Y/N)")



