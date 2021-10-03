def classify(number):
    if number < 1:
        raise ValueError('ValueError')
    aliquot_sum = sum(i if number % i == 0 else 0 for i in range(1, number))
    return 'perfect' if aliquot_sum == number else 'deficient' if aliquot_sum < number else 'abundant'
