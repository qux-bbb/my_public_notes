# yara规则---EmfClick

```r
rule EmfClick
{
    meta:
        author = "qux"
        description = "Emf file contains click string"

    strings:
        $click = "click here" wide nocase

    condition:
        filename matches /word\/media\/.+\.emf/ and
        $click
}
```

2019/9/17  
