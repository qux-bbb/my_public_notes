# 发布vscodium扩展

keywords: 发布扩展  

vscodium 扩展: https://open-vsx.org/  

为保证安全性，发布 vscodium 扩展稍微繁琐一点，简单整理一下，具体操作步骤见参考链接。  

1. 创建 Eclipse 账户  
    https://accounts.eclipse.org/user/register, 需要保证用户名和 github 一致  
2. 用 github 账户登录  open-vsx.org 并签署发布者协议  
    https://open-vsx.org/  
3. 创建访问令牌  
4. 创建命名空间  
    ```
    npm i -g ovsx
    npx ovsx create-namespace <name> -p <token>
    ```
    `<name>` 就是发布者名字，`<token>` 是第3步创建的访问令牌  
5. 打包上传  
    ```
    npx ovsx publish -p <token>
    ```

经过上面的步骤之后，以后再发布新版本，只需要执行第 5 步就好了  

命名空间需要在github创建issue来认证才不会弹出警告信息  
在 https://github.com/EclipseFdn/open-vsx.org/issues/new/choose 选择 `Claim namespace ownership`，然后说明一下，提交issue等待通过就好了  


参考链接：  
1. https://github.com/eclipse/openvsx/wiki/Publishing-Extensions  
2. https://github.com/eclipse/openvsx/wiki/Namespace-Access  


2021/5/9  
