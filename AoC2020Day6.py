# Part 1
# 1. divide each groups
# 2. join, uniq, count the group
# 3. sum them up

# Part 2
# 1. divide each groups
# 2. do intersection on every answers and find resulting count
# 3. sum them up

def part_one(text):
    groups = text.split("\n\n")
    
    count = 0
    for group in groups:
        answers = group.split("\n")
        count += len(set("".join(answers)))
    return count

def part_two(text):
    groups = text.split("\n\n")
    
    count = 0
    for group in groups:
        answers = group.split("\n")
        common = set(answers[0])
        for answer in answers[1:]:
            common = common.intersection(set(answer))
        count += len(common)
    return count

import requests
response = requests.get("https://raw.githubusercontent.com/bsmmoon/algo/main/AoC2020Day6.input")
print(part_one(response.text.strip()))
print(part_two(response.text.strip()))
