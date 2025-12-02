
data = open("input.txt").read().split(",")
ans = 0

for line in data:
    (start, end) = line.split("-",2)
    
    for i in range(int(start),int(end)+1):
        s = str(i)
        l = len(s)
        
        if l%2 != 0:
            continue;
        
        h = l//2
        
        if s[:h] == s[h:]:
            ans += i
            
print(ans)
            
