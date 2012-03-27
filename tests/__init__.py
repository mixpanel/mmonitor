from eventlet.greenpool import GreenPool

def tests(status, test):
    pool = GreenPool(size=500)
    for host, s in status['servers'].iteritems():
        for t in test:
            if t.name in s:
                pool.spawn_n(t.test, host, s)
    pool.waitall()
