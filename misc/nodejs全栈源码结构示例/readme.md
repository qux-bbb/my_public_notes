# nodejs全栈源码结构示例

## 前端源码结构示例
```r
.
├── App.css
├── App.js  // 主要文件，组织各个组件
├── components  // 各种组件
│   ├── Blog.test.js
│   ├── BlogForm.js
│   ├── Blogs.js
│   ├── CommentForm.js
│   ├── Notification.js
│   ├── Togglable.js
│   └── Users.js
├── index.js  // 入口
├── reducers  // 保存各种全局状态
│   ├── blogReducer.js
│   ├── currentUserReducer.js
│   ├── notificationReducer.js
│   └── userReducer.js
├── services  // 通过axios请求后端api接口
│   ├── blogs.js
│   ├── login.js
│   └── users.js
├── setupTests.js
└── store.js  // 整合全局状态
```
可以用cypress测试，很好用  

## 后端源码结构示例
```r
.
├── app.js  // 主要文件，连接数据库，整个各种中间件
├── controllers  // 负责各种路由处理
│   ├── blogs.js
│   ├── login.js
│   ├── testing.js
│   └── users.js
├── index.js  // 使用app.js等，开启服务
├── jest.config.js
├── models  // 数据结构定义，数据库相关
│   ├── blog.js
│   └── user.js
├── package-lock.json
├── package.json
├── test.rest
├── tests  // 测试文件，用的是jest
│   ├── blog_api.test.js
│   ├── list_helper.test.js
│   └── test_helper.js
└── utils  // 一些零碎的功能函数
    ├── config.js
    ├── list_helper.js
    ├── logger.js
    └── middleware.js
```


---
2020/11/10  
