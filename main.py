from fizzbuzz import fizzbuzz

if __name__ == '__main__':
    for idx, value in fizzbuzz(50, modulos={0:"Dummy"}):
        print(f"{idx} : {value}")