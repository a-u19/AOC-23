'''
Similar work to part 1, except all nodes ending in A have to be traversed

- first approach was to try and shift the entire list of nodes that ended in A with each instruction
- after some googling, LCM seems to be a better method
'''
from math import lcm

def read_file(file_name):
    with open(file_name,"r") as data:
        return data.read().split("\n\n")

def mapping_to_hash(mapping):
    mapping_hash = {}
    for line in mapping.split("\n"):
        mapping_hash[line[:3]] = [line[7:10],line[12:15]]
    return(mapping_hash)

def find_all_starting_nodes(mapping_hash):
    starting_nodes = []
    for node in mapping_hash.keys():
        if node[2] == "A":
            starting_nodes.append(node)
    return (starting_nodes)

def main(LR_instructions,mapping_hash,curr_node):
    step_counter = 0
    while curr_node[2] != "Z":
        for instr in LR_instructions:
            if instr == "L":
                curr_node = mapping_hash[curr_node][0]
            elif instr == "R":
                curr_node = mapping_hash[curr_node][1]
            step_counter += 1
    
    return (step_counter)

def part2main(file_name):
    LR_instructions,mapping = read_file(file_name)
    mapping_hash = mapping_to_hash(mapping)
    steps_list = []
    for starting_node in find_all_starting_nodes(mapping_hash):
        steps_list.append(main(LR_instructions,mapping_hash,starting_node))
    
    print(steps_list)

    print(lcm(*steps_list))


if __name__ == "__main__":
    part2main("Day8.txt")

# def read_file(file_name):
#     with open(file_name,"r") as data:
#         return data.read().split("\n\n")

# def mapping_to_hash(mapping):
#     mapping_hash = {}
#     for line in mapping.split("\n"):
#         mapping_hash[line[:3]] = [line[7:10],line[12:15]]
#     return(mapping_hash)

# def find_all_starting_nodes(mapping_hash):
#     starting_nodes = []
#     for node in mapping_hash.keys():
#         if node[2] == "A":
#             starting_nodes.append(node)
#     return (starting_nodes)

# def is_final_character_Z_for_all_items(list):
#     for item in list:
#         if item[2] != "Z":
#             return False
#     return True

# def move_to_L(list,mapping_hash):
#     for i in range(len(list)):
#         list[i] = mapping_hash[list[i]][0]
#     print("list is now: {}".format(list))
#     return (list)

# def move_to_R(list,mapping_hash):
#     for i in range(len(list)):
#         list[i] = mapping_hash[list[i]][1]
#     print("list is now: {}".format(list))
#     return list

# def main(file_name):
#     LR_instructions,mapping = read_file(file_name)
#     print(LR_instructions)
#     mapping_hash = mapping_to_hash(mapping)
#     starting_nodes = find_all_starting_nodes(mapping_hash)
#     print("starting list is {}".format(starting_nodes))
#     step_counter = 0
#     while not is_final_character_Z_for_all_items(starting_nodes):
#         for instr in LR_instructions:
#             if instr == "L":
#                 starting_nodes = move_to_L(starting_nodes,mapping_hash)
#             elif instr == "R":
#                 starting_nodes = move_to_R(starting_nodes,mapping_hash)
#             step_counter += 1
    
#     print(step_counter)

# if __name__ == "__main__":
#     main("Day8.txt")