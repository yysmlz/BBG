'''
Input:
chars = ['a','a','a','a','b','b','c','c','c','c','c']
k = 3
Process:
'a' * 4  ->  >k  -> "a4"
'b' * 2  -> ≤k  -> "bb"
'c' * 5  -> >k  -> "c5"
Output chars:
['a','4','b','b','c','5']
length = 6

General Idea:
for pointer move logic:
1.gain the cnt of a consecutive char
read 指向一段连续字符的起点
用 read 往右数有多少个相同字符（得到 cnt）
2. 根据 cnt 决定怎么写：cnt ≤ k → 写 cnt 个字符.cnt > k → 写 char + count read 跳到下一段的起点 重复直到read结束
We use two pointers to modify the character array in place:
one pointer is the read pointer, scans the array and counts the length of each consecutive run/segment of identical char.
write pointer overwrites the array with the required output.
For each run, if cnt ≤ k, we just write/copy the character cnt times. Otherwise, we write the start character once， followed by digits of cnt.
Finally, write is the new valid length of the modified array.

Clarify:
1.confirm input and output, is the form of input the char array or string? 
for output: should we only the first part of the array 
or return the whole modified array itself but remaining characters beyond are unused, Since the array has been modified in place

2.count 是否会大于10，是>=两位数？ 所以我们需要去 seperate each digit into one single char
so is it possible the count be two digits or more (e.g., 12 or 100)? If yes, I need to deal with multiple digits and write each digit separately as characters
3.是否保证 char array 有足够空间？是否会发生
  一般默认「压缩后不会超过原长度」 when compressing, we write fewer characters than cnt
, in the cnt ≤ k case we write exactly cnt characters, and in the cnt > k case we write fewer characters than cnt (assuming the compressed form fits), so write won’t catch up to read.

4.k 的边界 the bound of k
  k = 1？k >= n？


'''
#curr is the start char of one section of consecutive part
from typing import List

# `curr` is the leading character starting the current run (run =maxi consecutive segment of identical characters).
def compress_with_k(chars: List[str], k: int) -> int:
    read = 0
    write = 0
    n = len(chars)

    while read < n:
        # 1. count the number of consecutive identical characters
        start = read  # first record the position and the start character of this run
        curr = chars[read]
        
        # iterate through the char array to check whether each character is equal to the start character
        while read < n and chars[read] == curr:
            read += 1

        cnt = read - start  # consecutive length = (read - 1) - start + 1

        # 2. according to the count, decide how to write
        if cnt <= k:
            # write original characters
            # deal with the consecutive part starting at `start`;
            # the write pointer writes exactly `cnt` times
            for _ in range(cnt):
                chars[write] = curr
                write += 1
        else:
            # write compressed form
            chars[write] = curr
            write += 1  # move the pointer to write the digits
            
            # if the count has multiple digits (e.g., cnt = 15), write each digit separately: '1', '5'
            for digit in str(cnt):
                chars[write] = digit
                write += 1

    # return the new valid length of the array
    return write  # return chars[:write]  return the valid part is chars[:write]

