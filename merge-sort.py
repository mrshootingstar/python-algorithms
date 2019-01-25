'''
Extensions:
================
Bottom-up merge sort
================
Faster merge. Implement a version of merge() that copies the second half of a[] to aux[] in decreasing order and then does the merge back to a[]. This change allows you to remove the code to test that each of the halves has been exhausted from the inner loop. Note: the resulting sort is not stable.
================
Improvements. Write a program MergeX.java that implements the three improvements to mergesort that are described in the text: add a cutoff from small subarrays, test whether the array is already in order, and avoid the copy by switching arguments in the recursive code.
================
Inversions. Develop and implement a linearithmic algorithm Inversions.java for computing the number of inversions in a given array (the number of exchanges that would be performed by insertion sort for that array—see Section 2.1). This quantity is related to the Kendall tau distance; see Section 2.5.
================
Index sort. Develop a version of Merge.java that does not rearrange the array, but returns an int[] perm such that perm[i] is the index of the ith smallest entry in the array.
'''

class MergeSort:
    def __init__(self, arr):
        self.arr = arr
        self.aux = [None] * len(arr)
        
    def sort(self):
        self.sort_util(0, len(self.arr)-1)
        return self.arr

    def merge(self, lo, mid, hi):
        for k in range(lo, hi+1):
            self.aux[k] = self.arr[k]

        i, j = lo, mid+1
        for k in range(lo, hi+1):
            if i > mid:
                self.arr[k] = self.aux[j]
                j += 1
            elif j > hi:
                self.arr[k] = self.aux[i]
                i += 1
            elif self.aux[i] < self.aux[j]:
                self.arr[k] = self.aux[i]
                i += 1
            else:
                self.arr[k] = self.aux[j]
                j += 1

    def sort_util(self, lo, hi):
        if lo >= hi:
            return

        mid = lo + (hi-lo)//2
        self.sort_util(lo, mid)
        self.sort_util(mid+1, hi)
        self.merge(lo, mid, hi)