import numpy as np

def part1(lines):
    counter = 0
    for bank in lines:
        if bank[-1] == '\n':
            bank = bank[:-1]
        bank = str(bank)
        idx_highest_digit = -1
        highest_digit = -1 
        for i, char in enumerate(bank):
            if (i+1) == len(bank):
                continue # don't need to look at last digit for tens
            if int(char) > highest_digit:
                # Reset the list
                highest_digit = int(char)
                idx_highest_digit = i
                if highest_digit == 9:
                    break
        
        second_digit = -1
        for i in range(idx_highest_digit+1, len(bank)):
            if int(bank[i]) > second_digit:
                second_digit = int(bank[i])
        jolt = 10*highest_digit + second_digit
 
        counter += jolt
    print(f'The total output is {counter} jolts')
    
def part2(lines):
    counter = 0
    num_digits = 12
    for bank in lines:
        if bank[-1] == '\n':
            bank = bank[:-1]

        digits = np.full(num_digits, -1)
        digit_idxs = np.full(num_digits, -1)
        N = len(bank)
        
        #print(f'N = {N}')
        #print(bank)
        for i in range(num_digits):
            # First go around
            #print(digits)
            #print(N-num_digits+i+1)
            #print(bank[digit_idxs[i-1]+1:int(N-num_digits+i+1)])
            for j in range(digit_idxs[i-1]+1, int(N-num_digits+i+1)):
                if int(bank[j]) > digits[i]:
                    digits[i] = int(bank[j])
                    digit_idxs[i] = j
        
        jolts_str = ""
        for digit in digits:
            jolts_str += str(digit)
        counter += int(jolts_str)
        
    print(f'The total overload output is {counter} jolts')
        #print(digits)
        #input()
    
def main():
    fname = 'input'
    with open(fname, 'r') as f:
        lines = f.readlines()
    part2(lines)
    
    
        
if _name_ == '_main_':
    main()
