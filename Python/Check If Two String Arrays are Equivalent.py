class Solution(object):
    
    def arrayStringsAreEqual(self, word1, word2):
        
        n1 = len(word1)
        n2 = len(word2)
        string1 = ""
        string2 = ""
        
        for i in range(n1):
            string1 += word1[i] 
            
        for i in range(n2):
            string2 += word2[i] 
        
        if string1 == string2:
            return True
        else:
            return False