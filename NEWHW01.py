while True:
    input_str = input("Please enter two words: ")
    
    if not input_str:
        print("-- bye !!")
        break
    
    words = input_str.split()
    
    if len(words) == 1:
        word1 = word2 = words[0]
    elif len(words) == 2:
        word1, word2 = words
    else:
        print("Invalid input. Please enter one or two words.")
        continue
    
    if word1 < word2:
        print(f"{word1} comes first")
    else:
        print(f"{word2} comes first")
