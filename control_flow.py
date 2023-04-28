# Write a function that uses while, if and continue statements to print all 
# the even numbers between 0 and 50. 
def while_loop():
    x=0
    while x<50:
        x+=1
        if x%2==0:
            continue
        print(x)


# # # Write a function that takes an integer argument and prints "Prime" if the 
# # # number is prime, and "Not prime" if the number is not prime.
def prime_numbers(numbers):
    if  numbers<=1:
       print ("Not prime")
       return
    for i in range(2,int(numbers **0.5)+1):
        if numbers%i==0:
            print("Not prime")
            return 
        print(f"{i}is Prime")
        
# # # Write a function that takes a list of integers as input and prints the sum of 
# # # all the even numbers in the list.
def even_integers(ints):
    sum=0
    for num in ints:
        if num%2==0:
           sum+=num
    print(sum)

# # # Write a function that takes any two integers as input, and prints the sum of all
# # #  the numbers between the two integers (inclusive) that are divisible by 3.
def takes_digits(num1,num2):
    sum=0
    for num in range(num1,num2+1):
        if num%3==0:
            sum+=num
    print(sum)
