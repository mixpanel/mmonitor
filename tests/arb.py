import urllib2

from test import Test

class Arb(Test):
    def __init__(self, email):
        import time

        super(Arb, self).__init__(email)
        self.name = 'arb'
        date = time.strftime('%Y-%m-%d')
        self.query = ':8000/query?project_id=3&to_date=%s&from_date=%s&selector=false' % (date, date)
        self.response = '{"status": "ok", "results": {"%s": 0}}\n' % date

    def test(self, ip, status):
        oldstatus = status[self.name]
        self.discover(ip, status)
        if status[self.name] != oldstatus:
            self.email.add('%s arb status change %s -> %s' % (status['hostname'], oldstatus, status[self.name]))

    def discover(self, ip, status):
        try:
            response = urllib2.urlopen('http://' + ip + self.query, timeout=5).read()
            if response == self.response:
                status[self.name] = 'up'
        except:
            pass
