 ### took 40 mins. 
 - 10mins to understand & to code 
 - 20 mins for mending exceptional cases  :( 
 
 # approach 1 : stack 
 - put opening paranthesis in stack
 - encounter closing paranthesis -> compare with stack 
 - if len stack > 0 or closing paranthesis comes first, return false

# codes
- return stack == 0 : a way to return true/false 
- looking up something in dict keys => if a in dict // if a in dict.keys() <- the same
- keyError means i put wrong key in dict
- dict[key] takes time. instead, use 'temp = dic[one]' to replace calculate. 
- if len(res) doesn't need >0. 
- ex)
    def isValid(self, s: str) -> bool:
        dic = {'(':1 , ')':2 , '[':3 , ']':6 , '{':5 , '}':10}
        res = []
        for one in s:
            temp = dic[one]
            if(temp %2 ):
                res.append(temp)
            else:
                if(len(res) and res[-1]==temp//2):
                    del res[-1]
                else:
                    return False
        return res==[]
