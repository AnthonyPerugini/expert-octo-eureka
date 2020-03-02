'''There is a diamond hidden on an N\times NN×N grid on the square (x_D,y_D)(x 
D
​	
 ,y 
D
​	
 ), where x_Dx 
D
​	
  and y_Dy 
D
​	
  are integers. You will attempt to find the diamond's position with as few guesses as possible.

Every guess, you suggest a pair of coordinates (x_Gx 
G
​	
 , y_Gy 
G
​	
 ) which represent one of the squares on the grid. If the diamond isn't there you are given a hint as to where to go to continue looking. You are told either NW, N, NE, E, SE, S, SW, or W:

W implies x_D < x_Gx 
D
​	
 <x 
G
​	
  and y_D = y_Gy 
D
​	
 =y 
G
​	
 
NW implies x_D < x_Gx 
D
​	
 <x 
G
​	
  and y_D > y_Gy 
D
​	
 >y 
G
​	
 
etc.
So an incorrect guess narrows the diamond's position down to one of eight options. You are given one of the cardinal directions if heading up, down, left or right will take you straight to the diamond. Otherwise, you are given the two cardinal directions you will have to move along in order to reach the diamond.

If you can get the diamond with 10 guesses or less (i.e. at most 9 wrong guesses and one right one), you get to keep the diamond. What is the largest NN for which you can guarantee success?
'''


def checkio(n):
    total = 0
    if n == 1:
        return 1
    else:
        total += (2 * checkio(n-1)) + 1
    return total


print(checkio(10))