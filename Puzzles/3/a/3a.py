import re

input_file = open("input.txt", "r")
lines = input_file.readlines()

claims = []

for line in lines:
    match = re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)

    claim_id = match.group(1)
    left = int(match.group(2))
    top = int(match.group(3))
    width = int(match.group(4))
    height = int(match.group(5))

    right = left + width - 1
    bottom = top + height - 1

    claim = {
        "id": claim_id,
        "left": left,
        "top": top,
        "width": width,
        "height": height,
        "right": right,
        "bottom": bottom
    }

    claims.append(claim)

max_right = max(claim["right"] for claim in claims)
max_bottom = max(claim["bottom"] for claim in claims)

points = [[0 for x in range(max_right + 1)] for y in range(max_bottom + 1)]

for claim in claims:
    left = claim["left"]
    top = claim["top"]
    width = claim["width"]
    height = claim["height"]

    for row in range(top, top + height):
        for column in range(left, left + width):
            points[row][column] = points[row][column] + 1

number_of_overlaps = 0

for row in range(0, max_bottom):
    for column in range(0, max_right):
        point = points[row][column]
        if (point > 1):
            number_of_overlaps = number_of_overlaps + 1

print(number_of_overlaps)
