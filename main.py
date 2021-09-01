
for b in range(1, 101):
    for c in range(1, 101):
        for t in range(1, 100):
            if (10 * b + 5 * c + 0.5 * t == 100) and (b + c + t == 100):
                print(b, c, t)