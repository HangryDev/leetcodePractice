class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(target, index, path):
            if target < 0:
                return  # backtracking
            if target == 0:
                res.append(path)
                return 
            for i in range(index, len(candidates)):
                dfs(target-candidates[i], i, path+[candidates[i]])
        
        dfs(target, 0, [])
        return res
          

        
# 1. path의 사용.
# 2. return answer 를 통해, combinationSum에 넣을 수 있다  
# 3. return 0. 이 아니라 return 만 때리면 더 좋다 

