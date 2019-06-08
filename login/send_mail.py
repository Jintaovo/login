import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    send_mail(
        '来自本科一班song的测试邮件',
        '欢迎访问',
        '1712421071@qq.com',
        ['909312994@qq.com'],
    )