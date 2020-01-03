#push-notification.py

from win10toast import ToastNotifier
hr=ToastNotifier()
hr.show_toast(title="alarm",msg="this is the message",icon_path="C:\\Users\\Y144510\\Desktop\\Python\\test.ico",duration=10)
