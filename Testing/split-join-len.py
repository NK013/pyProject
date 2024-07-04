user_numbers =  "13,70,35,60,32,76,93,55"
numbers_list = user_numbers.split(",")

print(" - ".join(numbers_list))
print(f"There are {len(numbers_list)} numbers in the list.")

for index in range(len(numbers_list)):
    print(f"{index + 1}. Number is {numbers_list[index]}")