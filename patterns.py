from __future__ import print_function

"""
*
* *
* * *
* * * *
* * * * *
"""
# def make_pattern(n):

# 	for i in range(0, n):
# 		for j in range(0, i+1):
# 			print ("* ", end="")
# 		print("\r")



# if __name__ == "__main__":
# 	n = 5
# 	make_pattern(n)

# ========================================================================
"""
1
12
123
1234
12345
"""
# def make_pattern(n):
# 	for i in range(0, n):
# 		for j in range(0, i+1):
# 			print(j+1, end="")
# 		print("\r")

# if __name__ == "__main__":
# 	n = 5
# 	make_pattern(n)

# =========================================================================
"""
    *
   **
  ***
 ****
*****
"""

# def make_pattern(n):
# 	# k = 2*n -2
# 	k = n-1
# 	for i in range(0, n):
# 		for j in range(0, k):
# 			print(end=" ")
# 		k = k - 1
# 		for j in range(0, i+1):
# 			print("*", end="")
# 		print("\r")

# if __name__ == "__main__":
# 	n = 5
# 	make_pattern(n)


# =========================================================================
"""
        *
       * *
      * * *
     * * * *
    * * * * *
"""

# def make_pattern(n):
# 	k = n*2 - 2

# 	for i in range(0, n):
# 		for j in range(0, k):
# 			print(end=" ")
# 		k = k - 1
# 		for j in range(0, i+1):
# 			print("* ", end="")
# 		print("\r")

# if __name__ == "__main__":
# 	n = 5
# 	make_pattern(n)

# =========================================================================
""" 
******************
******************
******************
******************
**
**
**
**
**
"""

# def make_pattern(flag_width, flag_height, pole_height):
# 	pole_width = 2
# 	for i in range(0, flag_height):
# 		for j in range(0, flag_width):
# 			print("*", end="")
# 		print("\r")
# 	for i in range(0, pole_height):
# 		for j in range(0, pole_width):
# 			print("*", end="")
# 		print("\r")



# if __name__ == "__main__":
# 	flag_width = 18
# 	flag_height = 4
# 	pole_height = 5
# 	make_pattern(flag_width, flag_height, pole_height)

"""
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
"""
def printPascal(n):  
  
    for line in range(1, n + 1):  
        C = 1; # used to represent C(line, i)  
        for i in range(1, line + 1):  
              
            # The first value in a  
            # line is always 1  
            print(C, end = " ");  
            C = int(C * (line - i) / i);
            print ("---->", C, line, i)
        print("");  
  
# Driver code  
n = 5;  
printPascal(n); 
  
