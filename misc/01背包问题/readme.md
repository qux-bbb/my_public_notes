# 01背包问题

## 简介

01背包问题的解释可以看百度百科[01背包问题](https://baike.baidu.com/item/01%E8%83%8C%E5%8C%85/4301245)  

只输出最终背包重量：  
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/  

输出每个物品的信息：  
https://www.geeksforgeeks.org/printing-items-01-knapsack/  


## 只获取最终重量和价值
下面这个方法只能求出最后背包中物品的总重量和总价值，无法求出放入背包的每个物品，如果需要求后者，需要使用二维数组。  

自己不太懂，不过看这个代码好像有点理解的意思了，就先收藏一下代码吧  

```cpp
/********************************************************/
/*背包问题：有m件物品和一个承重为t的背包。              */
/*          第i件物品的重量是w[i]，价值是v[i]。         */
/*          求解将哪些物品装入背包可使这些物品的        */
/*          重量总和不超过背包承重量t，且价值总和最大。 */
/********************************************************/

/* 变量对应，这样有意义一些，看起来很舒服
m --- count
t --- max_weight
w[i] --- weight[i]
v[i] --- value[i]
*/

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>


int total_value[1010]; // 记录不同承重量背包的总价值
int weight[1010]; // 记录不同物品的重量
int value[1010]; // 记录不同物品的价值


//返回x,y的最大值
int max(int x, int y)
{
    if (x > y)
        return x;
    return y;
}


int main()
{
    int max_weight; // 背包的最大承重量
    int actual_weight; // 背包实际承重
    int count; // 物品的数量
    int i, j; // 临时变量

    memset(total_value, 0, sizeof(total_value));  //总价值初始化为0
    printf("请输入背包承重量 物品的数量：\n");
    scanf("%d %d", &max_weight, &count);  //输入背包最大承重量max_weight、物品的数目count
    printf("请输入每件物品的重量 价值：\n");
    for (i = 1; i <= count; i++)
        scanf("%d %d", &weight[i], &value[i]);  //输入count组物品的重量weight[i]和价值value[i]

    //尝试放置每一个物品
    //在放入第i个物品前后，检验不同j承重量时，背包的总价值
    //如果放入第i个物品后比放入前的价值提高了，则修改j承重量背包的价值，否则不变
    for (i = 1; i <= count; i++)
        for (j = max_weight; j >= weight[i]; j--)
            total_value[j] = max(total_value[j - weight[i]] + value[i], total_value[j]);

    // 获取背包的实际承重
    for (actual_weight = max_weight; actual_weight > 0; actual_weight--)
        if (total_value[actual_weight] != total_value[actual_weight - 1])
            break;

    printf("背包最终重量 价值\n");
    printf("%d %d\n", actual_weight, total_value[actual_weight]);
    getchar();
    return 0;
}
```


以下为三组测试数据  
```r
请输入背包承重量 物品的数量：
10 3
请输入每件物品的重量 价值：
1 2
8 3
5 6
背包最终重量 价值
6 8
```

```r
请输入背包承重量 物品的数量：
20 5
请输入每件物品的重量 价值：
5 10
25 40
12 8
10 10
15 2
背包最终重量 价值
15 20
```

```r
请输入背包承重量 物品的数量：
7 4
请输入每件物品的重量 价值：
1 1
3 4
4 5
5 7
背包最终重量 价值
7 9
```


## 可输出每个装入物品的数据（python）
把 https://www.geeksforgeeks.org/printing-items-01-knapsack/ 的python版本稍微改造一下，可以输出总的信息和每个物品的信息。  
代码如下：  
```python
# coding: utf8

# Python3 code for Dynamic Programming 
# based solution for 0-1 Knapsack problem 
  
# Prints the items which are put in a  
# knapsack of capacity W 
def printknapSack(W, wt, val, n): 
    K = [[0 for w in range(W + 1)] 
            for i in range(n + 1)] 
              
    # Build table K[][] in bottom 
    # up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i - 1] <= w: 
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]) 
            else: 
                K[i][w] = K[i - 1][w] 
  
    # stores the result of Knapsack 
    res = K[n][W]
    print('final knapsack\' weight value:')
    print(K[n].index(res), res)

    if not res:
        return
      
    print('items packed in knapsack "weight value":')
    w = W 
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        # either the result comes from the 
        # top (K[i-1][w]) or from (val[i-1] 
        # + K[i-1] [w-wt[i-1]]) as in Knapsack 
        # table. If it comes from the latter 
        # one/ it means the item is included. 
        if res == K[i - 1][w]: 
            continue
        else: 
  
            # This item is included. 
            print(wt[i - 1], val[i-1]) 
              
            # Since this weight is included 
            # its value is deducted 
            res = res - val[i - 1] 
            w = w - wt[i - 1] 


val = []
wt = []
W = int(input('please input capacity of Knapsack: '))
n = int(input('please input number of items: '))
print('please input each item\' weight value: ')
for i in range(n):
    weight, value = input('{}: '.format(i+1)).strip().split()
    wt.append(int(weight))
    val.append(int(value))
      
printknapSack(W, wt, val, n) 
  
# This code is contributed by Aryan Garg.
```


以下为三组测试数据  
```r
please input capacity of Knapsack: 10
please input number of items: 3
please input each item' weight value:
1: 1 2
2: 8 3
3: 5 6
final knapsack' weight value:
6 8
items packed in knapsack "weight value"
5 6
1 2
```

```r
please input capacity of Knapsack: 20
please input number of items: 5
please input each item' weight value:
1: 5 10
2: 25 40
3: 12 8
4: 10 10
5: 15 2
final knapsack' weight value:
15 20
items packed in knapsack "weight value"
10 10
5 10
```

```r
please input capacity of Knapsack: 7
please input number of items: 4
please input each item' weight value:
1: 1 1
2: 3 4
3: 4 5
4: 5 7
final knapsack' weight value:
7 9
items packed in knapsack "weight value"
4 5
3 4
```


---
2019/3/5  
