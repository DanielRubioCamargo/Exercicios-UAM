import time
from random import randint

def find_value(list_:list,v:int,index:int) -> int:
    if list_[index] == v:
        return index
    elif index <= 0:
        return -1
    return find_value(list_,v,index-1)


def find_value_nonrecursive(list_:list,v:int):
    for i,c in enumerate(list_):
        if c == v:
            return i
        elif i == len(list_)-1:
            return -1

    
def generate_random_to_list(list_:list,amount:int):
    for i in range(amount):
        list_.append(randint(1,10))

def main():
    numbers = list()
    generate_random_to_list(numbers,5)
    print(numbers)

    s1 = time.time()
    print(find_value(numbers,7,len(numbers)-1))
    e1 = time.time()

    s2 = time.time()
    print(find_value_nonrecursive(numbers,2))
    e2 = time.time()

    print(e1-s1)
    print(e2-s2)

if __name__ == "__main__":
    main()
