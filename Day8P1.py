'''
Keep looping through l/r instructions until zzz is found. 

Simple approach is to keep iterating until target node == zzz.

Better approach is to use a dictionary and convert the mapping
'''

def read_file(file_name):
    with open(file_name,"r") as data:
        return data.read().split("\n\n")

def mapping_to_hash(mapping):
    mapping_hash = {}
    for line in mapping.split("\n"):
        mapping_hash[line[:3]] = [line[7:10],line[12:15]]
    return(mapping_hash)

def main(file_name):
    LR_instructions,mapping = read_file(file_name)
    curr_node = "AAA"
    mapping_hash = mapping_to_hash(mapping)
    step_counter = 0
    while curr_node != "ZZZ":
        for instr in LR_instructions:
            if instr == "L":
                curr_node = mapping_hash[curr_node][0]
            elif instr == "R":
                curr_node = mapping_hash[curr_node][1]
            step_counter += 1
    
    print(step_counter)

if __name__ == "__main__":
    main("Day8.txt")