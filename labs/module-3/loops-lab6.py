blocks = int(input("Enter the number of blocks: "))

#
# write your code here.
height = 0
blocks_left = blocks
blocks_used = 0
n_blocks = 1 

while blocks_left >= n_blocks: 
    blocks_used = n_blocks + 1 
    blocks_left -= n_blocks 
    n_blocks += 1
    height += 1 
#	

print("The height of the pyramid:", height)

