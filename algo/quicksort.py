# Do one quick sort run, then run quicksort left of pivot and right of pivot - repeat
# You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length m, you should simply add m−1 to your running total of comparisons.


def quicksort(list1):
    
    if len(list1)==1: #base case
        return list1
    pivot=list1[0]
    
