with open("./input.txt", 'r') as f:
    lines = f.readlines()

    total_sum = 0
    for line in lines:
        num = ''
        first_num = None
        second_num = None
        for letter in line:
            if letter.isdigit():
                if first_num is None:
                    first_num = letter
                second_num = letter

        total_sum += int(first_num + second_num)

print(total_sum)
