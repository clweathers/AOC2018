import string as string_import

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
    return_string = string

    string_length = len(return_string)
    index_of_second_to_last_character = string_length - 2
    index = index_of_second_to_last_character

    while (index >= 0):
        character = return_string[index]

        index_of_character_to_the_right = index + 1

        if (index_of_character_to_the_right >= len(return_string)):
            index = index - 1
            continue
        
        character_to_the_right = return_string[index_of_character_to_the_right]

        characters_match = characters_are_the_same_letter_with_different_cases(character, character_to_the_right)
        if (characters_match):
            return_string = return_string[:index] + return_string[index_of_character_to_the_right + 1:]
        
        index = index - 1

    return return_string

def string_by_repeatedly_removing_matches_until_none_are_left(string):
    return_string = string

    while (1):
        string_without_matches = string_by_removing_matches(return_string)

        removed_all_matches = (return_string == string_without_matches)
        if (removed_all_matches):
            break
        
        return_string = string_without_matches
    
    return return_string

def string_by_removing_all_casings_of_letter(string, letter):
    return_string = string
    return_string = return_string.replace(letter.upper(), "")
    return_string = return_string.replace(letter.lower(), "")
    return return_string

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    string = input_file.read()
    string = string_by_removing_last_character(string)  # The last character is a newline, which we don't want.
    
    best_result = len(string)

    all_letters = set(string_import.ascii_lowercase)
    for letter in all_letters:
        string_without_letters = string_by_removing_all_casings_of_letter(string, letter)
        string_without_matches = string_by_repeatedly_removing_matches_until_none_are_left(string_without_letters)
        string_length = len(string_without_matches)
        best_result = min(string_length, best_result)
        
    print(best_result)
