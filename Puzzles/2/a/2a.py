input_file = open("input.txt", "r")
lines = input_file.readlines()

number_of_twos = 0
number_of_threes = 0

for line in lines:
    unique_characters = "".join(set(line))

    has_twos = False
    has_threes = False

    for character in unique_characters:
        count = line.count(character)

        if count == 2:
            has_twos = True
        elif count == 3:
            has_threes = True
    
    if (has_twos):
        number_of_twos = number_of_twos + 1

    if (has_threes):
        number_of_threes = number_of_threes + 1

checksum = number_of_twos * number_of_threes
print(checksum)
