txt = "ABCDXYZABCDEFGHIJABCD"
pat = "ABCD"

M , N = len(pat) , len(txt)

i , j , th , ph = 0 , 0 , 0 , 0
h = 1 # power ... at the ith index --> for subtraction
d = 256 # character size
q = 97 # big prime
res = []

for i in range(M-1):
    h = ( h * d ) % q

for i in range(M):
    th = ( d * th + ord(txt[i])) % q
    ph = ( d * ph + ord(pat[i])) % q

for i in range(N-M+1):
    if ph == th:
        if txt[i:i+M] == pat:
            res.append(i)
    if i < N - M:
        th = ( d*(th - ord(txt[i]) * h ) + ord(txt[i+M])) % q
        if th < 0:
            th += q


print(f"Occurences of {pat} in {txt} at indices --> {res}")
    