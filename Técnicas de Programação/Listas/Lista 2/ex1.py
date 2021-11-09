import time

def sum_all(n:int) -> int:
    if n == 1:
        return 1
    return n + sum_all(n-1)

def sum_all_nonrecursive(n:int) -> int:
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

def main():
    s1 = time.time()
    print(sum_all(900))
    e1 = time.time()

    s2 = time.time()
    print(sum_all_nonrecursive(900))
    e2 = time.time()

    print(e1-s1)
    print(e2-s2)

if __name__ == "__main__":
    main()