# python---快速排序

注：代码是百度百科的  
## 代码
```python
# quick sort
def quickSort(L, low, high):
	i = low
	j = high
	if i >= j:
		return
	key = L[i]
	while i < j:
		while i < j and L[j] >= key: # 从后向前找比key小的值
			j-=1
		L[i] = L[j] # 把比key小的值移到key在的位置
		while i < j and L[i] <= key: # 从前向后找比key大的值
			i+=1
		L[j] = L[i] # 把比key大的值移到刚找出的比key小的值的位置
	L[i] = key  # 这时的i左右分别为比key小和大的值，key移到i处
	quickSort(L, low, i-1) # 继续排前一部分
	quickSort(L, j+1, high) # 继续排后一部分
	return
```

## 测试用例
```r
a = [4, 5, 3, 12, 43, 1, 0, 34]
quickSort(a, 0, len(a) - 1)
print(a)
```

## 结果
```r
[0, 1, 3, 4, 5, 12, 34, 43]
```

## 最好和最坏情况
最好：key每次都能使序列均匀划分，时间复杂度为O(nlogn)  
最坏：key为最大或最小数字，时间复杂度为O(n^2)  


---
2017/9/16  
