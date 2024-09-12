width = input("Flag width:\n")
width = int(width)

height = input("Flag height:\n")
height = int(height)

half_width = int(width / 2)
half_height = int(height / 2)

print(("#" * int(half_width) + "-" * int(half_width) + '\n') * half_height, end='')
print(("-" * int(width) + '\n') * half_height)
