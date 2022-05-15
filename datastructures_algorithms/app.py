import re

from generate_numbers import sorted_numbers

print(sorted_numbers)


def find_target(target):
    first_index = 0
    last_index = len(sorted_numbers) - 1
    count = 0
    while first_index <= last_index:
        count += 1
        mid = (first_index + last_index) // 2
        if sorted_numbers[mid] == target:
            return f"index: {mid}, target: {target}, count: {count}"
        elif sorted_numbers[mid] < target:
            first_index = mid + 1
        else:
            last_index = mid - 1


def get_number():
    while True:
        user_input = input("Enter a number to find: ")
        pattern = r"^[0-9]+$"
        is_number = re.match(pattern, user_input)
        if is_number:
            return int(user_input)


def main():
    num = get_number()
    result = find_target(num)

    if result:
        print(result)
    else:
        print("Not found!")


if __name__ == "__main__":
    main()
