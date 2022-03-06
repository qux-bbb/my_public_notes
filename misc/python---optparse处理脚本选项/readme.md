# python---optparse处理脚本选项

optparse已被弃用，建议使用argparse  

官网: https://docs.python.org/2.7/library/optparse.html  

实例：  
```python
from optparse import OptionParser

    parser = OptionParser(
        'Usage:    python %prog [options]\n'
        'Example:\n'
        '  Detect single webpage: python %prog -a webpage -u https://www.baidu.com\n'
        '  Detect whole website: python %prog -a webpage -u https://www.baidu.com -w\n'
        '  Detect pcap file: python %prog -a pcap -f hello.pcapng\n'
        '  Detect sniffed 50 packages: python %prog -a pcap -c 50\n'
        '  Update some files: python %prog --update\n')

    parser.add_option('-a', '--action', dest='action', help='what to do, could be one of them: webpage | pcap')
    parser.add_option('-f', '--file', dest='pcap_file', help='the pcap file to scan, if action is pcap, this option is valid')
    parser.add_option('-u', '--url', dest='url', help='the url or website to scan, if action is webpage, this option is valid')
    parser.add_option('-w', '--whole_site', action='store_true', dest='whole_site', default=False, help='need to scan whole website, if action is webpage, this option is valid')
    parser.add_option('-i', '--interface', dest='interface', help='the interface to sniff, if action is pcap and have not -f, this option is valid, can only be used under linux')
    parser.add_option('-c', '--count', type='int', dest='sniff_caps_count', help='the count of  caps to sniff, if action is pcap and have not -f, this option is valid')
    parser.add_option('-t', '--time', type='int', dest='sniff_time', help='the time(seconds) to sniff, if action is pcap and have not -f, this option is valid, only -c or -t')
    parser.add_option('-s', '--save', action='store_true', dest='save_pcap', default=False, help='save the packages sniffed, if action is pcap and have not -f, this option is valid')
    parser.add_option('--update', action='store_true', dest='update_ip',
                      default=False, help='update resource file "domain_ip"')

    (options, args) = parser.parse_args()

    action = options.action
    pcap_file = options.pcap_file
    url = options.url
    whole_site = options.whole_site
    net_interface = options.interface
    sniff_caps_count = options.sniff_caps_count
    sniff_time = options.sniff_time
    save_pcap = options.save_pcap
    update_ip = options.update_ip
```

输出帮助  
```python
parser.print_help()  
```

输出用法  
```python
parser.print_usage()
```

`%prog` 可用来替换当前文件名  


2019/12/18  
