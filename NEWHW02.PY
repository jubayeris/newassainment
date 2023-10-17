input_string = input("Enter string: ")
print("Input string = ", input_string)

index = len(input_string) - 1
while index >= 0:
    print(input_string[index])
    index -= 1
