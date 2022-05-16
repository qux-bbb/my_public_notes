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
			"    print(\"${0:Hello World}\")",
			"",
			"",
			"if __name__ == \"__main__\":",
			"    main()",
			""
		],
		"description": "Write a python Hello World"
	},
	"Python open file read": {
		"prefix": "openr",
		"body": [
			"the_file = open(\"${0:hello.txt}\", \"r\")",
			"the_content = the_file.read()",
			"the_file.close()"
		],
		"description": "Python open file read"
	},
	"Python open file write": {
		"prefix": "openw",
		"body": [
			"the_file = open(\"${1:hello.txt}\", \"w\")",
			"the_file.write(${0:the_content})",
			"the_file.close()"
		],
		"description": "Python open file write"
	}
```

还是很方便的  

官方文档: https://code.visualstudio.com/docs/editor/userdefinedsnippets  


2020/3/12  
