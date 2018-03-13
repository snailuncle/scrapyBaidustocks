#centos7 systemctl list-unit-files          列出所有可用单元
#       vi /etc/my.cnf                      mysql配置文件
#       systemctl list-units                列出所有运行中单元
#           systemctl start mysqld          启动mysql
#           systemctl stop  mysqld         关闭mysql
        
#        
#        mysql -u username -p          登陆mysql
#        systemctl status mysqld        查看mysql服务的状态        
        
        
#        systemctl enable mysqld     自动启动
#       systemctl disable mysqld         关闭自动启动
        
        
#*启动、重启、停止、重载服务
# systemctl start httpd.service
# systemctl restart httpd.service
# systemctl stop httpd.service
# systemctl reload httpd.service
# systemctl status httpd.service
        
        
#*激活/禁止自动启动
## systemctl enable httpd.service
## systemctl disable httpd.service
#1
#2
#*杀死服务
## systemctl kill httpd

#       mv a b c d          把 a b c 三个文件移动到d目录中

#[mysqld_safe]
#log-error=/var/log/mysqld.log

#win7        net start myql                        开启sql   
#           mysql_secure_installation               mysql的安全选项

#           grant all on *.* to root@'%' identified by '123';       允许所有人登陆root用户使用密码123

