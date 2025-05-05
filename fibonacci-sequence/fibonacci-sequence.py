def fibonacci_sequence():
    '''
    Prints Fibonacci sequence up to the number of terms entered by the user.
    '''

    a,b = 0,1
    try:
        n =int(input('Enter the number of terms: '))
        if n <= 0:
            print('Please enter a positive integer.')
            return
    except ValueError:
        print('Invalid input! Please add a valid integer.')
        return
    
    sequence = []
    for i in range(n):
        sequence.append(str(a)) 
        a,b = a+b,a
    print(', '.join(sequence))


fibonacci_sequence()