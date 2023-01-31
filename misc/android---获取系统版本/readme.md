# android---获取系统版本

kotlin:  
```r
package com.example.test

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val infoView:TextView = findViewById(R.id.info);
        infoView.text = "MODEL: " + android.os.Build.MODEL +
                "\nVERSION.SDK_INT: " + android.os.Build.VERSION.SDK_INT +
                "\nVERSION.RELEASE: " + android.os.Build.VERSION.RELEASE;

    }
}
```

原链接: https://www.cnblogs.com/Free-Thinker/p/6638376.html  


2023/1/31  
