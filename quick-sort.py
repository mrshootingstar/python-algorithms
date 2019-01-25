class Quick:
    def sort(self, arr):
        lo, hi = 0, len(arr)-1
        self.sort_util(arr, lo=lo, hi=hi)

    def partition(self, arr, lo, hi):
        border = lo
        pivot = arr[hi]
        for i in range(lo, hi):
            if arr[i] < pivot:
                arr[border], arr[i] = arr[i], arr[border]
                border += 1
        arr[hi], arr[border] = arr[border], arr[hi]
        return border 

    def sort_util(self, arr, lo, hi):
        if hi <= lo: return
        split_point = self.partition(arr, lo, hi)
        self.sort_util(arr, lo=lo, hi=split_point-1)
        self.sort_util(arr, lo=split_point+1, hi=hi)

a = [1,1,1,1,0,-1,-2]
q = Quick()
q.sort(a)
print(a)