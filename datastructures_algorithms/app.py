import re
from generate_numbers import sorted_numbers

print(sorted_numbers)


def find_target(target):
    for i in range(len(sorted_numbers)):
        if sorted_numbers[i] == target:
            return i, target


def main():
    while True:
        user_input = input("Enter a number to find: ")
        pattern = r"^[0-9]+$"
        is_number = re.match(pattern, user_input)
        if is_number:
            break

    result = find_target(int(user_input))

    if result:
        print(result)
    else:
        print("Not found!")


if __name__ == "__main__":
    main()
