DIRECTION = {
    'L': -1,
    'R': +1
}


def counter_part1(lines):
    pos = 50
    counter = 0

    for i in range(len(lines)):
        
        to_move = DIRECTION[lines[i][0]] * int(lines[i][1:])
        pos = (pos + to_move) % 100
        #print(f'move: {to_move} | new_pos: {pos}')
        if pos == 0:
            counter += 1

    print(f'The first code to open the safe is {counter}')


def counter_part2(lines):
    pos = 50
    counter = 0

    for i in range(len(lines)):
        counter_pre = counter
        to_move = DIRECTION[lines[i][0]] * int(lines[i][1:])
        print(pos, to_move, (pos+to_move)%100)
        # All hundreds just turn the handle in circles passing it once per 100
        num_hundreds = int(to_move/100) # int() always rounds down
        if num_hundreds != 0:
            counter += abs(num_hundreds) 
            to_move = to_move - (num_hundreds * 100)


        if to_move == 0:
            continue # Fallback in case pos = 0 and to_move = k*100 - also, saves time for the rest
        if pos == 0:
            pos = (pos + to_move) % 100 # Otherwise the 'pass 0' clause can trigger for L movements
            continue

        if ((pos+to_move)>100) or ((pos+to_move)<0):
            counter += 1

        pos = (pos + to_move) % 100
        if pos == 0:
            counter += 1

        print(f'count increased by {counter-counter_pre} | counter: {counter}')
        #input()
    print(f'The real code to open the safe is {counter}')

def main():
    fname = 'input'
    with open(fname, 'r') as f:
        lines = f.readlines()
        f.close()

    counter_part1(lines)
    counter_part2(lines)


        




    

if __name__ == '__main__':
    main()