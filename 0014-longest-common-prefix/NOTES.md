20min total. not sure how much for understanding/solving/coding. inital score 98.68% / 11.06%

# approach 1 : Horizontal Scanning (mine)
- first string becomes prefix. 
- compare with next one to get common prefix. 
- keep going until the last one 
- 'if prefix = "" the break' should be needed, but actually slowed down runtime. 

# approach 2 : Vertial Scanning 
- search by each character of first string


# approach 3 : Divide and conquer (recursive) 
- divide strs by two until every segment has two or less. 
- then compare the segment
- not really time efficient in the case

# approach 4: binary tree
- minlen = shortest string's length = initial high
- move "low" by one characters towards "high" and see if its LCP
- if so, move "low" again. if not, move high towards low. 


# approach 5 : tries
- no idea bc not familiar with tries yet
