# python---click

click模块用于创建命令行界面，处理参数  

官方文档: https://click.palletsprojects.com/en/7.x/  

官方简单示例:  
```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
```


2019/12/24  
