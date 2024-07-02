
#fullname = input("Please enter fullname (with space between name and surname) : ")

#fullname_split = fullname.split(" ")

#name = fullname_split[0]
#surname = fullname_split[1]

#print("Name: " + name)
#print("Surname: " + surname)



nums = [1, 2, 3, 4, 5]

stringNums = []

for number in nums:
    stringNums.append(str(number))

print(' | '.join(stringNums))