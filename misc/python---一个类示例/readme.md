# python---一个类示例

```python
# coding:utf8


class Employee:
    """所有员工的基类"""

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


# 创建 Employee 类的第一个对象
emp1 = Employee("Zara", 2000)
# 创建 Employee 类的第二个对象
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

print("Doc: %s" % Employee.__doc__)
```

结果：  
```r
Name :  Zara , Salary:  2000
Name :  Manni , Salary:  5000
Total Employee 2
Doc: 所有员工的基类
```


2017/11/10  
