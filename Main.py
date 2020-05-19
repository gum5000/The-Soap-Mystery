# Python program for implementation of MergeSort 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

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
	return -(mid + 2)

numSoap = int(input())
soapCost = []
inputCost = input().split(" ")

for i in range(numSoap):
	soapCost.append(int(inputCost[i]))

mergeSort(soapCost)

q = int(input())

for Q in range(q):
	cost = int(input()) - 1
	
	if cost < soapCost[0]:
		print(0)
	elif cost > soapCost[numSoap - 1]:
		print(numSoap)
	else:
		index = binary_search(soapCost, cost)
		if index < 0:
			index = index * -1
			if index >= numSoap:				
				index = numSoap - 1
			while cost < soapCost[index]:
				index -= 1
		else:
			if index + 1 < numSoap:
				while cost >= soapCost[index + 1]:
					if index + 2 < numSoap:
						index += 1
					else:
						break
		print(index + 1)
