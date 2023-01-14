keypad_alphabets = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
alpha_key_values = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]

inputString = "bsve"
outputString = ""

for i in range(len(inputString)):
    ch = inputString[i]
    idx = ord(ch) - ord('a')
    key = alpha_key_values[idx]
    keypad_str = keypad_alphabets[key]
    for j in keypad_str:
        if j != ch:
            outputString += str(key)
        else:
            outputString += str(key)
            break
    
print(outputString)
