import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'my_website.settings'

if __name__ == '__main__':

    send_mail(
        '来自www.yueminghai.top的测试邮件',
        'testest',
        'yueminghai6@163.com',
        ['1096164277@qq.com'],
    )