# vscode---snippets

vscode有一个`代码片段`功能, 类似pycharm的代码模板(code Templates)  

文件->首选项->用户代码片段, 然后可以开始创建自己的代码片段  

这是我创建的一个python初始化片段:  
```r
	"Python initial template": {
		"prefix": "hello",
		"body": [
			// "#!/usr/bin/env python",
			"# coding:utf8",
			"\"\"\"",
			"@author: qux",
			"@file: $TM_FILENAME",
			"@time: $CURRENT_YEAR/$CURRENT_MONTH/$CURRENT_DATE",
			"\"\"\"",
			"",
			"",
			"def main():",
			"    print('${0:Hello World}')",
			"",
			"",
			"if __name__ == '__main__':",
			"    main()"
		],
		"description": "Write a python Hello World"
	},
	"Python open file": {
		"prefix": "open",
		"body": [
			"the_file = open('${0:hello.txt}', 'r')",
			"the_content = the_file.read()",
			"the_file.close()"
		],
		"description": "Write a python Hello World"
	}
```

还是很方便的  

官方文档: https://code.visualstudio.com/docs/editor/userdefinedsnippets  


2020/3/12  
