def divisible_count(x,y,k):
    num_range = x - y
    print(num_range)
    result = num_range // k * (-1)
    return result

print(divisible_count(10,20,2))