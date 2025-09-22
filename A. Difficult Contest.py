t = int(input())

for _ in range(t):
    s = str(input())
    s = s.replace("FFT", "FTF")
    s = s.replace("NTT", "NTF")
    print(s)