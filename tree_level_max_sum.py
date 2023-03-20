#this is the given structure of the Node class
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def tree_level_max_sum(root):
    
    level_sums = {}       #set the dictionary to record the sums for each levels
    L = 1                 #track current level
    current = [root]      #track the nodes of current level
    #loop through the tree, summing the values of each level and adding the grouping the nodes of each level
    while True:
        if len(current) == 0:
            break
        next_level = []       #prepare an empty list to store the nodes of the next level
        current_sum = 0       #restart the sum value of current level
        #iterate through the nodes of current level
        for node in current:      
            current_sum += node.value    #add the value of the nodes to the sum of current level
            #add the nodes of the next level to the list of next_level nodes
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level_sums[L] = current_sum       #record the sum of current level
        L += 1                         #increment the level
        current = next_level         #set the list of next_level nodes as current list for the next iteration

    max_level, max_sum = max_value(level_sums)      #get the level with the max_sum with its value
    return print(f"The level with maximum sum is Level {max_level} with sum of {max_sum}.")

def max_value(dic):
    max_val = 0
    for key in dic:
        if dic[key] > max_val:
            max_val = dic[key]
            max_key = key

    return max_key, max_val

n3 = Node(4, Node(3), Node(2))
n2 = Node(5, Node(4), Node(-1))
n1 = Node(1, n2, n3)

tree_level_max_sum(n1)
    
    
    