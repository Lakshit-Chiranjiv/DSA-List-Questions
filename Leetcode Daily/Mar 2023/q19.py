class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                current_node.children[character] = TrieNode()
            current_node = current_node.children[character]
        current_node.is_word = True
        
    def search(self, word):
        def dfs(root, index):
            curr = root

            for i in range(index,len(word)):
                ch = word[i]
                
                if ch == '.':
                    for child in curr.children.values():
                        if dfs(child,i + 1):
                            return True
                    return False

                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
            return curr.is_word
    
        return dfs(self.root, 0)


# intuition:
# 1. A trie can be used to store the words in an efficient manner.
# 2. A trie is a tree data structure where each node represents a character in the word. One node can have multiple children. Each node can have a boolean variable to indicate if the word ends at that node.
# 3. A separate function can be used to perform the dfs search on the trie.
# 4. The dfs function can be used to search for the word in the trie by traversing the trie based on the characters in the word.
# 5. If the character is a '.', the function can be called recursively on all the children of the current node - backtracking.
# 6. If the character is not a '.', the function can be called recursively on the child corresponding to the character.
# 7. If the word is found, return True. Else, return False.

# solution
# 1. Create a trie node class with a dictionary to store the children and a boolean variable to indicate if the word ends at that node.
# 2. In the constructor of dictionary, create a root TrieNode object and assign it to the object.
# 3. Create a function to add a word to the trie. Create a current node variable and assign it to the root node. 
# 4. Iterate through the characters in the word. If the character is not in the children of the current node, create a new TrieNode object and assign it to the character in the children of the current node.
# 5. Assign the current node to the child corresponding to the character.
# 6. After the iteration, set the is_word variable of the current node to True to indicate that the word ends at that node.
# 7. Create a function to search for a word in the trie. Create a dfs function that takes the root node and the index of the character in the word as parameters.
# 8. Create a current node variable and assign it to the root node.
# 9. Iterate through the characters in the word starting from the index. If the character is a '.', iterate through the children of the current node. Call the dfs function recursively on each child and the index + 1. If the dfs function returns True, return True. Else, return False.
# 10. If the character is not a '.', check if the character is in the children of the current node. If not, return False. Else, assign the current node to the child corresponding to the character.
# 11. After the iteration, return the is_word variable of the current node.
# 12. Call the dfs function on the root node and 0 and return the result.