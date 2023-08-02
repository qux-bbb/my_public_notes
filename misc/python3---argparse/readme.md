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

更多功能的示例：  
```python
# coding:utf8

import argparse
import os
import textwrap


def valid_path(the_path):
    if not os.path.exists(the_path):
        msg = f"{the_path} does not exist"
        raise argparse.ArgumentTypeError(msg)
    if not os.path.isfile(the_path):
        msg = f"{the_path} is not a file"
        raise argparse.ArgumentTypeError(msg)
    return the_path


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            """\
            A simple description

            Example:
                python %(prog)s download hello.txt -d 2222_folder -v
                python %(prog)s download hello.txt -v
            """
        ),
    )
    parser.add_argument("action", choices=["all", "download", "extract", "statistic"])
    parser.add_argument("src_path", type=valid_path, help="the source path")
    # "-"开头为可选项，可通过"required=True"设置为必选项
    parser.add_argument(
        "-d", "--dst_path", type=str, default="result_fodler", help="the result folder"
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="print more info")

    args = parser.parse_args()
    print(args)

    action = args.action
    src_path = args.src_path
    dst_path = args.dst_path
    verbose_flag = args.verbose

    # ...


if __name__ == "__main__":
    main()

```


2019/12/1  
