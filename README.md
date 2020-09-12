# AirportSignIn
基于selenium的机场签到python脚本  
如果你的机场，在网页底部能够找到**Powered by SSPANEL  Theme by editXY**，则可以使用这个脚本进行自动签到。  

## 第一步
其中`name`是机场名称，可以随便填，`url`是机场登录网址，一般为**https://xxxx.xxx/auth/login** ，`account`是账号，`password`是密码，可以按照列表的样式添加多个。
```
URL=[
    {
        'name':'xxxxx',
        'url':'xxxxxxxxxxxxxxxxxxxxxxx',
        'account':'xxxxxxxxxxxxxxxxxxxxxx',
        'password':'xxxxxxxxxxxxxxxxxxx'
    }
]
```  
## 第二步
需要下载一个chromedriver，并更换成自己的路径  
`driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=chrome_options)  # 这里换成自己chromedriver的路径`  
## 第三步
需要申请一个邮箱（建议163邮箱），我这里是用的163邮箱，然后获取邮箱的授权码，填上自己的邮箱，执行完毕后会发一封邮件到你的邮箱中。
```
msg_from = 'xxxxxxxxxxxxxxxxx'  # 发送方邮箱
passwd = 'xxxxxx'  # 填入发送方邮箱的授权码
msg_to = 'xxxxxxxxxxxxxxxxxxxx'  # 收件人邮箱
```
