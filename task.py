def print_hexagon(rows, cols):
    for r in range(rows):
        if r % 2 == 0:
            print(" " * 3, end="")
        for c in range(cols):
            print("  __  ", end="")
        print()
        
        if r % 2 == 0:
            print(" " * 2, end="")
        for c in range(cols):
            print(" /  \\ ", end="")
        print()
        
        if r % 2 == 0:
            print(" " * 1, end="")
        for c in range(cols):
            print("/    \\", end="")
        print()
        
        if r % 2 == 0:
            print(" " * 1, end="")
        for c in range(cols):
            print("\\    /", end="")
        print()
        
        if r % 2 == 0:
            print(" " * 2, end="")
        for c in range(cols):
            print(" \\__/ ", end="")
        print()

print("inputs :- 4 7")
print_hexagon(4, 7)

print("\ninputs :- 3 5")
print_hexagon(3, 5)
