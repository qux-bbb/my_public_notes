#!/usr/bin/bash

etc_crontab="/etc/crontab"
dir_path_list=( "/var/spool/cron" "/etc/cron.d" "/etc/cron.daily" "/etc/cron.hourly" "/etc/cron.monthly", "/etc/cron.weekly" )

# 需要使用sudo或者直接root执行
if [ $(id -u) -ne 0 ]
then
    echo "You need to use sudo command or root user to execute"
    exit
fi    

if [ -f $etc_crontab ]  # 若文件存在则输出路径
then
    echo "----------------------------------------"
    echo $etc_crontab
fi

for dir_path in ${dir_path_list[@]}
do
    if [ -d $dir_path ]  # 若文件夹存在
    then
        if [ "$(ls -A $DIR)" ]  # 若文件夹不为空
        then
            echo "----------------------------------------"
            if [ "$(command -v tree)" ]  # 如果存在tree命令，使用tree列出文件，否则使用ls列出文件
            then
                tree -a --noreport $dir_path
            else
                ls -A -R $dir_path
            fi
        fi
    fi
done
