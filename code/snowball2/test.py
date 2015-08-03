a = [[1,2],[3,2],[5,2],[3,7]]
for aa in a[:]:
    if aa[0] == 3:
        a.remove(aa)
print a