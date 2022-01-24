# python3---argparse

argparse用于设计、解析命令行参数。  

官方文档: https://docs.python.org/3/library/argparse.html  

一个求和示例：  
```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```


2019/12/1  
