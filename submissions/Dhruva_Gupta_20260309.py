
s="RaMA  rAo"
ans=""
for ch in s:
    if(ch=='A' or ch=='a' or ch=='E' or ch=='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='u' or ch=='U'):
        ch=ch.upper()
        if(ch not in ans):
            ans=ans+ch
print(ans)
