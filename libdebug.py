DEBUG = True
def debug(*args,**kw):
    if not DEBUG:
        return
    print(*args,**kw)
def exec(func):
    if not DEBUG:
        return
    func()