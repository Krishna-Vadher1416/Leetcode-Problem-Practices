class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 :
            return False
        vowels = ["a","e","i","o","u"]
        vow = False
        con = False

        

        for i in word :
            if not i.isalnum():
                return False
            
            if i.lower() in vowels :
                vow= True 
            elif not i.isdecimal() :
                con = True
        return vow and con


            
