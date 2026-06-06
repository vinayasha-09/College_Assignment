# Reverse Star Pattern
rows = 5

for i in range(rows, 0, -1): #range(start, stop, step)
    for j in range(1, i + 1):     #start = rows → begins at 5
        #stop = 0 → stops just before 0 (so it goes down to 1)
                 #step = -1 → decreases by 1 each time
                 
        print("*", end="")
    print()

