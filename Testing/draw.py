
prints = 1
lines = input("Lines wanted (max: 50): ")

for _ in range(int(lines)):
    if prints > 0:
        s = "•" * prints
        print(s.center(100))
    prints += 2
