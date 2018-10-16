import webbrowser

url = "***"
chromepath = r"***"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
webbrowser.get('chrome').open(url")
