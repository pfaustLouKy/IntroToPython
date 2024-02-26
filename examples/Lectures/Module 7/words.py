word = input('Enter a 5-letter word.  I will create arbitrary 3-letter words from its letters:')
for first in range(5):
    for second in range(5):
        if second != first:
            for third in range(5):
                if third not in (second, first):
                    print(f'{word[first]}{word[second]}{word[third]}')