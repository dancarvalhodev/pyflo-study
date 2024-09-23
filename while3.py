pyramid_size = int(input("Give me a Pyramid size: "))
i = 1
while i <= pyramid_size:
    spacing = pyramid_size - i
    print(" " * spacing + "#" * (i*2))
    i += 1