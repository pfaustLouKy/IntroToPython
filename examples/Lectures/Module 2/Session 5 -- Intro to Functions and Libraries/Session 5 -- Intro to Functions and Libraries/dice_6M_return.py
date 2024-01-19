"""Roll a six-sided die 6,000,000 times."""
import random
def dice(rolls):
    # face frequency counters
    frequency1 = 0
    frequency2 = 0
    frequency3 = 0
    frequency4 = 0
    frequency5 = 0
    frequency6 = 0
    results = []
    # 6,000,000 die rolls
    for roll in range(rolls):  # note underscore separators
        face = random.randrange(1, 7)
        # increment appropriate face counter
        if face == 1:
            frequency1 += 1
        elif face == 2:
            frequency2 += 1
        elif face == 3:
            frequency3 += 1
        elif face == 4:
            frequency4 += 1
        elif face == 5:
            frequency5 += 1
        elif face == 6:
            frequency6 += 1
    results.append(frequency1)
    results.append(frequency2)
    results.append(frequency3)
    results.append(frequency4)
    results.append(frequency5)
    results.append(frequency6)
    return results
    