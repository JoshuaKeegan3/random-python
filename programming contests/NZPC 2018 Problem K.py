# Folding rectange problem
# Problem k NZ Programming contest
##


#Width, Height, Folds, Squares to check
#TLRB d cm away
Sample_Input = '''3 3 2 2
L2
B1
2 1
1 1
0 0 0 0'''

Sample_Output ='''4
2'''
def fold_top(d):
    global grid
    if d*2 > len(grid[0]):
        for i in range(d-1):#fold col
            for j in range(len(grid[0])):#each position along the row
                grid[(d-1)*2-i][j] = grid[(d-1)*2-i][j] + grid[i][j]# add
        for i in range(d-1):
            del grid[0]#delete

    else:
        for i in range(d):#fold col
            for j in range(len(grid[0])):#each position along the row
                grid[(d)*2-i][j] = grid[(d)*2-i][j] + grid[i][j]# add

        for i in range(d):
            del grid[0]#delete
        
def rotate_start(s):
    global grid
    if s == 'T':
        a=0
    elif s== 'L':
        a=3
    elif s == 'B':
        a=2

    elif s == 'R':
        a=1

    for i in range(a):

        grid = rotate(grid)

def rotate_finish(s):
    global grid
    if s == 'T':
        a=0
    elif s== 'L':
        a = 1
    elif s == 'B':
        a = 2

    elif s == 'R':
        a = 3
    for i in range(a):
        
        grid = rotate(grid)
        
def rotate(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]
    # return map(list, list_of_tuples)
 
grid = []
_input = Sample_Input.split('\n')
_input[0] = _input[0].split(' ')
nof = _input[0][3]
for i in range(1+int(nof), len(_input)):
    _input[i] = _input[i].split(' ')
for i in range(1,len(_input)-int(nof)):
    _input[i] = list(_input[i])

# Create grid
for col in range(int(_input[0][1])):
    grid.append([])
    for row in range(int(_input[0][0])):
        grid[col].append(1)
# preform folds
for i in range(int(nof)):
    print(grid)
    rotate_start(_input[i+1][0])
    temp_string = ''
    for j in range(1, len(_input[i+1])):
        temp_string += _input[i+1][j]
    temp_int = int(temp_string)
    fold_top(temp_int)
    rotate_finish(_input[i+1][0])
    print(grid)

# Check locations
for i in range(1+int(nof),len(_input),1):
    if len(_input[i]) == 2:
        # (x,y)
        print(grid[int(_input[i][1])-1][int(_input[i][0])-1])
        

    
        

        

