class AssessmentTwo:

    # ===== BASIC =====

    def count_negative_numbers(self, numbers):
        """Return the number of negative values in the list."""
        
        count = 0
        if numbers is None:
            return count 
        else:
            
            for num in numbers:
                if num < 0:
                    count+=1
            return count
    print(count_negative_numbers(self = '', numbers=[]))

    def average(self, numbers):
        """Return the average of numbers or None if list is empty."""
        
        
        if len(numbers) == 0:
            return None
        else:
            count = 0
            for i in numbers:
                count +=1
            avg = sum(numbers)/count
            
            return avg
    
    print(average(self='',numbers=[3,4]))
        
        

    def first_and_last(self, items):
        """Return a tuple of (first, last) item or None if list is empty."""
        first = None
        last = None
        
        if len(items) == 0:
            return None
        else:
            for index,item in enumerate(items):
                if index == 0:
                    first = item
                if index == len(items)-1:
                    last = item
                
            return (first,last)
                
    def count_consonants(self, text):
        """Return the number of consonants in the string (letters only)."""
        
        count = 0
        
        for i in text:
            if i.upper() in 'BCDFGHJKLMNPQRSTVWXYZ':
                count +=1
        return count
        
    
    print(count_consonants(self='',text ='hzelhlo'))

    def is_even_length(self, text):
        """Return True if the string length is even."""
        if len(text)%2 == 0:
            return True
        else:
            return False


    # ===== INTERMEDIATE =====

    def remove_duplicates_preserve_order(self, numbers):
        """Remove duplicates while preserving order."""
        numbers = set(numbers)
        numbers = [num for num in numbers]
        return numbers
            

    def word_lengths(self, sentence):
        """Return a dictionary mapping each word to its length."""
        sentence = sentence.split()
        
        dictionary = {}
        
        for element in sentence:
            dictionary[element] = len(element)
            
        return dictionary

    def second_largest(self, numbers):
        """Return the second largest number or None if it doesn't exist."""
        if len(numbers) <=1:
            return None
        else:
            numbers = sorted(numbers)
            numbers = numbers[::-1]
            
        return numbers[1]
    
    print(second_largest(self='', numbers=[2,1,5,6,4]))

    def chunk_list(self, numbers, size):
        """Split list into chunks of given size."""
        pass

    def is_anagram(self, s1, s2):
        """Return True if the two strings are anagrams (ignore case & spaces)."""
        pass


    # ===== ADVANCED =====

    def running_sum(self, numbers):
        """Return a list of running sums."""
        add = 0
        num = []
        if len(numbers) == 0:
            return []
        else:
            
            for i in numbers:
                add +=i
                num.append(add)
            return num
    def longest_unique_substring(self, text):
        """Return the length of the longest substring without repeating characters."""
        
        return sum(1 for char in 'abcdefghijklmnopqrstuvwxyz' if char in text.lower())
        

    def rotate_matrix_90(self, matrix):
        """Rotate a square matrix 90 degrees clockwise."""
        for i in matrix:
            for index,element in enumerate(i):
                pass

    def validate_palindrome_number(self, n):
        """Return True if integer n is a palindrome."""
        pass

    def generate_pascal_row(self, n):
        """Return the nth row of Pascal's Triangle (0-indexed)."""
        pass
