s = 'adasdadasdjgavsbn'

sub= ""
submax = ""

for i in range(0, len(s)-1):
    if sub == "":
        sub = s[i] + s[i+1]

    else:
        sub= s[i]+s[i+1]

    elif s[i] > s [i+1]:
        sub=""
    if len(sub) > len(submax):
        submax = sub

print(submax)



