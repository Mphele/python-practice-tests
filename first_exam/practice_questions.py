class PracticeExam:

    # ===== BASIC QUESTIONS =====

    def count_odd_numbers(self, numbers):
        """Return the count of odd numbers in the list."""
        if len(numbers) ==0:
            return 0
        return sum(1 for i in numbers if i%2 != 0)

    def sum_list(self, numbers):
        """Return the sum of all numbers in the list."""
        return sum(numbers) 

    def reverse_words_order(self, sentence):
        """Reverse the order of words in a sentence."""
        return ' '.join(reversed(sentence.split()))

    def contains_vowel(self, text):
        """Return True if the string contains at least one vowel."""
        
        return True if sum(1 for char in 'aeiou' if char in text.lower())>0 else False

    def smallest_number(self, numbers):
        """Return the smallest number in the list or None if empty."""
        return min(numbers) if numbers else None  

    # ===== INTERMEDIATE QUESTIONS =====

    def remove_vowels(self, text):
        """Return the string with all vowels removed (case-insensitive)."""
        vowels ='aeiouAEIOU'
        for i in text:
            if i in vowels:
                text = text.replace(i,'')
        return text
    
    print(remove_vowels(self='',text= 'hellow'))
        

    def count_character_frequency(self, text):
        """Return a dictionary with character frequencies."""
        freq = {}
        
        # for char in text:
        #     if char in freq:
        #         freq[char] += 1
                
        #     else:
        #         freq[char] = 1
        # return freq
        for char in text:
            freq[char] = freq.get(char,0)+1
        return freq

    

    def is_prime(self, n):
        """Return True if n is a prime number, otherwise False."""
        if n < 2:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2,n-1):
                if n % i == 0:
                    return False
                
            return True
                
                
    print(is_prime(self='',n =13))
                

    def flatten_list(self, nested):
        """Flatten a 2D list into a 1D list."""
        
        unnest = []
        
        for i in nested:
            for j in i:
                unnest.append(j)
        return unnest

    def longest_common_prefix(self, words):
        """Return the longest common prefix among a list of words."""
        for word in words:
            pass


    # ===== ADVANCED QUESTIONS =====

    def fibonacci_sequence(self, n):
        """Return a list containing the first n Fibonacci numbers."""
        pass

    def max_subarray_sum(self, numbers):
        """Return the maximum sum of a contiguous subarray."""
        pass

    def valid_parentheses(self, s):
        """Return True if parentheses are valid."""
        pass

    def rotate_left(self, numbers, k):
        """Rotate the list to the left by k positions."""
        pass

    def spiral_matrix(self, n):
        """Return an n x n spiral matrix."""
        pass
