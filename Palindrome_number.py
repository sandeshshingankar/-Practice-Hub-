n=int(input("Enter a Number: "))
reverse = 0
while n>0:
    digit= n%10
    reverse = reverse * 10 + digit
    n = n//10
print("Reversed number is:", reverse)

#another logic for same
print(int(str(num[::-1])))
