# powershell混淆工具---Invoke-Obfuscation

https://github.com/danielbohannon  
这个人的混淆和检测混淆都有相关的项目，这里主要介绍 混淆项目  

项目地址：  
https://github.com/danielbohannon/Invoke-Obfuscation  

freebuf 相关介绍：  
https://www.freebuf.com/sectool/136328.html  

使用：  
```r
Import-Module ./Invoke-Obfuscation.psd1
Invoke-Obfuscation
```

简单命令记录：  
```r
# 设置脚本内容或路径
SET SCRIPTBLOCK script_block_or_command
SET SCRIPTPATH path_to_script_or_URL

# 显示当前选项
show options

# 导出混淆内容
out
```

一个简单混淆示例：  
```r
SET SCRIPTBLOCK Invoke-WebRequest -uri 'https://www.helloworld.com/index.php' -OutFile 'hello.exe'
string
2
2
2
2
back
out
```
最终效果：  
```ps1
 ((("{28}{51}{12}{6}{24}{13}{57}{37}{3}{27}{55}{59}{25}{36}{58}{19}{21}{64}{43}{68}{9}{16}{15}{45}{30}{17}{49}{61}{47}{41}{70}{33}{23}{69}{66}{53}{62}{4}{10}{7}{39}{48}{2}{60}{52}{63}{34}{5}{50}{56}{67}{22}{65}{46}{35}{20}{29}{54}{31}{42}{8}{38}{0}{18}{32}{14}{1}{11}{44}{26}{40}" -f'2Qy]65+[CHAr]82),[STrInG][CH','+[CHAr]76),[2Qy))  -crEPlaCe([CHar]121+[','njI5,jI5L2Qy,2Q','84}{98}{75}{19}{35}{16}{71}{73}{59}{51}{18}{','.heljI5,jI5SHOmjI5,jI5p{0}nNL,nNLojI5,jI5NjI5','Qy5','}{27}{8}{13}{34','NL,jI5,jI5{jI5,jI5.njI5','}{15}{80}{82}{69}{11}{88}{67}{72}{54}{44}{66}{81}{20}{37}{5}{17}{10}{34}{63}{101}{33}{48}{52}{62}2Qy,2Qy-jI5,jI5ljI5,jI5ojI5,jI5bRejI5,jI5nNjI5,jI5','I5,jI5LljI5,jI5cj',',jI511}jI5,jI5LjI5,jI5InnjI5,jI5njI5,jI5ejI5,jI5SHojI5,jI5lnNL,nNjI5,jI5Le{jI5,jI5wn','CHar]102+[CHar]83','{14}{9}{18}{1}{4}{33','28}{0}{23}{25}{11}{5}{30}','CHAr]78','0]jI5,jI5nNL,nNL//wwjI5,jI5NjI5,jI56jI5,jI5e[4]+jI5,jI52Qy,2QyjI5.nNL,nNjI5,jI5NjI5,jI539jI5,jI52jI','I5,jI5E[3','I5,jI2Qy,2QyI5,nNL2','Ar]36).rePlAcE(jI55ONjI5,[STrInG][CHAr]342Qy,2Qy).rePlAcE(([CHAr]110+','2Qy,2Qy5,jI5}{jI5','jI5,jI5',',jI','2Qy,2Qy5,jI5 2Qy,2Qy .( x2Qy,2Qy{28}{90}{95}{8}{70}{60}{40}{104}{100}{97}{96}{85}{2}{22}yfS-f 2Qy,2QyI5ind','25}','}{22}{12}{2}{7}{15}{3}{20}{10}{19}{6}{31}{24}{29}{','2Qy3}','34-REpLace  2QyjI52Qy,[CHar]39-REpLace  2QyxBl2Qy,[CHar]36)ucS.( Jw4sHelL','1','(((2w','0}nNL,nNL {jI5,jI5{9}jI5,jI52Q','cjI5,jI5fjI5,jI5}{jI2Qy,2QyjI5tFile {j','I2Qy,2Q','[','yjI5xjI5-joINjI5jI5) ( ((yfS{27}{23}{29}{61}{','1jI5,jI58}jI5,jI5ONjI5,jI5nNL,nNLejI2Qy,2','yI5,jI5NL.jI5,j2Qy,2Qy-','{49}{26}{57}{86}{64}{7','{24}{65}{',',njI5,jI5L,njI5,jI5{jI5,jI57}{1}{8jI5,jI5+njI5,jI5nNL,nNLttjI5,jI5}jI2Qy,',',jI5pjI5,jI51}j2Qy,2Qy,jI5om/jI5,jI5XnjI5,jI5{6}{jI5,jI5wjI','Id[1]+Jw4SHElLid[13]+2Qyx2Qy)','I5nNL)) jI5,jI5{15}{1jI5)).rePlAcE(([C2Qy,2QyS','yHAr]57+[CHAr2Qy,2Qy1}{58}{83}{1}{30}{6}{7',',jI5hjI5,jI5f jI5,jI5nNLjI5,jI57}{4}{19jI2Qy,2Qy5. jI5,jI5LexnNL,j','),[CHar]','5,jI5(5jI5,j2Qy,2Qy()[1,3]+2Qy,2QyjI5,jI5NLjI5,2Qy,2Qy[','jI5nNLpsjI5,j2Qy,2Q','NL,nNLjI5,j','5,jI50}h','Qy,2QyBlVerbosePREferEnCE.tosTRing2Qy,2Qy-OunNLjI5,jI5NL)(((jI5,jI5{3jI','L}hejI5,jI512}jI5,jI5L,jI5,jI5','1{26}','I5urinNLjI5,2Qy,','{13}{41}{','y,2Qy5,j','02Qy,2Qy5}{1jI5,jI5vokenNL,nNL jI5,jI5nNLjI5,jI5) )jI5,jI5( jI5,jI5{14}jI5,jI5mjI5,jI5NL,nNjI5,jI2Qy,2Qy{jI5,jI5NLjI5,jI59AR','exnNL,njI5,jI5nNLjI5,jI5NL,nNLjI5,jI5,nNL nNL,nNjI5,jI5NL,njI5,jI50}{5jI5,jI5HAR]jI5,jI5ojI5,jI5}{','{16}{32}{35}{36}{17}{21}2w1 -f 2QyI513}{22}2Qy,2Qy{99}{77}{39}{87}{56}','4}{31}{45}{89}{79}{55}{50}{0}{76}{9}{78}{2','PjI5,jI5rldjI52Qy,','y 2Qy,2Qy5,j','5,jI5stnNL,nNL-WjI5,jI5}2Qy,2Qy0n','92}{93}{12}{3}2Qy,2QyjI5','2Qy{2jI5,jI520}{10}{','52Qy,2QyI5,jI5L:nNjI5,jI5qujI5,jI55ON-jI5','jI5,','{32}{14}{42}{46}{38}{4}{94}{47}{91}{68}{102}{105}','j','I5,jI59ARpj','{36}{43}{53}','TrInG][CHAr]39))2Qy,2Q'))  -REpLace'ucS',[chAR]124  -REpLace'Jw4',[chAR]36 -crePlAcE '2Qy',[chAR]39  -REpLace([chAR]50+[chAR]119+[chAR]49),[chAR]34) |iEX
```


2020/5/28  
