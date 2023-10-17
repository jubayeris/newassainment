while True:
    input_string = input("Please enter a string (type 'done' to exit): ")

    if input_string.lower() == 'done':
        print("Bye!")
        break

    processed_string = ''
    for char in input_string:
        if char not in ',.!:?':
            processed_string += char

    processed_string = processed_string.upper()
    print(processed_string)
