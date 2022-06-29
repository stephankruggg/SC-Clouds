class Fibonacci:
    def __init__(self):
        self.__first_number = 0
        self.__second_number = 1
        self.__previous_number = self.__first_number
    
    def recursive(self, position: int):
        if (position == 0):
            return self.__first_number
        elif (position == 1):
            return self.__second_number
        else:
            return (self.recursive(position - 1) + self.recursive(position - 2))

    def linear(self, position: int):
        result = self.__first_number + self.__second_number
        for _ in range (1, position):
            tmp = result
            result += self.__previous_number
            self.__previous_number = tmp
        
        return result
