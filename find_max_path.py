"""
Create an algorithm that finds the path from top-left to bottom-right
that goes through the values of given array in a way that maximizes the 
sum of the values on path traveled. 
The traveler can only move in 'right' or 'down' direction.
"""
class Solution:
    #create the function that finds the path with max sum value
    def max_value(mat):
        max = Solution.move(mat,0,0,0)
        return max
    #create a function that traverses through all possible ways through the array recursively. 
    def move(mat, i, j, pocket, max_sum=0):
        #define the int variable that starts at 0 to record the sum of the values of a single path
        pocket= pocket + mat[i][j]
        #if the current location is at the bottom-right of the given 2D array return the resulting sum
        if i==len(mat)-1 and j==len(mat[0])-1:
            return pocket
        #if not, make a recursive move to 'down' direction if possible. Note that as each recursive move continues only with previous 'pocket'(i.e.sum value) 
        if i+1 < len(mat):
            total = Solution.move(mat, i+1, j, pocket)
            #if resulting sum is bigger than existing max, max_sum = current total
            if total > max_sum:
                max_sum = total
        #also make a recursive move to 'right' direction if possible
        if j+1 < len(mat[0]):
            total = Solution.move(mat, i, j+1, pocket)    
            #if resulting sum is bigger than existing max, max_sum = current total
            if total > max_sum:
                max_sum = total
        #return the final max_sum
        return max_sum

#sample 2D array
mat = [
    [0, 3, 0, 2],
    [1, 2, 3, 3],
    [6, 0, 3, 2]
]

#result is 13
print(Solution.max_value(mat))