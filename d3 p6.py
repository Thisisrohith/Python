def reverse(s):
    str = ""
    for i  in s:
        sttr = i + str
        return str

s =input("Enter the number")

print("the original string is : ", end="")
print(s)

print("the reversed string(usinng loops) is : ", end="")
print(reverse(s))
