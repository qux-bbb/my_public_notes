# python---编写python扩展

一个C文件，创建方法和接口(Extest2.c)  
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int fac(int n)
{
    if (n < 2) return(1); /* 0! == 1! == 1 */
    return (n)*fac(n-1); /* n! == n*(n-1)! */
}


char *reverse(char *s)
{
    register char t,                    /* tmp */
            *p = s,                     /* fwd */
            *q = (s + (strlen(s)-1));   /* bwd */
    while (p < q)                       /* if p < q */
    {                                   /* swap & mv ptrs */
        t = *p;
        *p++ = *q;
        *q-- = t;
    }
    return s;
}


int test()
{
    char s[BUFSIZ];
    printf("4! == %d\n", fac(4));
    printf("8! == %d\n", fac(8));
    printf("12! == %d\n", fac(12));
    strcpy(s, "abcdef");
    printf("reversing 'abcdef', we get '%s'\n", reverse(s));
    strcpy(s, "madam");
    printf("reversing 'madam', we get '%s'\n", reverse(s));
    return 0;
}



#include "Python.h"

static PyObject * Extest_fac(PyObject *self, PyObject *args) { 
    int num;
    if (!PyArg_ParseTuple(args, "i", &num))
        return NULL;
    return (PyObject*) Py_BuildValue("i", fac(num));
}


static PyObject * Extest_doppel(PyObject *self, PyObject *args) {
    char * orig_str;        // original string
    char *dupe_str;         // reversed string
    PyObject* retval;

    if (!PyArg_ParseTuple(args, "s", &orig_str)) return NULL;
    retval  =(PyObject*) Py_BuildValue("ss", orig_str, dupe_str=reverse(strdup(orig_str)));
    free(dupe_str);
    return retval;
}


static PyObject * Extest_test(PyObject *self, PyObject *args) { 
    test();
    return (PyObject*) Py_BuildValue("");
}


static PyMethodDef ExtestMethods[] = {
    { "fac", Extest_fac, METH_VARARGS },
    { "doppel", Extest_doppel, METH_VARARGS },
    { "test", Extest_test, METH_VARARGS },
    { NULL, NULL },
}; 


void initExtest() {
    Py_InitModule("Extest", ExtestMethods);
} 
```


一个python文件，用于模块编译和安装(setup.py)  
```python
# coding:utf8

from distutils.core import setup, Extension

MOD = 'Extest'
setup(name=MOD, ext_modules=[
    Extension(MOD, sources=['Extest2.c'])
])
```


方法:  
linux下，安装了python  
2个文件放在一个文件夹下  
命令  
```sh
# 编译
python setup.py build

# 安装
python setup.py install
```


2018/11/12  
