class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if ord(word[0])>=ord('A') and ord(word[0])<=ord('Z'):
            count = 0
            for i in range(len(word)):
                if ord(word[i])>=ord('A') and ord(word[i])<=ord('Z'):
                    count = count+1
            if count==len(word) or count == 1:
                return 1==1
            else:
                return 1==2
        else:
            count=0
            for i in range(len(word)):
                if ord(word[i])>=ord('A') and ord(word[i])<=ord('Z'):
                    count = count+1
            if count == 0:
                return 1==1
            else:
                return 1==2