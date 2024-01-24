# 1.
user_string = input('please enter a string: ')
print(user_string)

# 2.
first_char = user_string[0]
last_char = user_string[-1]

str_length = len(user_string)
mid_index = int(str_length/2)  # need to convert int because indices should always be integers
print(mid_index)
mid_char = user_string[mid_index]

new_str = first_char+mid_char+last_char
print(new_str)

