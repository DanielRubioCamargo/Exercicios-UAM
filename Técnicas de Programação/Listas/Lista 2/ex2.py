import time

def multiply(n1:int,n2:int) -> int:
    if n1 == 1:
        return n2
    return n2 + multiply(n1-1,n2)

def multiply2(n1:int,n2:int) -> int:
    result = 0
    for i in range(n1):
        result += n2
    return result

def main():
    s1 = time.time()
    print(multiply(10,10))
    e1 = time.time()

    s2 = time.time()
    print(multiply2(9,9))
    e2 = time.time()

    print(e1-s1)
    print(e2-s2)
    
if __name__ == "__main__":
    main()