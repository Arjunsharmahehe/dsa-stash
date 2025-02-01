''' Problem Statement: Given an array of integers nums and an integer target, return indices 
                       of the two numbers such that they add up to target. 
                       You may assume that each input would have exactly one solution, and 
                       you may not use the same element twice. 
                       
    Return Type: [index1, index2]'''


def twoSum(nums, target):
    hashmap = {}
    ind = -1
    for i in nums:
        ind+=1
        if target-i in hashmap:
            return [hashmap[target-i], ind]
            break
        else:
            hashmap[i] = ind
