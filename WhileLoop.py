class WhileLoop:

    @staticmethod
    def printEvenNumbers(number):
        while number < 53:
            if number % 2 == 0:
                print('Even number - {}'.format(number))
            else:
                print('Odd number - {}'.format(number))
            number += 1            

WhileLoop.printEvenNumbers(12)           