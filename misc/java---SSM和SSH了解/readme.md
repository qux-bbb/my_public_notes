# java---SSM和SSH了解

## SSM
**SSM:Spring + SpringMVC + MyBatis**  
常作为数据源较简单的web项目的框架
* **Spring**：轻量级的控制反转(IoC)和面向切面(AOP)的容器框架。  
    * **控制反转**：Inversion of Control：用配置文件(XML)来描述类与类之间的关系，由容器来管理，降低了程序间的耦合度，程序的修改可以通过简单的配置文件修改来实现
    * **面向切面**：Aspect Oriented Programming：散布于应用中多处的功能(日志、安全、事务管理等)被称为横切关注点，把横切关注点与业务逻辑分离是AOP要解决的问题
* **SpringMVC**：分离了控制器、模型对象、分派器以及处理程序对象的角色，这种分离让它们更容易进行定制。
* **MyBatis**：支持普通SQL查询，存储过程和高级映射的优秀持久层框架  

## SSH
**SSH:Struts + Spring + Hibernate**  
1. **Struts**进行流程控制
2. **Spring**进行业务流转
3. **Hibernate**进行数据库操作的封装


---
2017/9/21  
