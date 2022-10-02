#define a function is_odd_or_even
#with an argument n
def is_odd_or_even(n):
    #find the modulus of n
    if n%2!=0:
        #if the n is an odd number, the modulus will not be 0
        print(n,"is an odd number")
    else:
        #if n is an even number, the modulus will always be a 0
        print(n, "is an even number")
#entry point of the program
#enclose asking for input from the user in a try except block to handle the
#string input scenarios
#the program 
try:
    #Ask for input
    n = int(input("Enter a number please?"))#mind about type casting from a string to an integer
    #call our method to check if the number is odd or even
    is_odd_or_even(n)
except:
    print("Please you entered an invalid number, try again")



