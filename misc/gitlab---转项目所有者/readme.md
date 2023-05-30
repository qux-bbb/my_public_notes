# gitlab---转项目所有者

```
Currently, the only way to transfer a project from one user to another is:

1. Create a dummy group for which both users are owners
2. Have the old user transfer ownership of the project from themselves to the group
3. Have the new user transfer ownership from the group to themselves
4. Delete the dummy group
```

不能像github一样直接转，就很尴尬  

来源：  
https://gitlab.com/gitlab-org/gitlab-foss/-/issues/18423  


2020/10/20  
