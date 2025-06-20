lab = [
    [1,1,1,3,0,1,1,1,4],
    [3,0,0,1,0,1,0,0,1],
    [1,1,0,1,1,1,1,0,1],
    [0,1,0,1,0,0,1,0,1],
    [1,1,1,1,1,1,3,1,1],
    [3,0,1,0,0,0,1,0,1],
    [1,1,1,1,3,1,1,1,1],
    [1,0,0,1,0,1,0,0,4],
    [1,1,3,1,0,1,1,1,1],
]

n = len(lab)
camino = [[0]*n for _ in range(n)]
dirs = [(-1,0),(0,1),(1,0),(0,-1)]
found = False

def bt(i, j, s):
    global found
    if found: return
    if i<0 or i>=n or j<0 or j>=n or lab[i][j]==0 or camino[i][j]: return
    s += lab[i][j]
    camino[i][j] = 1
    if (i, j) == (0, 0):
        if s >= 23:
            found = True
        else:
            camino[i][j] = 0
        return
    for di, dj in dirs:
        bt(i+di, j+dj, s)
        if found: return
    camino[i][j] = 0

bt(n-1, 0, 0)

print("Laberinto original:")
for i in range(n):
    row = []
    for j in range(n):
        if (i, j) == (0, 0):
            row.append("F")
        elif (i, j) == (n-1, 0):
            row.append("I")
        else:
            row.append(str(lab[i][j]))
    print(" ".join(row))

if found:
    print("¡Se logró un camino viable con ≥23 puntos!")
else:
    print("No existe camino viable que reúna ≥23 puntos.")

print("Matriz de camino:")
for fila in camino:
    print(" ".join(str(x) for x in fila))
