# 图片转ASCII字符

有2个工具可以将图片转为ASCII字符，简单记一下。  

## jp2a

官网: https://csl.name/jp2a/  
github地址: https://github.com/cslarsen/jp2a  

最简单命令: `jp2a apple.png`  

举个例子：  
![苹果](./images/apple.png)  
```
$ jp2a apple.png --size=60x30
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWK0OkO0XMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWNXkoollcc:::o0WMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNkxxxddoooollccc::xNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMKdONMMWXKOxoooolccccKMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMW0NONMMMMMMMMMWX0xooollcXMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMKc:WWWWWWWWMMMMMMMWKkddoxMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWWXK0,d0OkxdooodxOXMMMMMN0xkMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWXOxodxxx,dkkkxdollccclkNMMMMWNMMMMMMMMMMMMM
MMMMMMMMMMMMMMNOlclloddxkkcxkxdddddooolcckWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMM0l::ccloddxxxkxxxkkkkkkkxdolcoNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMx:;;:clodxxkkOOOkO00KKK0OxdollldWMMMMMMMMMMMMMMM
MMMMMMMMMMMO:;,;;clodxkO000000KKKKOkkdddoooo0MMMMMMMMMMMMMMM
MMMMMMMMMMW:,,,;;:clodxkOOO00OO0OOkkddoddoddkMMMMMMMMMMMMMMM
MMMMMMMMMMK:,',,,;:cllodxkkkkkOOkxkxdddoxdxkkWMMMMMMMMMMMMMM
MMMMMMMMMM0:,,,,,;;::cclododddxxxdxddoxokxkOOMMMMMMMMMMMMMMM
MMMMMMMMMMN:,,,,,;;;;::cclllllodddxdddxdxxO00MMMMMMMMMMMMMMM
MMMMMMMMMMMd;,,,,,,;;::::ccclcldoddxddddxk00NMMMMMMMMMMMMMMM
MMMMMMMMMMMNc,,,,,,;;;:::ccccclolodxdddddO0KMMMMMMMMMMMMMMMM
MMMMMMMMMMMMK:,,,,,,;;::cclcccloooddodddx0KWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMXl,'',,,;::ccllcclooodooddxOKWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWk;'',,,;::ccllclooododdxOXMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMWWNNXx:,,,;;cccllcloodooxk0XNWWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWNK0kkxdl::::clloooldxdododxkO0XNWMMMMMMMMMMMMMMM
MMMMMMMMMMMWX0Oxdolc::;;;;:::c:::::ccodxkOKNWMMMMMMMMMMMMMMM
MMMMMMMMMMMMWNXK00OkxxddddoooddddxxkkO0KKXNWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWWWWNNNNXXXXXXXXXNNNNNWWWWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
```


## ascii-image-converter

有windows和linux版本。  

github地址: https://github.com/TheZoraiz/ascii-image-converter  

举例：  
```
>ascii-image-converter.exe apple.png -d 60,30
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*+++++*#@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*+++++===--=+%@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%++*****++++++==--=%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@#*%@@@@@@%#*+++++==-#@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%*%#@@@@@@@@@@@@%#*+++==%@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%=-@@@@%%%%@@@@@@@@%#*+=*@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@%%%#-=#***+++=++*#@@@@@@%*#@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@#*++++*#-+****++====-=*%@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@*====++****=****+++++++===*@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#=-===++++***************++==+@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@*----==++****#######%%%##*++++=*@@@@@@@@@@@@@@@@
@@@@@@@@@@@*-----==+***#######%%%##***++++++%@@@@@@@@@@@@@@@
@@@@@@@@@@@=-----===+**###########****++++*+*@@@@@@@@@@@@@@@
@@@@@@@@@@#-::----===++****##*##****++++*+***@@@@@@@@@@@@@@@
@@@@@@@@@@#--:-----====+++++*+******++*+***##@@@@@@@@@@@@@@@
@@@@@@@@@@%----:------===+=++++*++**++*+**##%@@@@@@@@@@@@@@@
@@@@@@@@@@@+-----------=======++++**+*****##%@@@@@@@@@@@@@@@
@@@@@@@@@@@%----------=========++++*+++**###@@@@@@@@@@@@@@@@
@@@@@@@@@@@@#----:-----=======++++++++++*##@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#-::------========++++++++*#%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%=:::---=========+++++++**%@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@#=-:----=======+++++**#%@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%%###*==--===+++=++**+***##%%%@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@%#**++===----======+=====++**#%%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%##***++==============++**##%%@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@%%%%%###########%%%%%%@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```


在终端支持多颜色情况下，两个工具都可以显示彩色字符。  


2021/5/4  
2021/6/8  
