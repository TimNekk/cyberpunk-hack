from win10toast import ToastNotifier


def show_notification(title: str, text: str):
    toaster = ToastNotifier()
    toaster.show_toast(title, text, duration=5, threaded=True)