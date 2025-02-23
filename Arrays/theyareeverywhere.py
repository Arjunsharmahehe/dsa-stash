'''
Problem Title: They are everywhere
Problem Link: https://codeforces.com/problemset/problem/701/C
'''

def main():
    n = int(input())    # Taking the length of the input string
    string = input()    # Taking the input string
    s = set(string)     # Creating a set to get all the distinct characters
    hashmap = dict()    # A hashmap to track the frequency of each character in the substring
    size = len(s)       # Minimum count required
    count = 0           # Initial count of distinct elements
    l , r = 0, 0
    ans = n

    while(l <= r):

        # When the number of distinct chars in substring is equal to the min required size
        if count == size:   
            ans = min(ans, r - l)   # Take the min of length of current substring and itself

            # Reducing the number of occurences of string[l] as we will shift l by 1
            hashmap[string[l]] -= 1

            # If the occurence of the character drops to 0, it means:
            # That character is absent in the substring, meaning the number
            # of distinct characters decreases in the substring, hence -> count--
            if hashmap[string[l]] == 0:
                count -= 1

            # Mandatory increment
            l += 1
        

        elif r < n:
            
            # If we visit a new character that hasn't been mapped, we initialise it
            # with a frequency of 1 and increment the count as it is a new char
            if string[r] not in hashmap:
                hashmap[string[r]] = 1
                count += 1

            # If the char exists, but it's frequency has been reduced to 0
            # (meaning it is absent in the substring) we increment the count
            # and the frequency by 1
            elif hashmap[string[r]] == 0:
                hashmap[string[r]] = 1
                count += 1

            # Else, we just increase it's number of occurences (frequency)
            else:
                hashmap[string[r]] += 1

            # Mandatory increment
            r += 1

        # If r exceed n, we break out of the loop
        else:
            break

    print(ans)

if __name__ == "__main__":
    main()
