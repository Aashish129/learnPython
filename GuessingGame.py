import random

start_range = int(input("Hi!, Please Enter start of range of Number from which you want to guess\n"))

end_range = int(input("Hi!, Please End start of range of Number from which you want to guess\n"))

while end_range < start_range:
    print("Please end the end_range again, it needs to be smaller than start range")
    end_range = int(input())

full_list = list(range(start_range,end_range+1))

print("Okay, So You have your " + str(full_list) + " is here")

winnerguess = random.randrange(start_range,end_range+1)

#print(winnerguess)

user_guess = input("Enter Any Random Number from that start and end range you just entered\n")

if winnerguess == user_guess:
    print("You Guessed It Right!")
else:
    print("No, You Guessed Wrong!, Try again" "\U0001f600"  "the winner guess was " + str(winnerguess))





