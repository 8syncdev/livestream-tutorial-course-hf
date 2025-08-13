'''
j
01234   i
*       0, i=0, j=0, j=1 =>j <= i (0 <= 0)
**      1, j=0,i=1, j=1, i=1
***     2
****    3
*****   4
'''

n = int(input())

for i in range(n):
    for j in range(n):
        if j <= i:
            print("*", end="")
    # Sau khi vẽ xong các cột cho 1 hàng
    print()
print()
'''
n=5
j
01234   i
*   *   0 , i=0,j=0         i=0,j=4 (n-j-1==i 5-4-1=0)
 * *    1 , i=1,j=1=>j==i   i=1,j=3
  *     2 , i=2,j=2         i=2,j=2
 * *    3
*   *   4
'''

for i in range(n):
    for j in range(n):
        if i==j or n-j-1==i:
            print("*", end="")
        else:
            print(" ", end="")
    # Sau khi vẽ xong các cột cho 1 hàng
    print()
print()


'''
n=4
cột = 2*n-1=2*4-1=7
j
0123456     i
   *        0   , i=0,j=3 (n-1-i=4-1=3)
  ***       1   , i=1,j=(2,3,4)
 *****      2   , i=2,j=(1,2,3,4,5)
*******     3
'''

for i in range(n):
    for j in range(2*n):
        if n-i-1 <= j and j <= n+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    # Sau khi vẽ xong các cột cho 1 hàng
    print()
print()

'''

'''
