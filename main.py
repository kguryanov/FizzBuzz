from fizzbuzz import fizzbuzz, draw

if __name__ == '__main__':
    print(*draw(fizzbuzz(50), 10), sep="\n")