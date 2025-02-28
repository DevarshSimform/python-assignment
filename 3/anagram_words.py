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


class Grouping_Anagrams:

    '''This class groups the anagram words'''

    def __init__(self):

        self.hash_dict = {}

    @decorator_timer
    def group_anagram(self: object, strs: str) -> list:

        '''It will return list of (grouped list of anagram words)'''

        for current_str in strs:

            #creating 26 sized list initialised with all zero
            count_letter = [0]*26

            for letter in current_str:
                # Incrementing value on respective index of list.
                count_letter[ord(letter) - ord('a')] += 1

            # once list is created for specific word convert it to tuple and set it as key of hash_dict.
            count_letter_tuple = tuple(count_letter)
            
            if count_letter_tuple in self.hash_dict:
                #Appending anagram word to hash_dict if key matches.
                self.hash_dict[count_letter_tuple].append(current_str)
            else:
                #Set first word if new key (word) comes.
                self.hash_dict[count_letter_tuple] = [current_str]

        return list(self.hash_dict.values())
    
if __name__ == "__main__":

    userInstance = Grouping_Anagrams()

    try:
        input_list = list(input("Enter space seperated words: ").split(' '))
        print(userInstance.group_anagram(input_list))
    except ValueError as e:
        print(f'Error: {e}')