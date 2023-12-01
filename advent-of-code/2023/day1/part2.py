NUMS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open("./input.txt", 'r') as f:
    lines = f.readlines()

    total_sum = 0
    for line in lines:

        first_max_index = float("inf")
        last_max_index = float("-inf")
        first_max = None
        last_max = None

        for i in NUMS.keys():
            firsts_index = line.find(i)

            if 0 <= firsts_index <= first_max_index:
                first_max_index = firsts_index
                first_max = i

        if first_max:
            lline = line[:first_max_index] + str(NUMS[first_max]) + line[first_max_index:]
        else:
            lline = line

        for i in NUMS.keys():
            lasts_index = lline.rfind(i)

            if lasts_index >= last_max_index and lasts_index >= 0:
                last_max_index = lasts_index
                last_max = i

        if last_max:
            lline = lline[:last_max_index] + str(NUMS[last_max]) + lline[last_max_index:]

        num = ''
        first_num = None
        second_num = None

        for letter in lline:
            if letter.isdigit():
                if first_num is None:
                    first_num = letter
                second_num = letter

        total_sum += int(first_num + second_num)

print(total_sum)
