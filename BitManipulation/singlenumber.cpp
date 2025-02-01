// Problem Statement: Given a non-empty array of integers nums, every element appears twice 
//                    except for one. Find that single one.
//                    You must implement a solution with a linear runtime complexity and use 
//                    only constant extra space.
#include <iostream>
#include <vector>

int singleNumber(vector<int>& nums) {

    // Checking if the length of the array is 1
    if(nums.size() < 2) return nums[0];

    // XOR return 0 when we XOR the same numbers
    int XOR;
    XOR = nums[0];
    for(int i = 1; i < nums.size(); ++i){
        XOR = XOR^nums[i];
    }

    // The resultant value of XOR is the number that appears odd number of times
    return XOR;

}