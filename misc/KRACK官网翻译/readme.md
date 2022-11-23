# KRACK官网翻译

# 密钥重装攻击--通过强制重用nonce来攻破WPA2
*由mec-DistriNet, KU Leuven 的 Mathy Vanhoef 发布*  


## 介绍
WPA2是一个确保所有现代受保护网络安全的协议，我们发现了它的严重弱点。一个在受害者范围内的攻击者可以通过密钥重装攻击（**k**ey **r**einstallation **a**tta**ck**s， KRACKs）来利用这些弱点。具体来说，攻击者可以使用这种新颖的攻击技术来读取先前被认为是安全加密过的信息。这可能被利用来窃取敏感信息，如信用卡号，密码，聊天信息，电子邮件，照片等。**该攻击可以打击所有现代受保护的Wi-Fi网络**。根据网络配置，它还可能注入和操作数据。比如，攻击者有可能将勒索软件或者其他恶意软件注入网站。  

弱点在于Wi-Fi标准本身，而不是单独的产品或者实现。因此，即使WPA2正确的实现也可能受到影响。为了防止攻击，用户必须在安全更新可用时立即更新受影响的产品。请注意，**如果你的设备支持Wi-Fi，则很有可能受到影响**。在我们初步的研究中，我们发现Android, Linux, Apple, Windows, OpenBSD, MediaTek, Linksys等都受到一些攻击变体的影响。有关特定产品的更多信息，请查阅[CERT/CC数据库](https://www.kb.cert.org/vuls/byvendor?searchview&Query=FIELD+Reference=228519&SearchOrder=4)，或者和你的供应商联系。  

攻击相关的研究将在[计算机与通信安全（Computer and Communications Security ，CCS）](https://acmccs.github.io/session-F3/)会议和 [Black Hat Europe](https://www.blackhat.com/eu-17/briefings/schedule/#key-reinstallation-attacks-breaking-the-wpa2-protocol-8861)会议上发表。我们的[详细研究论文](https://www.krackattacks.com/#paper)已经可以下载了。  


## 演示
作为一个概念验证（proof-of-concept，Poc），我们对Android智能手机执行了密钥重装攻击。在这个演示中，攻击者能够解密受害者发送的所有数据。对于攻击者来说，这很容易完成，因为我们的密钥重装攻击对Linux和Android6.0或更高版本极具破坏性。这是因为**Android和Linux可以被欺骗（重）装一个全零加密密钥**（详细信息参阅下文 *细节* 中的 *Android and Linux*）。当攻击其他设备时，尽管可以解密大量数据包，但很难解密所有数据包。以下演示突出显示在对受保护的Wi-Fi网络执行密钥重装攻击时攻击者可以获取的信息类型：  

[一个演示的youtube视频](https://youtu.be/Oh4WURZoR98)  

我们的攻击并不限于恢复登录凭据（即电子邮件和密码）。通常，受害者传送的任何数据或信息都可以被解密。此外，根据所使用的设备和网络设置，还可能解密向受害者发送的数据（例如网站的内容）。虽然网站或应用可能会使用HTTPS作为额外的保护层，但在很多情况下，这种额外的保护措施仍然会被忽略。例如，以前HTTPS在[非浏览器软件](https://pdfs.semanticscholar.org/48fc/8f1aa0b6d1e4266b8017820ff8770fb67b6f.pdf)、[苹果的iOS和OS X](https://www.imperialviolet.org/2014/02/22/applebug.html)、[Android应用](https://arstechnica.com/information-technology/2015/04/android-apps-still-suffer-game-over-https-defects-7-months-later/)、[再次Android应用](https://arxiv.org/ftp/arxiv/papers/1505/1505.00589.pdf)（译者注：这里作者举了2个安卓的例子）、[银行应用](http://blog.ioactive.com/2014/01/personal-banking-apps-leak-info-through.html)甚至在[VPN应用](https://arstechnica.com/information-technology/2017/01/majority-of-android-vpns-cant-be-trusted-to-make-users-more-secure/)中都被绕过。  


## 细节
我们的主要攻击是针对WPA2协议的四次握手。当客户端想要加入受保护Wi-Fi网络时，此握手被执行，并用于确认客户端和接入点都具有正确的凭据（例如网络的预共享密码）。同时，4步握手还会协商一个新的加密密钥，用于加密所有后续流量。目前，所有现代受保护Wi-Fi网络都使用4步握手。这意味着所有这些网络都受到我们攻击（或者一些变体）的影响。例如，攻击影响个人和企业Wi-Fi网络，较旧的WPA和最新的WPA2标准，甚至是只使用AES的网络。**我们对WPA2的所有攻击都使用一种称之为密钥重装攻击（KRACK）的新技术**：  

### 密钥重装攻击：总体描述
在密钥重装攻击中，攻击者将诱骗受害者重装已经在使用的密钥。这是**通过操纵和重播加密握手消息来实现的**。当受害者重装密钥时，诸如增量发送数据包号（即随机数）和接收数据包号（即重播计数器）的相关参数被重置为其初始值。本质上，为了保证安全性，一个密钥只能被安装和使用一次。很不幸，我们发现WPA2并没有保证这一点。通过操纵加密的握手包，我们可以在实际中利用这个弱点。  

### 密钥重装攻击：针对4步握手的具体示例
如研究论文的介绍所述，密钥重装攻击背后的想法可以归纳如下。当客户端加入网络时，它会执行4步握手来协商一个新的加密密钥。在接收到4步握手的信息3后，将会安装该密钥。一旦密钥被安装，它就会用在加密协议里，对正常数据帧进行加密。然而，由于消息可能丢失或被丢弃，接入点（AP）没有收到适当的响应作为确认，就会重传消息3。结果就是，客户端可能会多次接收到消息3。每次收到消息，客户端将重新安装相同的加密密钥，从而重置增量发送数据包号（随机数），并接收加密协议使用的重播计数器。我们展现的就是**攻击者可以通过收集和重播4步握手中的消息3来强制重置随机数**。通过这种方式强制随机数重用，加密协议就能被攻击。例如可以重放、解密、伪造数据包。同样的技术也可以用来攻击组密钥、PeerKey、TDLS（Tunneled Direct Link Setup，通道直接链路建立）和快速BSS（Basic Service setup， 基本服务设置）转换握手包。  

### 实际影响
在我们看来，最广泛和最具影响力的攻击是4步握手的密钥重装攻击。我们基于两个观察结果做出判断。第一，在研究中，我们发现大多数客户端受到影响。第二，攻击者可以使用此攻击来解密客户端发送的数据包，从而拦截敏感信息，如密码或Cookie。数据包可以被解密是因为密钥重装攻击会导致传输的随机数（有时被称为数据包号或初始化向量）被重置为0。这样就导致**以前已经使用过的加密密钥和随机数值再次被使用**。也就导致了WPA2所有的加密协议在加密数据包时重用了[密钥流](https://en.wikipedia.org/wiki/Keystream)。如果重用密钥流的消息具有已知内容，那就很容易导出所使用的密钥流，此密钥流就可以用相同的随机数来解密消息。当没有已知的内容时，解密数据包比较困难，尽管在几种情况下仍然是可能的（例如 [英文文本仍然可以被解密](https://crypto.stackexchange.com/a/2250)）。实际上，找到具有已知内容的数据包没什么问题，因此可以认为任何数据包都可以被解密。  

解密数据包的能力可用于解密TCP SYN数据包。这使得攻击者可以获取连接的TCP序列号，从而[劫持TCP连接](https://en.wikipedia.org/wiki/TCP_sequence_prediction_attack)。因此，即使使用了WPA2，攻击者也可以对开放的Wi-Fi网络执行最常见的攻击：将恶意数据注入未加密的HTTP连接。例如，攻击者可以通过这种方式将勒索软件或者恶意软件注入到受害者访问的网站。  

如果受害者使用WPA-TKIP或GCMP加密协议，而不是AES-CCMP，那这种影响是极其严重的。**针对这些加密协议，随机数重用使得攻击者不仅可以解密，还可以伪造和注入数据包**。 此外，因为GCMP在两个通信方向上使用相同的认证密钥，而且如果随机数被重用，该密钥就可以被恢复，所以受到影响较严重。需要注意的是，目前正在以无线千兆（Wireless Gigabit， WiGig）的名义推出对GCMP的支持，预计在未来几年内将被高速采用。  

数据包可以被解密（可能被伪造）的方向取决于握手包被攻击。简单地说，当攻击4步握手时，我们可以解密（和伪造）客户端发送的数据包。当攻击快速BSS转换（Fast BSS Transition， FT）握手时，我们可以解密（和伪造）发送给客户端的数据包。我们的大多数攻击也允许重放单播、广播、多播帧。有关详细信息，请参阅我们研究论文的第6节。  

请注意我们的攻击无法得到Wi-Fi网络的密码。也不会恢复在4步握手期间新协商的加密密钥。  

### Android 和 Linux
我们的攻击对于wpa\_supplicant(通常在Linux上使用的Wi-Fi客户端)2.4及以上版本的影响尤为严重。这种情况下，客户端将安装一个全零加密密钥，而不是重装真正的密钥。这个漏洞似乎是由Wi-Fi标准中的一个注释造成的：建议在第一次安装之后，从内存中清除加密密钥。当客户端接收到4步握手中的重传消息3时，就会重装现在已经清除的加密密钥，也就是安装一个全零密钥。由于Android使用wpa\_supplicant，Android 6.0及更高版本也包含此漏洞。这使得**拦截和操纵这些Linux和Android设备发送的流量变得很简单**。需要注意的是，目前50%的Android设备容易受到使用我们这种攻击的极具破坏性的变体的影响。  
### 已确定的CVE编号
列一下CVE（Common Vulnerabilities and Exposures）编号，以跟踪哪些产品会受到密钥重装攻击的特定实例的影响：  

* [CVE-2017-13077](https://nvd.nist.gov/vuln/detail/CVE-2017-13077)：在4步握手中重装成对加密密钥（PTK-TK）
* [CVE-2017-13078](https://nvd.nist.gov/vuln/detail/CVE-2017-13078): 在4步握手中重装组密钥（GTK）
* [CVE-2017-13079](https://nvd.nist.gov/vuln/detail/CVE-2017-13079): 在4步握手中重装完整性组密钥（IGTK）
* [CVE-2017-13080](https://nvd.nist.gov/vuln/detail/CVE-2017-13080): 在组密钥握手中重装组密钥（GTK）
* [CVE-2017-13081](https://nvd.nist.gov/vuln/detail/CVE-2017-13081): 在组密钥握手中重装完整性组密钥（IGTK）
* [CVE-2017-13082](https://nvd.nist.gov/vuln/detail/CVE-2017-13082): 在处理接收重发的快速BSS转换（FT）时重新关联请求并重装成对加密密钥（PTK-TK）
* [CVE-2017-13084](https://nvd.nist.gov/vuln/detail/CVE-2017-13084): 在PeerKey握手中重装STK密钥
* [CVE-2017-13086](https://nvd.nist.gov/vuln/detail/CVE-2017-13086): 在TDLS握手中重装隧道直连设置（TDLS）PeerKye（TPK）密钥
* [CVE-2017-13087](https://nvd.nist.gov/vuln/detail/CVE-2017-13087): 处理无线网络管理（WNM）睡眠模式响应帧时重装组密钥（GTK） 
* [CVE-2017-13088](https://nvd.nist.gov/vuln/detail/CVE-2017-13088): 处理无线网络管理（WNM）睡眠模式响应帧时重装完整性组密钥（IGTK）  

需要注意的是，每一个CVE都表示一个密钥重装攻击的特定实例。这意味着每个CVE都描述了特定的协议漏洞，因此**很多供应商都受到了每个CVE的影响**。你还可以阅读CERT/CC的 [vulnerability note VU#228519](https://www.kb.cert.org/vuls/id/228519)，了解哪些产品已经确定会受到影响。


## 论文
我们关于攻击的研究论文题目是[重装攻击：强制重用WPA2中的Nonce](https://papers.mathyvanhoef.com/ccs2017.pdf)，将[在2017年11月1日星期三](https://acmccs.github.io/session-F3/)的[计算机和通信安全（CSS）](https://www.sigsac.org/ccs/CCS2017/)会议上进行介绍。  

虽然这篇论文是现在公布的，但已经在2017年5月19日提交审阅。之后只做了微小的改动。因此，文中的发现已经有几个月了。与此同时，我们发现了更简单的技术来进行4步握手中的密钥重装攻击。通过这种新技术，攻破只接受4步握手中的消息3的加密重传的实现是很简单的。这也就意味着**攻击macOS和OpenBSD比论文中讨论的要容易的多**。  

我们想强调下列附录和勘误表：  
### 附录：wpa_supplicant v2.6和Android 6.0+
Linux的wpa_supplicant v2.6也容易在4步握手中安装全零加密密钥。这是由John A. Van Boxtel发现的。因此，高于6.0的所有Android版本也受到攻击的影响，可能会被诱骗安装全零加密密钥。新的攻击通过注入伪造的消息1（和原先的消息1使用同样的ANonce），将重传的消息3转发给受害者。  

### 附录：其他易受攻击的握手
在论文中提到的初步研究之后，我们发现TDLS握手和WNM睡眠模式响应框架也容易受到密钥重装攻击。  

### 勘误
* 在攻击阶段3的图9中，从攻击者发送给认证者的帧应该是ReassoReq而不是ReassoResp。  
* 3.1节：图3包含状态机的简单描述（不是图2）。  

### 引用示例和bibtex条目
请引用我们的研究论文，而不是本网站（或引用两者）。您可以使用以下示例引用或bibtex条目：  
`Mathy Vanhoef and Frank Piessens. 2017. Key Reinstallation Attacks: Forcing Nonce Reuse in WPA2. In Proceedings of the 24th ACM Conference on Computer and Communications Security (CCS). ACM.`
```
@inproceedings{vanhoef-ccs2017,
  author        = {Mathy Vanhoef and Frank Piessens},
  title         = {Key Reinstallation Attacks: Forcing Nonce Reuse in WPA2},
  booktitle     = {Proceedings of the 24th ACM Conference on Computer and Communications Security (CCS)},
  year          = {2017},
  publisher     = {ACM}
}
```


## 工具
我们写了脚本来检测一个4步握手、群组密钥握手或快速BSS转换（FT）握手的实现是否容易受到密钥重装攻击。一旦我们有时间整理好使用说明，脚本就会被公布。  

我们还写了一个Poc脚本，用来验证特定的Android和Linux设备中存在的全零密钥重装。这个脚本被用在了我们的演示视频中。一旦每个人都有合适的机会更新他们的设备（我们也有机会准备要发布的代码库），我们就会公布这个脚本。需要知道的是，我们的Poc可靠性取决于受害者对真正网络的接近程度。如果受害者非常接近真正的网络，脚本可能会失败，因为受害者会一直连接真正的网络来通信，即使受害者（被强制）进入和该网络不同的Wi-Fi频道。  


## Q&A

### 我们需要WPA3吗？
不，幸运的是**具体实现可以使用向后兼容的方式进行修补**。 这意味着一个打了补丁的客户端仍然可以和没有打补丁的接入点（AP）进行通信，反之亦然。换句话说，打补丁的客户端或者接入点可以在和以前完全相同的时间，发送完全相同的握手包消息。总之，安全更新需要确保密钥只能安装一次，从而防止我们的攻击。所以再说一次，一旦安全更新可用，立刻更新你的所有设备。最后，尽管一个没有打补丁的客户端可以和一个打补丁的接入点通信，反之亦然，但还是建议客户端和接入点都打上补丁以防止所有攻击。  

### 我应该更改我的Wi-Fi密码吗？
更改Wi-Fi网络的密码并不能防止（或减轻）攻击。所以你不必更新Wi-Fi网络的密码。相反，你应该确保所有设备都已更新，还应该更新路由器的固件。不管怎么说，更新你的客户端设备和路由器后，更改Wi-Fi密码绝对不是个坏主意。  

### 我使用只用AES的WPA2。那也很脆弱吗？
是的，这样的网络配置也很脆弱。攻击对WPA1和WPA2，针对个人和企业网络以及正在使用的任何加密套件（WPA-TKIP，AES-CCMP和GCMP）都有效。所以每个人都应该更新设备以防止攻击！  

### 你在本网站使用“we”这个词。“we”是谁？
我使用“we”一词，因为这是我以前在论文中写的。事实上，所有的工作都是由我（Mathy Vanhoef）完成的。我的优秀主管以[荣誉作者](https://en.wikipedia.org/wiki/Academic_authorship#Honorary_authorship)身份被加到研究论文里，是因为他出色的总体指导。但实际上所有的工作都是我自己做的。所以学术论文的[作者列表](http://phdcomics.com/comics.php?f=562)不代表[工作分工](https://imgur.com/a/mKnnu):)  

### 我的设备脆弱吗？
可能吧。任何使用Wi-Fi的设备都很容易受到攻击。联系你的供应商了解更多信息。  

### 如果我的路由器没有安全更新怎么办？或者如果路由器不支持802.11r怎么办？
如果路由器或接入点（AP）支持快速BSS转换（FT）握手，或者它们支持客户端（中继器）功能，这样的设备才会受到我们的攻击。首先，FT握手是802.11r的一部分，主要由企业网络支持，而不是家庭的路由器或接入点。此外，大多数家庭路由器或接入点不支持（或不会使用）客户端（中继器）功能。换句话说，你的家庭路由器或接入点可能不需要安全更新。相反，主要是企业网络将不得不更新他们的网络基础设施（即他们的路由器和接入点）。  

也就是说，一些供应商在调查关于我们的攻击时发现了特定实现的安全问题。例如，[hostapd被发现在rekeys期间重复使用4步握手中的ANonce值](https://w1.fi/security/2017-1/wpa-packet-number-reuse-with-replayed-messages.txt)。具体而言，这意味着即使你的路由器或接入点不支持802.11r，并且不支持客户端功能，也可能仍然需要更新。请联系你的供应商了解更多详情。  

你可以尝试通过禁用客户端功能（例如用于中继器模式）并禁用802.11r（快速漫游）来减轻对路由器和接入点的攻击。对于普通家庭用户，此外，更新所有客户端设备，如笔记本电脑和智能手机。如果你的客户端设备没有收到更新，可以尝试与你的路由器供应商联系，询问他们是否有防止对已连接设备攻击的更新。  

### 只修补接入点是不是就够了？或者只修补客户段端？
目前，所有易受攻击的设备都应该打补丁。换句话说，修补AP不会阻止对易受攻击的客户端的攻击。同样，修补所有客户端也不会阻止对易受攻击的接入点的攻击。需要注意的是，只有支持快速BSS过渡握手（802.11r）的接入点可能是易受攻击的。  

也就是说，我们的工作在于[对接入点修改，以防止对易受攻击的客户端进行攻击](https://www.krackattacks.com/#ap-mitigations)。这些修改不同于给脆弱的接入点写的安全补丁！因此，除非你的接入点供应商明确提及他们的补丁可以防止对客户端的攻击，否则你还必须给客户端打补丁。  

### 我们可以修改接入点以防止对客户端的攻击吗？
是的，可以修改接入点使得连接的客户端不会被攻击。这样的修改只有在客户端连接到修改过的接入点才能防止攻击。当客户端连接到一个不同的接入点，仍然可以被攻击。  

技术上来说，可以通过修改接入点来达到防止攻击的目的，比如在4步握手阶段中不重传消息3。此外，接入点也需要被修改为不重传组密钥握手的消息1。[hostapd项目已经有这样的可用的修改了](https://w1.fi/cgit/hostap/commit/?id=6f234c1e2ee1ede29f2412b7012b3345ed8e52d3)，他们目前正在评估哪一方面会影响这些握手的可靠性。我们也可以通过使用相同的（以前的）EAPOL-Key重播计数器重传上述握手消息，防止对客户端的攻击。还可以通过让接入点以延迟的方式安装组密钥，并确保接入点仅接受最新的重放计数器来防止群组密钥握手的攻击（详见论文4.3节）。  

对于某些产品，无需更新就可以达到缓解的目的。例如，在某些接入点上，可以禁用所有握手消息的重传，防止针对4步握手和组密钥握手的客户端攻击（[比如思科的一个例子](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20171016-wpa#workarounds)）。  

### 你是怎么发现这些漏洞的？
在准备[另一篇论文](https://lirias.kuleuven.be/bitstream/123456789/572634/1/asiaccs2017.pdf)的最终版本时，我重新检查了我们对有关OpenBSD实现4次握手的一些声明。在某种意义上，我正在放松，因为我应该只是完成论文，而不是盯着代码。但是就在那里，我检查了一些已经读了一百次的代码，以逃避必须看下一段的东西。就是那个时候，对[ic_set_key](https://github.com/openbsd/src/blob/ca7fda7e2ae9fcf15b882d71bc910143e6b0d09b/sys/net80211/ieee80211_pae_input.c#L519)的一个特别的调用引起了我的注意。当处理4步握手的消息3时，将调用此函数，并将成对密钥安装到驱动程序。在盯着那行代码的时候，我在想“嗯。如果该函数调用两次，会发生什么。”。当我（正确地）猜到调用它两次可能会重置与密钥相关联的随机数。而且由于消息3可以被接入点重传，实际上它可能被调用两次。“最好先记下这一点。其他供应商也可能也会调用这样一个函数两次。但是现在先完成这篇论文...”。几周后，在完成论文和其他工作之后，我更详细地研究了这个新想法。接下来的大家都知道了。  

### 4步握手在数学上被证明是安全的。你的攻击是怎么可行的呢？
简短的回答是正式证明不能确保一个密钥只被安装一次。相反，它只能保证协商密钥保密，握手信息不能被伪造。  

详细的回答在我们的研究论文的介绍中：我们的攻击并不违反在4步握手的正式分析中证明的安全属性。确切的说，这些证明表明协商的加密密钥保持私有，并且客户端和接入点（AP）的身份被确认。我们的攻击不会泄露加密密钥。另外，虽然使用TKIP或GCMP可以伪造正常的数据帧，但攻击者不能伪造握手信息，因此在握手期间不能模仿客户端或AP。因此，在4步握手的正式分析中证明的属性仍然是正确的。但是，问题在于证明没有对密钥安装进行建模。换句话说，正式模型没有定义何时应该安装协商密钥。实际上，这意味着可以多次安装相同的密钥，从而重置被协议（例如，WPA-TKIP或AES-CCMP）使用的随机数和重放计数器。  

### 论文中的一些攻击似乎很难实现
我们进行了后续的工作，使我们的攻击（例如针对MacOS和OpenBSD）更为普遍，更容易执行。所以尽管我们同意这篇论文中的一些攻击方案是不切实际的，但是不要因为这个就让你相信密钥重装攻击不能在实际中被利用。  

### 如果攻击者可以做中间人攻击，为什么不能解密所有的数据？
如演示所述，攻击者首先在受害者和真正的Wi-Fi网络（被称为一个基于通道的MitM位置）之间首先获得了一个中间人（MitM）位置。但是，MitM的位置并不能使攻击者解密数据包！这个位置只允许攻击者可以延迟，阻止或重放*加密的*数据包。所以在攻击的这一点上，他们还不能解密数据包。相反，延迟和阻止数据包的能力用于执行密钥重装攻击。执行密钥重装攻击后，数据包可以解密。  

### 在野外有人可以利用这个漏洞吗？
我们无法确定这个漏洞是否已经（或正在被）在野外被活跃利用。也就是说，密钥重装攻击实际上可以自发发生，没有攻击者存在！举个例子如果握手的最后一个消息由于背景噪声而丢失，导致先前消息的重传。当处理这个重新发送的消息时，密钥可能重新安装，导致随机数重用，就像一次真正的攻击。  

### 我应该暂时使用WEP，直到我的设备被修补吗？
不！继续使用WPA2。  

### Wi-Fi标准是否会更新以解决这个问题？
根据共识，似乎Wi-Fi标准应该更新，以明确地防止我们的攻击。这些更新可能会与较早的WPA2实现向后兼容。时间将告诉我们标准是否以及如何更新。  

### Wi-Fi联盟是否也会解决这些漏洞？
对于不熟悉Wi-Fi的用户，[Wi-Fi联盟](https://en.wikipedia.org/wiki/Wi-Fi_Alliance)是一个证明Wi-Fi设备符合某些互通性标准的组织。除此之外，它也确保来自不同供应商的Wi-Fi产品一起工作。  

[Wi-Fi联盟有一个计划](https://www.wi-fi.org/securityupdate2017)来帮助解决已经发现的WPA2漏洞。总结来说，他们会：  
* 需要在其全球认证实验室网络中测试此漏洞。
* 提供漏洞检测工具供任何Wi-Fi联盟成员使用（此工具基于我自己的检测工具，它确定设备是否容易受到一些已发现的密钥重装攻击的威胁）。
* 向设备供应商广泛介绍有关此漏洞的详细信息，包括修补措施。此外，鼓励供应商与他们的解决方案提供商合作，快速整合任何必要的补丁。
* 使客户明白漏洞的重要性，以确保他们已经从设备制造商安装了最新推荐的安全更新。

### 为什么使用match.com作为演示视频的例子？
用户在诸如match.com等网站上共享很多个人信息。所以这个例子突出了攻击者可以获得的所有敏感信息，希望通过这个例子，人们也可以更好地认识到潜在的（个人）的影响。我们也希望这个例子让人们了解[这些约会网站可能收集的所有信息](https://www.theguardian.com/technology/2017/sep/26/tinder-personal-data-dating-app-messages-hacked-sold)。  

### 如何防止这类的错误？
我们需要对协议实现进行更严格的检查。这需要学术界的帮助和额外的研究！我们和其他研究人员希望组织研讨会来改进和验证安全协议实现的正确性。  

### 为什么选择了krackattacks.com这个域名？
首先，我知道KRACK攻击是一种[pleonasm](https://en.wikipedia.org/wiki/Pleonasm)，因为KRACK代表 **k**ey **r**einstallation **a**tta**ck**，因此已经包含了单词attack。但这个域名押韵，就用了这个域名。  

### 你为此获得了bug奖励吗？
我还没有申请任何bug奖励，也没有收到一个。  

### 这种攻击和其他对WPA2的攻击相比如何？
这是第一个针对WPA2协议本身的攻击，不依赖于密码猜测。事实上，其他针对WPA2网络的攻击是针对周围技术的比如[Wi-Fi Protected Setup（WPS）](http://archive.hack.lu/2014/Hacklu2014_offline_bruteforce_attack_on_wps.pdf)，或者针对旧标准的攻击比如[WPA-TKIP](https://lirias.kuleuven.be/bitstream/123456789/401042/1/wpatkip.pdf)。不同在于，已存的攻击中没有一个是针对4步握手或者针对在WPA2协议中定义的加密套件。相反，我们的密钥重装攻击针对4步握手（还针对其他握手），突出了WPA2协议本身的漏洞。  

### 其他协议可以受到密钥重装攻击的影响吗？
我们觉得其他协议的某些实现可能也容易遭受类似的攻击。所以审计安全协议的实现是否有这种攻击是一个好主意。然而，我们认为其他协议标准不太可能受到类似攻击的影响（或者至少我们希望这样）。然而，审计别的协议仍然是一个好主意。  

### 有一个更高分辨率版本的logo吗？
是的，[在这儿](https://www.krackattacks.com/images/logo.png)。非常感谢制作logo的人。  

### 你是什么时候通知厂商这个漏洞的呢？
我们在2017年7月14日左右向我们测试过的产品的供应商发出了通知。在和这些供应商沟通之后，我们意识到我们发现的漏洞有多普遍（直到那时我才真正说服自己，这确实是一个协议的漏洞而不是一套实现的错误）。到了那个时候，我们决定让[CERT/CC](https://cert.org/)帮助披露这些漏洞。之后，CERT/CC于2017年8月28日向供应商发出了广泛的通知。  

### 为什么OpenBSD在漏洞发布之前默默地发布了补丁？
OpenBSD在[2017年8月30日公布了一项勘误](https://marc.info/?l=openbsd-announce&m=150410604407872&w=2)，默默阻止了密钥重装攻击。更具体地说，他们为[OpenBSD 6.0](https://ftp.openbsd.org/pub/OpenBSD/patches/6.0/common/041_net80211_replay.patch.sig)和[OpenBSD 6.1](https://ftp.openbsd.org/pub/OpenBSD/patches/6.1/common/027_net80211_replay.patch.sig)发布了补丁。  

在CERT/CC参与协调之前，我们于2017年7月15日告知OpenBSD这个漏洞。很快，Theo de Raadt就回复并批评了这个暂时的披露截至日期：“In the open source world, if a person writes a diff and has to sit on it for a month, that is very discouraging”。因为这样，我就给OpenBSD回复了早已给他们写好的建议的文章，在那个时候把暂定披露截止日期定在了大概8月底。作为妥协，我允许他们默默地修复漏洞。事后看来，这是一个坏决定，因为别人可能通过检查他们的静默补丁来重新发现漏洞。为了避免今后出现这个问题，OpenBSD将在漏洞公布之前接收漏洞通知。  

### 所以你期待找到别的Wi-Fi漏洞？
“I think we're just getting started.”  — Master Chief, Halo 1  

## 我可以从哪里了解更多关于密钥重装攻击的信息？
比较好的技术类信息和评论：  
* [LiveOverflow录制了一个视频来解释攻击](https://www.youtube.com/watch?v=fOgJswt7nAc)
* [Computerphile也录制了关于攻击的视频](https://www.youtube.com/watch?v=mYtvjijATa4)
* [关于KRACK和漏洞的原因，Matthew Green写了一篇比较好的博客](https://blog.cryptographyengineering.com/2017/10/16/falling-through-the-kracks/)
* [Nojo Networks 对攻击写了一篇详细的博客](https://blog.mojonetworks.com/wpa2-vulnerability)
* [Bruce Schneier 也对攻击做了简要的讨论](https://www.schneier.com/blog/archives/2017/10/new_krack_attac.html)

有比较高质量信息的报道：  
* [BCC制作了一个短片来解释攻击，还写了一篇文章](http://www.bbc.com/news/technology-41635516)
* [华尔街日报: Significant Flaw Discovered in Wi-Fi Security Protocol](https://outline.com/MHm5yw)
* [卫报: 'All wifi networks' are vulnerable to hacking, security expert discovers](https://www.theguardian.com/technology/2017/oct/16/wpa2-wifi-security-vulnerable-hacking-us-government-warns)
* [时代周刊: Everything With Wi-Fi Has a Newly Discovered Security Flaw. Here's How to Protect Yourself](http://time.com/4983720/krack-attack-wpa2-wifi/)
* [Ars Technica: Serious flaw in WPA2 protocol lets attackers intercept passwords and much more](https://arstechnica.com/information-technology/2017/10/severe-flaw-in-wpa2-protocol-leaves-wi-fi-traffic-open-to-eavesdropping/)
* [Ars Technica: How the KRACK attack destroys nearly all Wi-Fi security](https://arstechnica.com/information-technology/2017/10/how-the-krack-attack-destroys-nearly-all-wi-fi-security/)
* [The Verge: Wi-Fi security has been breached, say researchers](https://www.theverge.com/2017/10/16/16481136/wpa2-wi-fi-krack-vulnerability)
* [The Verge: 41 percent of Android phones are vulnerable to 'devastating' Wi-Fi attack](https://www.theverge.com/2017/10/16/16481252/wi-fi-hack-attack-android-wpa-2-details)
* [路透社: Researchers uncover flaw that makes Wi-Fi vulnerable to hacks](https://uk.reuters.com/article/us-cyber-wifi-flaw/researchers-uncover-flaw-that-makes-wi-fi-vulnerable-to-hacks-idUKKBN1CL1UE)
* [福布斯: Update Every Device -- This KRACK Hack Kills Your Wi-Fi Privacy](https://www.forbes.com/sites/thomasbrewster/2017/10/16/krack-attack-breaks-wifi-encryption/#5f734a282ba9)
* [CNET: KRACK attack: Here's how companies are responding](https://www.cnet.com/news/krack-wi-fi-attack-patch-how-microsoft-apple-google-responding/)




官网：https://www.krackattacks.com/


2017/10/24  
