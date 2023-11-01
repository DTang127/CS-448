
def is_prime(number):
    possible_factor = 2 #possible factors for number

    # while the problem is not yet solved
    while True: 
        if (number%possible_factor == 0) and number/possible_factor >= 2: #test: if (number) / (possible factor) is an integer >= 2
            return 'not prime' #then return not prime
        else:
            possible_factor += 1 #possible factors for number
            if possible_factor == number: #if possible factors equals number
                return 'prime' #then return number is prime


for i in range(3,101):
    print(i, ': ', is_prime(i))
