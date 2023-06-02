from fizzbuzz import fizzbuzz

if __name__ == '__main__':
    for idx, value in enumerate(fizzbuzz(50), start=1):
        print(f"{idx} : {value}")