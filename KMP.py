n = "abcdxyzabcd" 
h = "sadabcdxyabcdxyzabcdzabcdabcdxyzabcd"

# KMP --> Amortized O(m+n) TC and O(m) space
M , N = len(n) , len(h)

# Longest prefix suffix / PI precalculation
def LPS(pattern):
    arr = [0 for _ in range(M)]
    cur = 1
    prefix = 0
    while cur < M:
        if pattern[cur] == pattern[prefix]:
            prefix += 1
            arr[cur] = prefix
            cur += 1
        else:
            if prefix == 0:
                cur += 1
            else:
                prefix = arr[prefix-1] # reset prefix to last matching prefix
    return arr

lps = LPS(n)  
print(f"Longest Prefix Suffix Array / PI for pattern : {n} --> {lps}")
hp , np = 0 , 0 # haystack pointer , needle pointer init
res = False
while hp < N:
    if h[hp] == n[np]:
        hp += 1
        np += 1
    else:
        if np == 0:
            hp += 1
        else:
            np = lps[np-1]
    if np == M:
        print(f"Pattern found at index : {hp-np}")
        res = True
        break

if not res:
    print("Pattern not Found")


"""
LPS ARRAY --> abcd xyz abcd --> [0,0,0,0,0,0,0,1,2,3,4]
abab xyz abab yyy --> [0,0,1,2,0,0,0,1,2,3,4,0,0,0]

"""

