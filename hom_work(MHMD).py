import math

what_is = input("Enter your what\n\
+ plus\n\
- negetive\n\
* zarb\n\
/ taghsim\n\
** tavan\n\
sin -> x\n\
cos -> x\n\
degree -> radians\n\
log:\n\
  log(x , base) -> if x aloe base is e\n\         
: ")
def four():
    number_1 = input("Enter a number: ")
    number_2 = input("Enter a number: ")
    return number_1 , number_2
if what_is == "+":
    number_1 , number_2 = four()
    print("{} + {} = {}".format(number_1 , number_2 , number_1 + number_2))
elif what_is =="-":
    number_1 , number_2 = four()
    print("{} - {} = {}".format(number_1 , number_2 , number_1 - number_2))
elif what_is =="*":
    number_1 , number_2 = four()
    print("{} * {} = {}".format(number_1 , number_2 , number_1 * number_2))
elif what_is =="/":
    number_1 , number_2 = four()
    print("{} / {} = {}".format(number_1 , number_2 , number_1 / number_2))
elif what_is =="**":
    number_1 , number_2 = four()
    print("{} ^ {} = {}".format(number_1 , number_2 , number_1 ** number_2))
elif what_is == "sin":
    degree = float(input("Enter your degree: "))
    calc = math.sin(math.radians(degree))
    print("{:1.2f}".format(calc))
elif what_is == "cos":
    degree = float(input("Enter your degree: "))
    calc = math.cos(math.radians(degree))
    print("{:1.2f}".format(calc))
elif what_is =="degree":    
    degree = float(input("Enter your radians: "))
    print(math.radians(degree))
elif what_is == "log":
    x = float(input("Enter a number: "))
    base =float(input("Enter a base of logaritm (Emter means is defult): "))
    print(math.log(x ,base))
else:
    print("The word not true.")

print("=" *20)
print("Thank you. Bye")
