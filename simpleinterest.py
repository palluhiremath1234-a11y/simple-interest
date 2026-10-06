def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


if __name__ == "__main__":
    principal = 1000
    rate = 2
    time = 2

    print("Simple interest is:", simple_interest(principal, rate, time))