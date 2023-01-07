* took ~10 mins to understand problems & come up with solution, 5 mins to code. ~2min no debug. 


# approach #1 - brute force. (my initial approach) 
- pair every element to see if they "complement"
-- complement  =  subtracting element from target , 

# approach #2 - two-pass hashmap 
- two-pass means "hashtable used twice" 
- trades space for speed
- create hashtable, {key: list value , value : list index}
- get complement by subtracting element from target , then search it in hashmap. 
- return if there is complement. 
- complement cannot be element itself. 

# approach #3 - one-pass hashmap
- one-pass means "hashtable used once" 
- while inserting elements in hashtable, check if complement exists.
- iterate once less 


# code toolbox: 
- list.index(i)
- didn't like len(nums) - alternatives?
- breaking out of double for loops : for - else 

