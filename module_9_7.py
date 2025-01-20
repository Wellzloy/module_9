def is_prime(func):
    def wrapper(*args):
        num = func(*args)

        if num > 1:
            for i in range(2, int(num * 0.5) + 1):
                if num % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        return num

    return wrapper


@is_prime
def sum_three(one, two, three):
    return one + two + three


result = sum_three(2, 3, 6)
print(result)
