from json import loads as l
def dfs(g, i, j):
    g[i][j] = "0"
    if i+1 < len(g) and g[i+1][j] == '1':
        g = dfs(g, i+1, j)
    if j+1 < len(g[i]) and g[i][j+1] == '1':
        g = dfs(g, i, j+1)
    if i-1 >= 0 and g[i-1][j] == '1':
        g = dfs(g, i-1, j)
    if j-1 >= 0 and g[i][j-1] == '1':
        g = dfs(g, i, j-1)
    return g

with open('user.out','w') as file:
    for g in stdin:
        g = l(g)
        if not g or not g[0]:
            file.write('0'+'\n')
        else:
            c = 0
            for i in range(len(g)):
                for j in range(len(g[i])):
                    if g[i][j] == "1":
                        c += 1
                        g = dfs(g, i, j)
            file.write(str(c)+'\n')
exit()