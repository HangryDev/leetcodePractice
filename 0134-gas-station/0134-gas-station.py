class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        answer = 0
        #order = [i for i in range(len(gas))] #[0,1,2,3,4,5]
         
        can = [item1 - item2 for item1, item2 in zip(gas, cost)]
        if sum(can) < 0 :
            return -1 

        # 누적합이 음수가 되는 구간이 나오는지는 계속 체크해야겠네 
        # 1~100중에 1~10이 음수 구간이면, 그걸 또 더할 필요는 없을듯. 
        # 2~10이라고 다른 결과가 나오지는 않을 것이다

        i = 0 
        mark = 0 
        total = 0
        
        while can: 
            total += can.pop(0)
            i += 1
            if total < 0: 
                can.append(total)
                total = 0 
                answer = i
        
        return answer
        
        """
        for i in range(len(gas)):
            current_gas = 0 
            
            for j in order:
                current_gas += gas[j]
                current_gas -= cost[j]
                
                if current_gas < 0:
                    a = order.pop(0)
                    order.append(a)
                    break; 
                
            if current_gas >= 0 :
                answer = i 
                break; 
   
        return answer 
            
        """
        


