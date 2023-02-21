​


Code Examples:  


# Simple DFS python code beat 90% : https://leetcode.com/problems/number-of-islands/discuss/56585/Simple-DFS-python-code-beat-90
*재귀 안 쓰는 방법

```python

def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
        return 0
        
    m = len(grid)
    n = len(grid[0])
    sum  = 0
    
    for i in range(m):
        for j in range(n):
            
            if grid[i][j] == "0":
                continue
            else:
                
                #sum up only once per chance of meeting "1"
                sum += 1
                stack = list()
                stack.append([i,j])
                
                #visit each "1" in the adjacent area using a stack
                while len(stack) != 0:
                    
                    [p,q] = stack.pop()
                    
                    if p >= 1 and grid[p-1][q] == "1":
                        stack.append([p-1,q])
                        
                    if p < m -1 and grid[p+1][q] == "1":
                        stack.append([p+1,q])
                    
                    if q >= 1 and grid[p][q-1] == "1":
                        stack.append([p,q-1])
                        
                    if q < n - 1 and grid[p][q + 1] == "1":
                        stack.append([p,q+1])
                    
                    #mark as visited
                    grid[p][q] = "0"
    
    
    
    return sum
    
    # 
```
# [Python3]Number of Islands BFS + DFS   https://leetcode.com/problems/number-of-islands/discuss/345981/Python3Number-of-Islands-BFS-%2B-DFS

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    print(i,j)
                    self.dfs(grid,i,j)
                    count  += 1
        #print(grid)
        return count
    # use a helper function to flip connected '1's to 0
    def dfs(self,grid,i,j):
        grid[i][j] = 0
        for dr,dc in (1,0), (-1,0), (0,-1), (0,1):
            r = i + dr
            c = j + dc
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]=='1':
                self.dfs(grid,r,c)
```



# [Python] 3 solutions: DFS, BFS, Union-Find - Concise & Clean   https://leetcode.com/problems/number-of-islands/discuss/583745/Python-3-solutions%3A-DFS-BFS-Union-Find-Concise-and-Clean

Solution 1: DFS
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]
        
        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == "0": return 0
            grid[r][c] = "0"  # Mark as visited
            for i in range(4):
                dfs(r + DIR[i], c + DIR[i+1])
            return 1
        
        ans = 0
        for r in range(m):
            for c in range(n):
                ans += dfs(r, c)
        return ans
```

Solution 2: BFS
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]
    
        def bfs(r, c):
            if grid[r][c] == "0": return 0
            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == "0": continue
                    grid[nr][nc] = "0"  # Mark as visited
                    q.append([nr, nc])
            return 1
    
        ans = 0
        for r in range(m):
            for c in range(n):
                ans += bfs(r, c)
        return ans
```

Solution 3a: Union-Find (Naive)
```python
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        
    def find(self, u):
        while u != self.parent[u]:
            u = self.parent[u]
        return u
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        self.parent[pu] = pv
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIR = [0, 1, 0, -1, 0]
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m*n)
        
        component = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "0": continue
                component += 1
                curId = r * n + c
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == "0": continue
                    neiId = nr * n + nc
                    if uf.union(curId, neiId):
                        component -= 1
        return component
```
    

```python
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        if self.size[pu] < self.size[pv]:  # Merge pu to pv
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        else:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIR = [0, 1, 0, -1, 0]
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m*n)
        
        component = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "0": continue
                component += 1
                curId = r * n + c
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == "0": continue
                    neiId = nr * n + nc
                    if uf.union(curId, neiId):
                        component -= 1
        return component
```
Complexity

Time: O(MN * α(MN)), where M <= 300 is number of rows, N <= 300 is number of columns in the matrix.
Explanation: Using both path compression and union by size ensures that the amortized time per UnionFind operation is only α(n), which is optimal, where α(n) is the inverse Ackermann function. This function has a value α(n) < 5 for any value of n that can be written in this physical universe, so the disjoint-set operations take place in essentially constant time.
Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure or https://www.slideshare.net/WeiLi73/time-complexity-of-union-find-55858534 for more information.
Space: O(M*N)
