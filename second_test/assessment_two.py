class AssessmentTwo:

    # ===== BASIC =====

    def count_negative_numbers(self, numbers):
        """Return the number of negative values in the list."""
        if len(numbers)==0:
            return 0
        else:
            count = 0
            for num in numbers:
                if num < 0:
                    count +=1
                    
            return count
                


    def average(self, numbers):
        """Return the average of numbers or None if list is empty."""
        
        if not numbers:
            return None
        else:
            return sum(numbers)/len(numbers)
        

        
        

    def first_and_last(self, items):
        """Return a tuple of (first, last) item or None if list is empty."""
        if items is None:
            return []
        else:
            return (items[0],items[-1])
  
                
    def count_consonants(self, text):
        """Return the number of consonants in the string (letters only)."""
 
        return sum(1 for i in text if i.lower() in 'bcdfghjklmnpqrstvwxyz' )
    

    def is_even_length(self, text):
        """Return True if the string length is even."""
        return True if len(text)%2 == 0 else False

    # ===== INTERMEDIATE =====

    def remove_duplicates_preserve_order(self, numbers):
        """Remove duplicates while preserving order."""

        return set(numbers)
    def word_lengths(self, sentence):
        """Return a dictionary mapping each word to its length."""
   
         

    def second_largest(self, numbers):
        """Return the second largest number or None if it doesn't exist."""
      
    

    def chunk_list(self, numbers, size):
        """Split list into chunks of given size."""
        num = []
        
        if numbers is None:
            return []
        else:
            for number in range(0,len(numbers),size):
                num.append(numbers[number:number+size])
                
            return num
    print(chunk_list(self=None,numbers=[1,2,3,4,5,6],size=3))
    def is_anagram(self, s1, s2):
        """Return True if the two strings are anagrams (ignore case & spaces)."""
        
    
       


    # ===== ADVANCED =====

    def running_sum(self, numbers):
        """Return a list of running sums."""
        
        
        
    def longest_unique_substring(self, text):
        """Return the length of the longest substring without repeating characters."""
        
        return sum(1 for char in 'abcdefghijklimopqrstuvwxyz' if char in text.lower())
        

    def rotate_matrix_90(self, matrix):
        """Rotate a square matrix 90 degrees clockwise."""
        

    def validate_palindrome_number(self, n):
        """Return True if integer n is a palindrome."""
      
    def generate_pascal_row(self, n):
        """Return the nth row of Pascal's Triangle (0-indexed)."""
        
        '''
        0           1
        1          1  1
        2         1  2  1
        3       1   3  3  1
        4      1   4  6  4  1
        5     1  5  10 10  5  1
        
        '''
        
    
