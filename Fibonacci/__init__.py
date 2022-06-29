from Fibonacci import Fibonacci

STOP_CONDITION = 'sair'
MINIMUM_NUMBER_POSSIBLE = 0

print(f'Para terminar o programa, digite {STOP_CONDITION}')
while (True):
    maximum_sequence_number = input()
    try:
        maximum_sequence_number = int(maximum_sequence_number)
        if (maximum_sequence_number < MINIMUM_NUMBER_POSSIBLE):
            print(f'Forneça um valor maior ou igual a {MINIMUM_NUMBER_POSSIBLE}')
        else:
            FibonacciSequence = Fibonacci()
            recursive_result = FibonacciSequence.recursive(maximum_sequence_number)
            print(f'O resultado recursivo é: {recursive_result}')

            linear_result = FibonacciSequence.linear(maximum_sequence_number)
            print(f'O resultado linear é: {linear_result}')
    except (ValueError) as error:
        if (maximum_sequence_number.lower() == STOP_CONDITION):
            break

        print('Forneça um número inteiro')
