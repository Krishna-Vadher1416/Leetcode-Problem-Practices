class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
            
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        has_vow = False
        has_con = False

        for char in word:
            
            if not char.isalnum():
                return False
            
            
            if char.isalpha():
                if char in vowels:
                    has_vow = True
                else:
                    has_con = True
                    
        
        return has_vow and has_con