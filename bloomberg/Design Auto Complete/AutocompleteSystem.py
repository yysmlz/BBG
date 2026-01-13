'''
node[char]  →  child_node {}
We use a Trie to store all historical sentences and their frequencies.
when user types each character, we move a cursor in the trie to the corresponding prefix 
and perform DFS to collect all historical sentences sarting from the searched prefix
and return the top three sentences with the maxi frequency.

A trie node is represented as a dictionary that maps characters to child nodes, 
and uses a special '#' key to store the sentence frequency if a sentence ends at that node.

Clarify:
1.the parameter of input() is the single character? 
2.Can I assume that each input character is either a lowercase letter, a space, or #
Can I assume all input characters are within the ASCII range, and only # hash symbol has special meaning, which is end-of-input marker?
3.Should spaces be treated as valid characters in the trie? / Are sentences case-sensitive, or can I assume all input is lowercase
4.for the ranking,it is based on descending frequency, and then lexicographical (ASCII) order — is that correct?
5.特殊情况：the character and prefix typing is not in the trie:
if the user types a prefix that does not exist in history, should the system return an empty list?
and it allows continuing input and saving it as a new sentence until # is entered
'''
from typing import List

class AutocompleteSystem:
#self.node acts as a cursor in the trie. During initialization it's reset to the root
#and during user input, self.node moves along the trie to track the current prefix state.
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        for i,sentence in enumerate(sentences): #the ith sentence
            node = self.trie #node 重新从 root 开始build trie 

            for c in sentence: #iterate through each char in one sentence
                if c not in node: 
                    node[c] = {} 
                node = node[c] #node move forward to the child node
            node["#"] = times[i] #mark the end with endnode dict{'#':times}, whose key is #,value is times 
        
        self.node = self.trie #node回到一开始{}，用来搜索       
        self.prefix = []
    
    def input(self, c: str) -> List[str]:
#1.if #, we update the cnt of sentence
        if c == "#":
            if "#" in self.node: #the end mark # is in the child node, it means the sentence already exists in the trie
                self.node["#"] += 1 
            else: 
                self.node["#"] = 1
            self.prefix = []  #clear the prefix
            self.node = self.trie #reset the node to the root
            return []
#2.if the char inputted, find this prefix node in the trie, if not, we add a new    
        if c not in self.node: #不在就往self.node这个dict{}中,插入item char:node #if the char is not in the node, insert it
            self.node[c] = {} # 在self.node这个大dict{}, 中插入元素[c]:{node}
        self.node = self.node[c] #move forward node
        self.prefix.append(c)
#3.find all outgoing paths from the current node to the end of sentences.        
        ans = []
        self.dfs(self.node,self.prefix,ans) #gain all paths starting from the prefix searched
        ans.sort(key=lambda x:(-x[0],x[1])) #sort candidate sentences by descending frequency and lexicographical order
        return [x[1] for x in ans][:3] # return the top three sentence strings.

#DFS traverses all paths under the current prefix node and gathers all valid sentences for autocomplete.
    def dfs(self,node,prefix,ans):
        for k in node: #iterate through all key,the character,in the child node dictinary(if node={},the childnode is newly added,there is no operation on ans, just return ans=[])
            if k != "#": 
                prefix.append(k)  #append the character to the prefix
                self.dfs(node[k],prefix,ans) #recursively explore the child node
                prefix.pop() #backtrack to restore the prefix state.
            else:
                ans.append([node["#"],"".join(prefix)])

'''
ans = [
  [5, "i love you"],
  [3, "island"],
  [2, "iroman"],
  [2, "i love leetcode"]
]

'''
  


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)