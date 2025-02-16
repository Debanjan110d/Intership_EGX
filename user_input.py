user_input = input("Enter numbers separated by space: ")
input_list = list(map(int, user_input.split()))

input_list.sort()

print("Sorted list:", input_list)

