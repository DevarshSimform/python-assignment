def decorator_timer(some_function):
    '''Decorator to measure and print the execution time of a function.'''
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = some_function(*args, **kwargs)
        end = time() - t1
        print(f"Execution Time: for {some_function.__name__} is {end:.6f} seconds")
        return result  

    return wrapper


class GenerateParenthesis:

    '''Class to generate all combinations of valid parentheses for a given number of pairs.'''

    def __init__(self):
        pass

    @decorator_timer
    def generate_valid_parenthesis(self, number):
        
        # To validate user input and Raise Error
        if number < 1 or number > 8:
            raise ValueError(f'Invalid Input')
        
        def recursive_generator(current_str = '', open_bkt = 0, close_bkt = 0, valid_outputs = []):
            
            # Append the valid string to list valid_outputs
            if len(current_str) == 2*number :
                valid_outputs.append(current_str)
                return 
            
            # Add open bracket and stops when open bracket is equal to number
            if open_bkt < number:
                recursive_generator(current_str+'(', open_bkt+1, close_bkt, valid_outputs)

            # Add close bracket and stops when close bracket is equal to open bracket
            if close_bkt < open_bkt:
                recursive_generator(current_str+')', open_bkt, close_bkt+1, valid_outputs)
            
            return valid_outputs
        
        return recursive_generator()


if __name__ == "__main__":

    userInstance = GenerateParenthesis()

    try:
        n = int(input("Enter Number in range of 1 to 8: "))
        print(userInstance.generate_valid_parenthesis(n))
    except ValueError as e:
        print(f'Error: {e}')