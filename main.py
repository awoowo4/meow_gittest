def calculate_average(numbers):
    return sum(numbers)/len(numbers)

if __name__ == '__main__':
    numbers = [1,2,3,4,5]
    print('Среднее значение: ', calculate_average(numbers))