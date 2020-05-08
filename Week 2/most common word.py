class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import collections
        
        paragraph=paragraph.lower()
        remove = ['!',"?","\'",",",";","."]
        for i in paragraph:
            if i in remove:
                
                paragraph = paragraph.replace(i, " ")
            
        wordlist = paragraph.split()
       
        p = collections.Counter(wordlist)
        for word in p:
            if word in banned:
                p[word]=0
        
        for word,i in p.most_common(1):
            return word