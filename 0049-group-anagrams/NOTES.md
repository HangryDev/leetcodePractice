​       
3 mins to nail approach. coded 27 mins. 
        - 1 sort words by char in strs
        - 2 put 1's result in dict. ex) {'aet': \["ate"\]} 
        - 3 repeat 1-2 until end of strs
        - 4 return bigdict Value
        - o(n)  

changed approach midst. first tried key as nested dict. {{b:1, a:1, t:1} : "bat"}
fixed: sorted word by char and used that as key
      

# approach 1 : (mine) 
as said above 


# approach 2 : count
the same, but keys are count of each chars 
![image](https://user-images.githubusercontent.com/49356933/216814795-4aa05e50-8826-49b6-b095-5e7c274f2ec7.png)


# stuck on: 
1: can you have a (nested) dict as a key for a dict? 
2: updating dict when value is list type 
3: how to sort string by char

