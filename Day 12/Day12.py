# Used https://www.youtube.com/watch?v=g3Ms5e7Jdqo&t=310s - youtube video by HyperNeutrino
cache = {}

def count(cfg, nums):
    if cfg == "": # are there any characters left in the configuration?
        return 1 if nums == () else 0 # return 1 if there aren't and there are no numbers left because it's a match
    if nums == (): # are there any numbers left over?
        return 0 if "#" in cfg else 1 # if not and there's a hash implying that there should be another number in nums, then return 0
    
    key = (cfg, nums)
    if key in cache:
        return cache[key]
    
    res = 0
    if cfg[0] in ".?": # treating ? as another dot, first dot can be ignored
        res += count(cfg[1:], nums) # rerun count but just ignore first dot
    if cfg[0] in "#?": # treat ? as another # then a new block is starting
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            res += count(cfg[nums[0] + 1:], nums[1:])
    
    cache[key] = res
    return res
             
def main(file):
    total = 0    
    with open(file, 'r') as f:
        for line in f.readlines():
            cfg, nums = line.split()
            nums = tuple(map(int, nums.split(",")))
            total += count(cfg, nums)  
    return (total)

def main_part_two(file):
    total = 0    
    with open(file, 'r') as f:
        for line in f.readlines():
            cfg, nums = line.split()
            cfg = "?".join([cfg] * 5)
            nums = tuple(map(int, nums.split(",")))
            nums *= 5
            total += count(cfg, nums)  
    return (total)    


if __name__ == "__main__":
    print(f"Answer to part one is {main('day12input.txt')}")
    print(f"Answer to part two is {main_part_two('day12input.txt')}")