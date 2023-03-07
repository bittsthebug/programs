 PATTERN PRINTING 
1.    *
     * *
    * * *
   * * * *  
x = 1
y = 3

while (x <= 4):
    print(" "*y + "* "*x + " "*y)
    x = x + 1
    y = y - 1
    
 2.     *
        * *
        * * *
        * * * * 
        
x = 1
y = 3

while(x <= 4):
    print("* "*x + " "*y)
    x = x + 1
    y = y - 1 
    
3.   
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

x = int(input("Enter the number of rows : "))

for r in range(x):
    for c in range(r + 1):
        print(r + 1 , end = " ")
    print()

4.
        * * * *
        * * *
        * * 
        * 
x = 4
y = 0

while(y<=3):
    print("* "*x + " "*y)
    x = x-1
    y = y+1 
    
5.      * * * *
          * * *
            * *
              * 
            
x = 4 
y = 0

while(y <= 3) :
    print("  "*y + "* "*x)
    y = y + 1
    x = x - 1 
    
6. 
        *
      * *
    * * *
  * * * *
  
x = 1
y = 3 

while(x <= 4):
    print("  "*y + "* "*x)
    x = x + 1
    y = y - 1
    
7.
        * * * *
         * * * 
          * * 
           * 

x = 4 
y = 0 

while(y <= 3) :
    print(" "*y + "* "*x + " "*y)
    y = y + 1
    x = x - 1 
    

8. 
        * * * *
       *     *
      *     * 
     * * * * 
        
size = int(input("Enter the size of the rhombus: "))
 
for i in range(size):
    for j in range(size-i):
        print(" ", end="")
    for j in range(size):
        if i == 0 or i == size-1 or j == 0 or j == size-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
