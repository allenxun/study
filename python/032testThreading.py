import threading,time

def update():
    print 1

def update_cycle():
    for i in xrange(5):
        t = threading.Timer(1,update)
        t.start()

update_cycle()
