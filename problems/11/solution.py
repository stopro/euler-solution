#/usr/bin/python
matrix = []
with open('source.txt') as f:
    read_data = f.readline()
    while read_data != '':
        row = [int(x) for x in read_data[:-1].split(' ')]
        row.append(1)
        row.append(1)
        row.append(1)
        row.insert(0,1)
        row.insert(0,1)
        row.insert(0,1)
        matrix.append(row)
        read_data = f.readline()
f.closed

nop = [1 for x in range(26)]
matrix.append(nop);
matrix.append(nop);
matrix.append(nop);
print(matrix)
MAX = 0
for i in range(20):
    for j in range(3,23):
        if matrix[i][j] == 0:
            continue;
        m1 = matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3]
        m2 = matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j]
        m3 = matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3]
        m4 = matrix[i+1][j-1] * matrix[i+2][j-2] * matrix[i+3][j-3]
        selected = max(m1,m2,m3,m4) * matrix[i][j]
        if (selected > MAX):
            MAX = selected

print(MAX)


def max(m1, m2, m3, m4):
    maximum = m1
    if (maximum < m2):
        maximum = m2
        
    if (maximum < m3):
        maximum = m3

    if(maximum < m4):
        maximum = m4
    
