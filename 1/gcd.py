def decorator_timer(some_function):
    '''
    Decorator to measure and print the execution time of a function.
    '''
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = some_function(*args, **kwargs)
        end = time() - t1
        print(f"Execution Time: for {some_function.__name__} is {end:.6f} seconds")
        return result  

    return wrapper


class NumberConverter:

    '''Handles conversion between words and digits using Singleton Pattern'''
    
    _instance = None  
 
    def __new__(cls):
        '''Ensure that only one instance is created'''
        if cls._instance is None:
            cls._instance = super(NumberConverter, cls).__new__(cls)
            # Creating dictionary in singleton to avoids creating it again by don't allowing to create another instance
            cls._instance.DICT_WORD = {
                'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'
            }
            cls._instance.DICT_DIGIT = {
                '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'
            }
        return cls._instance  
    

    def word_to_digit_recursive(self: object, ans_str: str, current_word = '', index = 0) -> str:

        '''Converts a word-based number into its digit representation'''

        if index == len(ans_str):
            if current_word in self.DICT_WORD:
                return self.DICT_WORD[current_word]
            elif current_word == '':
                return ''
            else:
                raise ValueError(f"Invalid word segment {current_word} in {ans_str}")

        current_word += ans_str[index]

        if current_word in self.DICT_WORD:
            return self.DICT_WORD[current_word] + self.word_to_digit_recursive(ans_str, '', index + 1)

        return self.word_to_digit_recursive(ans_str, current_word, index + 1)

    def digit_to_word_recursive(self: object, ans_in_word: str, current_digit = '', index = 0) -> str:

        '''Converts a digit-based number into its word representation'''

        if index == len(ans_in_word):
            if current_digit in self.DICT_DIGIT:
                return self.DICT_DIGIT[current_digit]
            else:
                return ''

        current_digit += ans_in_word[index]

        if current_digit in self.DICT_DIGIT:
            return self.DICT_DIGIT[current_digit] + self.digit_to_word_recursive(ans_in_word, '', index + 1)
    
    
class GCDCalculator:

    '''Handles GCD calculation which has static method to calculate GCD'''

    @staticmethod
    def compute_gcd(max_digit: int, min_digit: int) -> int:

        '''Computes the Greatest Common Divisor (GCD) using Euclid's Algorithm (Recursion)'''

        if min_digit == 0:
            return str(max_digit)  # return strings because digit_to_word_recursive takes strings as input
        return GCDCalculator.compute_gcd(min_digit, max_digit % min_digit)


class NumberProcessing:

    ''' This function will handle all internal processing, to simplifies instance creation'''

    def __init__(self):
        self.converter = NumberConverter()
        self.gcd_calculator = GCDCalculator()

    @decorator_timer
    def process_gcd(self: object, word_num1: str, word_num2: str) -> str:
        
        '''Handles full conversion process and computes GCD. User will always call this function.'''
        
        digit_a = self.converter.word_to_digit_recursive(word_num1)
        digit_b = self.converter.word_to_digit_recursive(word_num2)
            
        gcd_result = self.gcd_calculator.compute_gcd(int(digit_a), int(digit_b)) if int(digit_a) > int(digit_b) else self.gcd_calculator.compute_gcd(int(digit_b), int(digit_a))
 
        return self.converter.digit_to_word_recursive(gcd_result)


if __name__ == "__main__":

    NumberProcessor = NumberProcessing()

    a = input("Enter first number in words: ").lower()
    b = input("Enter second number in words: ").lower()
    
    try:
        print("GCD in words:", NumberProcessor.process_gcd(a, b))
    except ValueError as e:
        print(f'Error: {e}')