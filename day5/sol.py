import numpy as np

def part1(fresh_ids, stock_ids):
    counter = 0
    for idx in stock_ids:
        for i in range(fresh_ids.shape[0]):
            if idx >= int(fresh_ids[i][0]) and idx <= int(fresh_ids[i][1]):
                counter += 1
                break
    
    print(f'There are {counter} fresh items')

def part2(fresh_ids):
    fresh_id_ranges = np.zeros((0,2), dtype=int)
    first_low, first_high = fresh_ids[0]
    fresh_id_ranges = np.vstack((fresh_id_ranges, [int(first_low), int(first_high)]))
    # Need to track the index ranges - all numbers is not viable.
    for low, high in fresh_ids[1:]:
        low = int(low)
        high = int(high)
        #print('Adding in: ', low, high)
        # Test for any overlap in any of the ranges
        # If we find one, then include and clean up
        # Work out each of the possible cases separately
        match_found = False
        for i, id_range in enumerate(fresh_id_ranges):
            # Low in existing range, high outside of it
            if low >= id_range[0] and low < id_range[1] and high > id_range[1]:
                fresh_id_ranges[i][1] = high
                match_found = True
            # High in existing range, low outside of it
            elif high <= id_range[1] and high > id_range[0] and low < id_range[0]:
                fresh_id_ranges[i][0] = low
                match_found = True
            # New range encompasses old range
            elif low < id_range[0] and high > id_range[1]:
                fresh_id_ranges[i] = [low, high]
                match_found = True
            if match_found:
                break
        
        # Separate range
        if not match_found:
            #print('no overlap found, adding in separate')
            fresh_id_ranges = np.vstack((fresh_id_ranges, [low, high]))

        # Clean up the range array
        if fresh_id_ranges.shape[0] == 1:
            continue
        
        fresh_id_ranges = np.sort(fresh_id_ranges, axis=0)
        # Check for overlap
        for i in range(fresh_id_ranges.shape[0]-1):
            if fresh_id_ranges[i][1] >= fresh_id_ranges[i+1][0]:
                fresh_id_ranges[i][1] = fresh_id_ranges[i+1][1]
                fresh_id_ranges = np.delete(fresh_id_ranges, i+1, axis=0)
                #print('Found overlap, merging two rows')
                break # Stop because this only happens once a loop max
    
    # Count number of possible fresh IDs
    total = 0
    for low, high in fresh_id_ranges:
        total += high+1 - low
    print(f'Total number of fresh items is {total}')

def main():
    fname = 'input'
    with open(fname, 'r') as f:
        lines = f.readlines()
        
        fresh_ids = np.zeros((0,2), dtype=int)
        for i, line in enumerate(lines):
            if line.endswith('\n'):
                line = line[:-1]
            try:
                start, stop = line.split('-')
                fresh_ids = np.vstack((fresh_ids, np.array([[start, stop]])))
            except ValueError:
                break

        stock_ids = np.array(lines[i+1:], dtype=int)
        #print('\n Finished prep. now check ids.')
        part1(fresh_ids, stock_ids)
        part2(fresh_ids)

if __name__ == '__main__':
    main()
