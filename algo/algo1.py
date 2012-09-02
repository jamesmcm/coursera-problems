
inversions=0
def mergeSort(array):

    global inversions
    if len(array)==1:
        return array
    elif len(array)>1:
        array1=mergeSort(array[0:(len(array)/2)])
        array2=mergeSort(array[(len(array)/2):len(array)])
        #print array1, array2
        array=merge(array1, array2)
        return array




def merge(array1, array2):
    global inversions
    i=0
    j=0
    array=[]
    while i<len(array1) or j<len(array2):
        if i >= len(array1):
            array.append(array2[j])
            j+=1
        elif j>=len(array2):
            array.append(array1[i])
            i+=1
        
        else:
            if array1[i]<=array2[j]:
                array.append(array1[i])
                i+=1
            else:
                array.append(array2[j])
                inversions+=(len(array1)-i)
                j+=1
    #print "merge:" + str(array )
    return array

#array=[10,9,8,7,6,5]
#print mergeSort(array)
file1=open("IntegerArray.txt","r")
list1=file1.readlines()
list2=[]
for item in list1:
    list2.append(int(item.strip("\r\n")))

mergeSort(list2)

print inversions

