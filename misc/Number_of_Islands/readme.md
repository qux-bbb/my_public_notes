# Number of Islands

## 题目
Given a 2d grid map of ‘1’s (land) and ‘0’s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.  
Example 1：
```r
11110
11010
11000
00000
```
Answer: 1  

Example 2: 
```r
11000
11000
00100
00011
```
Answer：3  

## 思路
思路很简单，在访问一个是'1'的点之后，修改其为'2'或者别的字符，然后再看周围是否为'1'，这样所有判断之后，就会确定一个岛  
之前想过是不是可以只判断下边和右边，这样会简化很多，但是发现自己想错了，比如这种情况：
```r
111111
000100
010100
011100
```
如果只判断下边和右边，结果是2个岛，但其实是1个

## 代码
```java
public class Main {
	
	static int NumOfIslands(char[][] grid){
		int count = 0;
		for(int i = 0; i < grid.length; i++){
			for(int j = 0; j < grid[0].length; j++){
				if(grid[i][j] == '1'){
					Search(grid , i, j);
					count++;
				}
			}
		}
		return count;
	}

	static void Search(char[][] grid, int i, int j){
		
		// 超出边界或者不是 '1'，直接返回
		if(i < 0 || i >= grid.length || j < 0 ||  j >= grid[0].length || grid[i][j] != '1')
			return;
		grid[i][j] = '2';
		Search(grid, i-1, j); // 上边
		Search(grid, i+1, j); // 下边
		Search(grid, i, j-1); // 左边
		Search(grid, i, j+1); // 右边
	}
	
	public static void main(String[] args) {
			char a[][] = {{'1','1','1','1','0'},
					{'1','1','0','1','0'},
					{'1','1','0','0','0'},
					{'0','0','0','0','0'}};
			char b[][] = {{'1','1','0','0','0'},
					{'1','1','0','0','0'},
					{'0','0','1','0','0'},
					{'0','0','0','1','1'}};
			char c[][] = {{'1','1','1','1','1','1'},
					{'0','0','0','1','0','0'},
					{'0','1','0','1','0','0'},
					{'0','1','1','1','0','0'}};
			System.out.println(NumOfIslands(a));
			System.out.println(NumOfIslands(b));
			System.out.println(NumOfIslands(c));
	}

}
```


2017/9/20  
