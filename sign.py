from selenium import webdriver
from time import sleep
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

URL=[
    {
        'name':'xxxxx',
        'url':'xxxxxxxxxxxxxxxxxxxxxxx',
        'account':'xxxxxxxxxxxxxxxxxxxxxx',
        'password':'xxxxxxxxxxxxxxxxxxx'
    },
    {
        'name':'xxxxx',
        'url':'xxxxxxxxxxxxxxxxxxxxxxx',
        'account':'xxxxxxxxxxxxxxxxxxxxxx',
        'password':'xxxxxxxxxxxxxxxxxxx'
    },
    {
        'name':'xxxxx',
        'url':'xxxxxxxxxxxxxxxxxxxxxxx',
        'account':'xxxxxxxxxxxxxxxxxxxxxx',
        'password':'xxxxxxxxxxxxxxxxxxx'
    }
]

startTime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def openChrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=chrome_options)  # 这里换成自己chromedriver的路径
    return driver

def getURL(driver):
    liuliangInfo=[]
    for info in URL:
        driver.get(info['url'])
        sleep(10)
        liuliangInfo.append(Login(info,driver))
    return liuliangInfo

def Login(info,driver):
    driver.find_element_by_id('email').send_keys(info['account'])
    driver.find_element_by_id('password').send_keys(info['password'])
    driver.find_element_by_css_selector('[type=submit]').click()
    sleep(3)
    try:
        driver.find_element_by_css_selector('[data-dismiss=modal]').click()
    except Exception as e:
        print(e)
        pass
    signFlow=''
    try:
        driver.find_element_by_xpath('//*[@id="checkin-div"]/a').click()    #签到
        sleep(10)
        signFlow=driver.find_element_by_id('swal2-content').text
    except:
        pass
    remainFlow=driver.find_elements_by_css_selector('[class=card-body]')[1].text
    usedFlow=driver.find_elements_by_css_selector('[class=card-stats]')[1].text
    return info['name']+'：'+'\n'+signFlow+'\n'+'剩余流量：'+remainFlow+'\n'+usedFlow+'\n'

def email(content):
    msg_from = 'xxxxxxxxxxxxxxxxx'  # 发送方邮箱
    passwd = 'xxxxxx'  # 填入发送方邮箱的授权码
    msg_to = 'xxxxxxxxxxxxxxxxxxxx'  # 收件人邮箱

    endTime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    subject = '机场签到信息'
    msg = MIMEText('运行开始时间：'+startTime+'\n'+content+'运行结束时间：'+endTime)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    s = None
    try:
        s = smtplib.SMTP_SSL("smtp.163.com", 465)  # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print(e)
    finally:
        s.quit()

if __name__ == '__main__':
    driver=openChrome()
    INFO=getURL(driver)
    info=''
    for i in INFO:
        info+=i+'\n'
    email(info)
