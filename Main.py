#insertion sort
def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i] 
		j = i-1
		while j >= 0 and key < arr[j] : 
			arr[j+1] = arr[j] 
			j -= 1
		arr[j+1] = key
	return arr

#binary search for index of x
def binary_search(arr, x): 
	low = 0
	high = len(arr) - 1
	mid = 0
	
	while low <= high: 
  	
		mid = (high + low) // 2
		
		if arr[mid] < x: 
			low = mid + 1
			
		elif arr[mid] > x: 
			high = mid - 1
			
		else:
            		return mid 
	return -1

numSoap = int(input())
soapCost = []
inputCost = input().split(" ")

for i in range(numSoap):
	soapCost.append(int(inputCost[i]))

soapCost = insertionSort(soapCost)

q = int(input())

for Q in range(q):
	cost = int(input())
	while cost > 0:
		index = binary_search(soapCost, cost)
		print(index, "hi", cost)
		if index < 0:
			cost -= 1
		else:
			print(index + 1)
			cost = 0
