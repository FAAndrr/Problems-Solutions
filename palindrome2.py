char = list(str(input()).strip())
for i in range(len(char)//2):
    j = len(char) - 1 - i
    char[i] = char[j] = min(char[i], char[j])  
print("".join(char))