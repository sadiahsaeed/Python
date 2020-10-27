number=input("Please enter a Word: ")
number=str(number)
rvs=number[::-1]
print(rvs)
if number == rvs:
    print(" This word is a palindrome ")
else:
    print(" This word is not a palindrome ")
input()
