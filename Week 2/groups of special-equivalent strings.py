class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        odd=['' for _ in range(len(A))]
        even=['' for _ in range(len(A))]
        
        for strg in range(len(A)):
            for let in range(len(A[0])):
                if let%2==0:
                    even[strg]+=A[strg][let]
                else:
                    odd[strg]+=A[strg][let]
        for strg in range(len(even)):
            even[strg]=sorted(even[strg])
        for strg in range(len(odd)):
            odd[strg]=sorted(odd[strg])       
        new=['' for _ in range(len(A))]
       
        
        for strg in range(len(A)):
            for let in range(len(A[0])):
                if let%2==0:
                    x = even[strg].pop(0)
                    new[strg]+=x
                else:
                    x = odd[strg].pop(0)
                    new[strg]+=x
        
        ans = set(new)
       
        return len(ans)