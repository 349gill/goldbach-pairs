'''
A pair of primes, (p, q), is called a Goldbach pair of primes associated with an even positive integer, 2n, if 2n = p + q.
The Goldbach conjecture asserts that with every even integer greater than 4 there is associated at least one Goldbach pair of primes.
'''


def is_prime(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False
    return True


def find_pair(num):
    if num % 2 != 0:
        return 0, 0
    for i in range(2, num):
        other_num = num-i
        if is_prime(i) and is_prime(other_num):
            return i, other_num


def main():
    num = int(input("Enter an even number\n"))
    print(
        f"The associated pair of primes for the given number is {find_pair(num)}")


if __name__ == "__main__":
    main()
