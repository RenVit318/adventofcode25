import numpy as np

def part1(grid):
    # Implemenation based on first version using lists and '@'
    # Directly translated to numpy and numbers for part 2
    width = len(grid[0])
    height = len(grid)
    
    counter = 0
    for i in range(height):
        for j in range(width):
            square = grid[i][j]
            if square != 1:
                continue
            
            # Check 3x3
            num_adjacent = 0
            for m in range(max(i-1, 0), min(i+2, height)):
                #print(grid[m][max(j-1, 0): min(j+2, width)])
                for n in range(max(j-1, 0), min(j+2, width)):
                    if m == i and n == j:
                        continue
                    if grid[m][n] in ['1', '2']:
                        num_adjacent += 1
            #print(num_adjacent)
            if num_adjacent < 4:
                #print(num_adjacent)
                counter += 1
 
    print(f'There are {counter} rolls that can be picked up')
                    
                
def part2(grid):
    h = grid.shape[0]
    w = grid.shape[1]

    total_removed = 0
    loop_removed = 1 # Initialize > 0 so loop starts
    
    while loop_removed > 0:
        loop_removed = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0:
                    #print('continuing')
                    continue
                
                # Make 3x3 with numpy                
                section = grid[max(i-1, 0):min(i+2, h), max(j-1, 0):min(j+2, w)]
                if np.sum(section) < 5: # Now including the paper to be picked up
                    grid[i][j] = 0 # Remove the paper
                    total_removed += 1
                    loop_removed += 1
                    
    print(f'With removing, there are {total_removed} rolls that can be picked up')

            

def main():
    fname = 'input'
    #grid = []
    with open(fname, 'r') as f:
        lines = f.readlines()
        # -1 because of the \n at the end in input files
        grid = np.zeros((len(lines), len(lines[0])-1), dtype=int)
        
        for i, line in enumerate(lines):
            if line.endswith('\n'):
                line = line[:-1]
            for j, val in enumerate(line):
                if val == '@':
                    grid[i][j] = 1
                    
    print(grid)

    #part1(grid)
    part2(grid)
    
if __name__ == '__main__':
    main()
