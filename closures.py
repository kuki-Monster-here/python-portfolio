def multiplier(factor):
    def inner(number):
        return number * factor
    return inner

double = multiplier(2)
print(double(5))  # 10
