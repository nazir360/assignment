#takes input from the user
max=int(input("Enter the maximum value for find sum of primes:"))
sum=0
for num in range(2,max+1):
    i=2
    for i in range(2,num):
        if(int(num%i==0)):
            i=num
            break;
        #when the number is prime calculate sum
    if i is not num:
        sum+=num
print("Sum of all prime numbers 1 to ",max,":",sum)