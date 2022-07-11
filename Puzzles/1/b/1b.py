import itertools

input_file = open("input.txt", "r")
lines = input_file.readlines()
frequency_changes = map(int, lines)

frequency = 0
frequencies_reached = []

for frequency_change in itertools.cycle(frequency_changes):
    frequency = frequency + frequency_change

    has_previously_reached_frequency = frequency in frequencies_reached

    if (has_previously_reached_frequency):
        print(frequency)
        break
    else:
        frequencies_reached.append(frequency)
