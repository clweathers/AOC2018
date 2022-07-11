from operator import itemgetter

def timestamp_string_from_line(line):
    timestamp_string = line[1:17]
    return timestamp_string

def guard_number_from_line(line):
    guard_number = None

    if ("Guard" in line):
        line = line[26:]
        line = line.replace(" begins shift", "")
        guard_number = int(line)

    return guard_number

def line_without_newlines(line):
    line = line.replace("\n", "")
    return line

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    timestamps = []

    for line in lines:
        line = line_without_newlines(line)
        
        timestamp_string = timestamp_string_from_line(line)
        guard_number = guard_number_from_line(line)

        timestamp = {
            "guard_number": guard_number,
            "line": line,
            "timestamp_string": timestamp_string
        }

        timestamps.append(timestamp)
        
    timestamps = sorted(timestamps, key=itemgetter('timestamp_string'))

    for timestamp in timestamps:
        print(timestamp)
