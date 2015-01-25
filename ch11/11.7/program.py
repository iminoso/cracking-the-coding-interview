from sys import argv

def qsort(arr):
	smaller = []
	middle = []
	greater = []

	if len(arr) > 1:
		pivot = arr[0]
		for i in arr:
			if i < pivot:
				smaller.append(i)
			elif i == pivot:
				middle.append(i)
			else:
				greater.append(i)
		return qsort(smaller) + middle + qsort(greater)
	else:
		return arr

def findLongestSquence(pairs):
	startIndex = 0
	endIndex = 0

	for i in range(0, len(pairs)):
		secondNum = pairs[i][1]
		smallest = pairs[startIndex][1]
		greatest = pairs[endIndex][1]
		
		if secondNum < smallest:
			startIndex = i
			endIndex = startIndex + 1
		elif secondNum > greatest:
			endIndex = i

	return pairs[startIndex:endIndex]

def main():
	script, filename = argv
	lines = []
	with open(filename) as f:
		lines = f.readlines()

	pairs = lines[0].replace("(", "").replace(")" , "").split(' ')
	paired_arr = {}
	first_arr = []
	for pair in pairs:
		first_arr.append(pair.split(',')[0])
		paired_arr[pair.split(',')[0]] = (pair.split(',')[1])
	
	first_arr = qsort(first_arr)
	first_sorted = []
	
	for i in first_arr:
		first_sorted.append( [int(i), int(paired_arr[i])] )

	output = ""
	for pair in findLongestSquence(first_sorted):
		output += "(" + str(pair[0]) + "," + str(pair[1]) + ") "

	print(output)
	
if __name__ == "__main__":
    main()

