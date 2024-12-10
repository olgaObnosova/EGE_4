with open('27_B.txt') as f:
    sklad = [[float(robot.replace(',', '.')) for robot in line.split()] for line in f]
klaster1=[robot for robot in sklad if robot[0] > 18]
klaster2=[robot for robot in sklad if robot[0] < -12]
klaster3=[robot for robot in sklad if -9 < robot[0] < 15]
centroid1, S1 = None, float('inf')
for i in range(len(klaster1)):
    S=0
    for j in range(len(klaster1)):
        if i==j:
            continue
        x1, y1 = klaster1[i]
        x2, y2 = klaster1[j]
        S+=abs(x2 - x1)+abs(y2 - y1)
    if S<S1:
        centroid1=klaster1[i]
        S1=S

centroid2, S2 = None, float('inf')
for i in range(len(klaster2)):
    S = 0
    for j in range(len(klaster2)):
        if i == j:
            continue
        x1, y1 = klaster2[i]
        x2, y2 = klaster2[j]
        S += abs(x2 - x1) + abs(y2 - y1)
    if S < S2:
        centroid2 = klaster2[i]
        S2 = S
centroid3, S3 = None, float('inf')
for i in range(len(klaster3)):
    S = 0
    for j in range(len(klaster3)):
        if i == j:
            continue
        x1, y1 = klaster3[i]
        x2, y2 = klaster3[j]
        S += abs(x2 - x1) + abs(y2 - y1)
    if S < S3:
        centroid3 = klaster3[i]
        S3 = S
print(klaster2)
px=((centroid1[0]+centroid2[0]+centroid3[0])/3)*1000
py=((centroid1[1]+centroid2[1]+centroid3[1])/3)*1000
print(px, py)