def print_ten_times(input_str, count=0):
    if count < 10:
        print(input_str)
        print_ten_times(input_str, count + 1)

user_input = input("Enter a string: ")
print_ten_times(user_input)

