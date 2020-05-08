class Solution(object):
    head={}
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        ans = ''
        for word in words:
            self.add(word)
        
         
        
        for word in words:
            if self.search(word):
                if len(word)>len(ans) or (len(word)==len(ans) and word<ans):
                    ans=word
                    
            
        return ans
                
           
                
    
    def add(self,word):
        cur = self.head
        for let in word:
            if let not in cur:
                cur[let]={}
            cur=cur[let]
        cur['*']=True #marks end of word
    
    def search(self,word):
        cur = self.head
        for let in word:
            if let not in cur:
                return False
            cur = cur[let]
        if '*' in cur:
            return True
        else: 
            return False