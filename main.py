from fizzbuzz import fizzbuzz, draw

if __name__ == '__main__':
    print(*draw(fizzbuzz(10), 5), sep="\n")