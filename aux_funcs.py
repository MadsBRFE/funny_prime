from math import sqrt

def get_primes(lower_bound ,upper_bound) -> [int]:
    prime_ls = []
    lower_bound = max(lower_bound ,2)
    for num in range(lower_bound ,upper_bound + 1):
        if num< 9:
            num_is_prime = num in [2 ,3 ,5 ,7]
        else:
            num_is_prime = True
            for i in range(2, int(sqrt(num) ) +1):
                if (num % i) == 0:
                    num_is_prime = False

                    break
        if num_is_prime:
            prime_ls.append(num)
    return prime_ls

def get_funniest_number_and_score(nr_list):
    funniest_number = 0
    funniest_number_score = 0
    for num in nr_list:
        funniness = get_funniness(num)
        if funniness >= funniest_number_score:
            funniest_number_score = funniness
            funniest_number = num
    return funniest_number ,funniest_number_score

def get_funniness(num):
    if num == 0:
        digits = [0]
    else:
        digits = []
        while num >0:
            digit = num % 10
            digits.append(digit)
            num = num // 10
    score = len(set(digits))
    return score


