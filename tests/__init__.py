def tests(status, test):
    for ip, s in status['servers'].iteritems():
        for t in test:
            if t.name in s:
                t.test(ip, s)
