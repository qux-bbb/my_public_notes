# Unity---获取输入设置text

"+" -> UI 中, 可以添加各种组件  

下面是文本相关的控制代码  

```CSharp
using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;


public class Button_Click : MonoBehaviour
{
    InputField txt_Input;
    Text txt_Show;
    public void OnClick(){
        Debug.Log("On Click");

        txt_Input = GameObject.Find("InputField").GetComponent<InputField>();
        txt_Show =  GameObject.Find("TextShow").GetComponent<Text>();

        Debug.Log(txt_Input.text);
        
        if (txt_Input.text != "")
        {
            txt_Show.text = txt_Input.text;
        }
    }
}

```


参考链接:  
1. https://www.bilibili.com/video/BV1tE411V721  
2. https://answers.unity.com/questions/1261333/how-to-use-input-field-value-in-scripting.html  
3. https://answers.unity.com/questions/1273054/change-text-value.html  


2020/4/12  
