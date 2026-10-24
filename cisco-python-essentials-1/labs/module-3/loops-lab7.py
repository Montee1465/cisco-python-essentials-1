c0 = int(input("non-negative, non-zero integer numbers :"))
steps = 0

while True:
    if c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
            # Increase the steps counter.
            steps += 1
            print (c0)
    
        else:
            c0 = 3 * c0 + 1
            # Increase the steps counter.
            steps += 1
            print(c0)
        continue
    
    else:
            print("Steps: ",steps)
            break
