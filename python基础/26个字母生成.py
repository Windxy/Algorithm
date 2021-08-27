Char_list = [chr(i) for i in range(ord("A"),ord("Z")+1)]
print(Char_list)

dicts = {chr(i): i-ord('A')+1 for i in range(ord('A'), ord('Z') + 1)}
print(dicts)
