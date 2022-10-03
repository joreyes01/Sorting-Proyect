#[4.8.2.6.0.5.2]

#O(n2) Complexity
def bbubleSort (inputList) :
    #Traverse through all List elements
    for i in range(0, len(inputList)):
        #Last i elements are already in place (Greater than)
        for j in range(1, len(inputList-i-1)):
            #Replace elements if the element is greater
            #than the next element
            if inputList[i] > inputList[j]:
                inputList[i], inputList[j] = inputList[j], inputList[i]
    #return the sorted List
    graphTime()
    return inputList

def selectionSort (inputList) :
    for i in range(0, len(inputList)):
        k = i
        for j in range(i+1, len(inputList)):
            if inputList[k] > inputList[j]:
                k=j

#Additional
def swap(A, i, j):
    #Helper function to swap elements i and j of list A.

    if i != j:
        A[i], A[j] = A[j], A[i]

def insertionSort(A):
    # In-place insertion sort.
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            swap(A, j, j - 1)
            j -= 1
            yield A

def mergeSort(A, start, end):
    #Merge sort.

    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergeSort(A, start, mid)
    yield from mergeSort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A

def merge(A, start, mid, end):
    #Helper function for merge sort.
    
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A

def quickSort(A, start, end):
    #In-place quicksort.

    if start >= end:
        return

    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quickSort(A, start, pivotIdx - 1)
    yield from quickSort(A, pivotIdx + 1, end)

def selectionsort(A):
    #In-place selection sort.
    if len(A) == 1:
        return

    for i in range(len(A)):
        # Find minimum unsorted value.
        minVal = A[i]
        minIdx = i
        for j in range(i, len(A)):
            if A[j] < minVal:
                minVal = A[j]
                minIdx = j
            yield A
        swap(A, i, minIdx)
        yield A

#TODO: Verify list type for derive request
# Check Complexity
def checkSorting():
    pass

#TODO: Bokeh library to plot time Complex
def graphTime():
    pass

if __name__ == "__main__":
    # Get user input to determine range of integers (1 to N) and desired
    # sorting method (algorithm).
    NIntegers = int(input("Enter number of integers: "))
    method_msg = "Enter sorting method:\n(b)ubble\n(i)nsertion\n(m)erge \
        \n(q)uick\n(s)election\n"
    method = input(method_msg)


