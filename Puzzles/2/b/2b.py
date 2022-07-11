input_file = open("input.txt", "r")
lines = input_file.readlines()

qualifying_words = []

for index, line in enumerate(lines):
    for next_index, next_line in enumerate(lines, index):
        different_characters = []

        for character_index, character in enumerate(line):
            compare_character = next_line[character_index]
            if character != compare_character:
                different_characters.append(character)
        
        if len(different_characters) == 1:
            result = line.replace(different_characters[0], "")
            print(line)
            print(result)