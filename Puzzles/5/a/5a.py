def string_by_removing_last_character(string):
    string_by_removing_last_character = string[:-1]
    return string_by_removing_last_character

def characters_are_the_same_letter_with_different_cases(first_character, second_character):
    characters_are_exactly_the_same = (first_character == second_character)
    if (characters_are_exactly_the_same):
        return False
    
    characters_are_the_same_if_both_are_uppercased = (first_character.upper() == second_character.upper())
    if (characters_are_the_same_if_both_are_uppercased):
        return True

    return False

def string_by_removing_matches(string):
    string_length = len(string)
    index_of_second_to_last_character = string_length - 2
    index = index_of_second_to_last_character

    while (index >= 0):
        character = string[index]

        index_of_character_to_the_right = index + 1
        character_to_the_right = string[index_of_character_to_the_right]

        characters_match = characters_are_the_same_letter_with_different_cases(character, character_to_the_right)
        if (characters_match):
            string = string[:index] + string[index_of_character_to_the_right + 1:]
        
        index = index - 1

    return string

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    string = input_file.read()
    string = string_by_removing_last_character(string)  # The last character is a newline, which we don't want.

    print("Starting string: ", string)

    while (1):
        string_without_matches = string_by_removing_matches(string)

        removed_all_matches = (string == string_without_matches)
        if (removed_all_matches):
            break
        
        string = string_without_matches
    
    print("Final string: ", string)

    string_length = len(string)
    print("Final string length: ", string_length)
