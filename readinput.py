print("Hello. :)")

name = input("What is your name? ")
print("Nice to meet you " + name + "!")

age = input("How old are you, " + name + "? ")
print("So, you are already " + str(age) + " years old, " + name + "!\nCONNGRATULATIONS!!!")

ans = input("Is today your birthday, " + name + "? ")
if 'Y' in ans or 'y' in ans:
    print('HAPPY BIRTHDAY!!!')
else:
    print('That\'s too bad. :(')

x = int(input("Please enter an integer: "))
print('Your number is', x)
#another way to write
print('Your number is {0}'.format(x))

y = float(input("Please enter an integer: "))
print("Your number is "+str(y)+".")
print('Your number is {0}.'.format(y))

