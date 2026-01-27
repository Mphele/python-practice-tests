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
    # print(count_negative_numbers(self = '', numbers=[]))

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
    
    # print(average(self='',numbers=[3,4]))
        
        

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
        
    
    # print(count_consonants(self='',text ='hzelhlo'))

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
    
    # print(second_largest(self='', numbers=[2,1,5,6,4]))

    def chunk_list(self, numbers, size):
        """Split list into chunks of given size."""
        numberlist  = []
        for num in range(0,len(numbers)-1,size):
            number = numbers[num : num + size ]
            numberlist.append(number)
        if len(numbers) %2 != 0:
                
                numbers = numbers[::-1]
                numberlist.append([numbers[0]])
        return numberlist
    print(chunk_list(self='', numbers=[1,2,3,4,5],size=2))

    def is_anagram(self, s1, s2):
        """Return True if the two strings are anagrams (ignore case & spaces)."""
        
        s1 = s1.replace(' ','')
        s2 = s2.replace(' ','')
        
        s1 = sorted(s1)
        s2 = sorted(s2)
        
        if s1 == s2 :return True
       


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
        rotate =[[],[]]
        
        rotate[0].append(matrix[1][0])
        rotate[0].append(matrix[0][0])
        rotate[1].append(matrix[1][1])
        rotate[1].append(matrix[0][1])
        return rotate
    # print(rotate_matrix_90(self='',matrix=[[1,2],[3,4]]))
    def validate_palindrome_number(self, n):
        """Return True if integer n is a palindrome."""
        # n = str(n)
        # print(n)
        # print(''.join(reversed(n)))
        # if n == ''.join(reversed(n)):
        #     return True
        # else:
        #     return False
        
        # n = [i for i in str(n) if str(n).isdigit()]
        
        # if n == n[::-1]:
        #     return True
        # else:
        #     return False
        
        return True if str(n) == ''.join(reversed(str(n))) else False
    print(validate_palindrome_number(self='',n=121))
    def generate_pascal_row(self, n):
        """Return the nth row of Pascal's Triangle (0-indexed)."""
        
        '''
        0           1
        1          1  1
        2         1  2  1
        3       1   3  3  1
        4      1   4  6  4  1
        
        '''
        
        pascal = []
        for i in range(n+1):
            if n == 0:
                pascal.append(1)
            else:
                
                pass
