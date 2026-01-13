# Write a function to crush candy in one dimensional board. In candy crushing games, groups of like items are removed from the board. In this problem, any sequence of 3 or more like items should be removed and any items adjacent to that sequence should now be considered adjacent to each other. This process should be repeated as many time as possible. You should greedily remove characters from left to right.


# Input: "aaabbbc"
# Output: "c"
# Explanation:
# 1. Remove 3 'a': "aaabbbbc" => "bbbbc"
# 2. Remove 4 'b': "bbbbc" => "c"

# Input: "aabbbacd"
# Output: "cd"
# Explanation:
# 1. Remove 3 'b': "aabbbacd" => "aaacd"
# 2. Remove 3 'a': "aaacd" => "cd"

# Input: "aabbccddeeedcba"
# Output: ""
# Explanation:
# 1. Remove 3 'e': "aabbccddeeedcba" => "aabbccdddcba"
# 2. Remove 3 'd': "aabbccdddcba" => "aabbcccba"
# 3. Remove 3 'c': "aabbcccba" => "aabbba"
# 4. Remove 3 'b': "aabbba" => "aaa"
# 5. Remove 3 'a': "aaa" => ""

# Input: "aaabbbacd"
# Output: "acd"
# Explanation:
# 1. Remove 3 'a': "aaabbbacd" => "bbbacd"
# 2. Remove 3 'b': "bbbacd" => "acd"

# Follow-up:
# What if you need to find the shortest string after removal?

# Input: "aaabbbacd"
# Output: "cd"
# Explanation:
# 1. Remove 3 'b': "aaabbbacd" => "aaaacd"
# 2. Remove 4 'a': "aaaacd" => "cd"
'''

O(n) Each character is pushed to and popped from the stack at most once.
'''

def candy_crush(s, k):
    # I'll use a stack to simulate the process of removing adjacent duplicates.
    # Each element in the stack stores: [character, consecutive count].
    stack = []

    # Traverse each character in the string.
    for i in range(len(s)):
        c = s[i]
        if not stack or stack[-1][0] != c:
            stack.append([c, 1])
        else:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()

    # Reconstruct the final string from the stack.
    sb = []
    for char, count in stack:
        sb.append(char * count)  # Append the character `count` times 、
    return "".join(sb)  # Return the final cleaned string.



print(candy_crush("abbbcc",3)) # c
print(candy_crush("aaaabbbc",3)) # c
print(candy_crush("aabbbacd",3)) # cd
print(candy_crush("aabbccddeeedcba",3)) # blank expected
print(candy_crush("aabbbaacd",3)) # cd
print(candy_crush("dddabbbbaccccaax",3)) # x