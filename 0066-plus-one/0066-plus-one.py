class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        zeros = []

        #모든 수를 다 체크했거나, 마지막 자리가 9 이하면 loop 벗어남. 
        #9인 동안은 zeros에 0을 하나씩 append. 
        while digits and digits[-1] == 9:
            i = digits.pop()
            zeros.append(0)
            print(digits, i, zeros)
            
        # 이제 마지막 자리에 1을 더하고, 0들을 붙일 거임.  
        #예외 처리 시작 
        #1- 만약에 digits가 다 9여서 텅 비어있으면, digits에 1을 추가하면 됨
        if digits == []:
            digits.append(1)
            digits.extend(zeros)
        #2 - 9가 하나도 없었다면: 
        elif zeros == []:
            digits[-1] += 1
        else: 
            # 마지막 자리에 값 1을 더 추가함
            digits[-1] += 1
            # 오른쪽에 9의 개수만큼 0을 append함
            digits.extend(zeros)
        
        return digits 