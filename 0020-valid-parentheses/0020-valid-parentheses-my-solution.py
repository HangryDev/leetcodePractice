class Solution:
    def isValid(self, s: str) -> bool:
        # 일단 쌍들 다 제거하자 
        s = s.replace('()','').replace('[]','').replace('{}','')
        
        #1 pop
        dict = {'(':')', '[':']', '{':'}'}        
        stack = []
        #2 match
        #경우의 수 "((" "[" 
        # dict.keys()에 있으면 stack에 넣고 
        # dict.value()에 있는게 나오면, stack의 끝과 비교. (stack이 0 이상인지도 체크)
        # match 실패할 경우 False 
        # stack에 남는게 있으면 False
        # 끝까지 가면 True 
        
        
        e = False
        
        while s:
            pointer = s[0]; s = s[1:]
            if pointer in dict.keys():
                stack.append(pointer)
            elif pointer in dict.values() and stack != []: 
                if dict[stack[-1]] == pointer:
                    stack.pop(-1)
                else: 
                    break
            else:
                break
        else:
            if len(stack) > 0 : 
                e = False 
            else:
                e = True
        
        return e 
            
