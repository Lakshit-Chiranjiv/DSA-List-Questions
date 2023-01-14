mp = {}
input_string = input()
for i in input_string:
    if i in mp:
        mp[i] += 1
    else:
        mp[i] = 1

for i in mp:
    if mp[i] > 1:
        print(i, mp[i])