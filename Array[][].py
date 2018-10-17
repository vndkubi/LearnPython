#Use Array[][]

XY = input("Input your X, Y and between two number with ',': ")
dismensions = [int(x) for x in XY.split(",")]

rowNumber = dismensions[0]
colNumber = dismensions[1]

#Create array[X][Y] with 0
multi = [[0 for col in range(colNumber)] for row in range(rowNumber)]

for row in range(rowNumber):
	for col in range(colNumber):
		multi[row][col] = row * col
	print(multi[row])

print(multi)