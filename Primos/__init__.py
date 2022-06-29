from Primos import Primos

STOP_CONDITION = 'sair'
MINIMUM_SEQUENCE_NUMBER = 1

print(f'Para terminar o programa, digite {STOP_CONDITION}')
while (True):
    maximum_sequence_number = input()
    try:
        maximum_sequence_number = int(maximum_sequence_number)
        if (maximum_sequence_number <= MINIMUM_SEQUENCE_NUMBER):
            print(f'Forneça um valor maior que {MINIMUM_SEQUENCE_NUMBER}')
        else:
            PrimeSequence = Primos()
            recursive_result = PrimeSequence.recursive(maximum_sequence_number)
            print(f'O resultado recursivo é: {recursive_result}')

            linear_result = PrimeSequence.linear(maximum_sequence_number)
            print(f'O resultado linear é: {linear_result}')
    except (ValueError) as error:
        if (maximum_sequence_number.lower() == STOP_CONDITION):
            break

        print('Forneça um número inteiro')
