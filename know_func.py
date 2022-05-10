
def add(a, b):
    return a + b

# this function no return, have 1 pararmeter
def sayhello(name):
    print(f"hello {name}.")

# this function no return, no pararmeter
def main(): 
    print("this is main function.")

if __name__ == '__main__':
    print("this program entry point.")
    
    main()

    sayhello("wei")
    sayhello("jimmy")

    sum = add(2, 6)
    print(f"2 + 6 = {sum}")
    
    sum = add(8, 9)
    print(f"8 + 9 = {sum}")