// Title: Minimum Bit Flips to Convert Number

// Problem Statement: Given two integers start and goal, return the minimum number of bit 
//                    flips to convert start to goal.

#include <iostream>
using namespace std;

int minBitFlips(int start, int goal) {
    int ans = 0;

   // XOR will give us the bits that need to be flipped
   int XOR = start^goal;

   while(XOR != 0){
    // if the last bit is 1, we will increment count
    ans = ans + (XOR & 1);

    // Right shift the number to check the next bit
    XOR = XOR>>1;
   } 

   return ans;
}