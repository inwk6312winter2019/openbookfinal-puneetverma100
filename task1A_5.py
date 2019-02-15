def starts_with_vow (vow):
	vow = open("book.txt") 
      
    # Intializing count variable to 0 
    count = 0
      
    # Creating a set of vowels 
    vowel = set("aeiouAEIOU") 
      
    # Loop to traverse the alphabet 
    # in the given string 
    for alphabet in vow: 
      
        # If alphabet is present 
        # in set vowel 
        if alphabet in vowel: 
            count = count + 1
      
    print("No. of vowels :", count) 
      
# Driver code  
vow = file
  
# Function Call 
vowel_count(vow)
