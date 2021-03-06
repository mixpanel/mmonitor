import urllib2

from test import Test

class Arb(Test):
    def __init__(self, email):
        import time
        import urllib

        super(Arb, self).__init__(email)
        self.name = 'arb'
        t = time.gmtime(time.time() - 3600 * 24)
        date = time.strftime('%Y-%m-%d', t)
        params = {
                'project_id': 3,
                'from_date': date,
                'to_date': date,
                'queries': '[{"selector":"false"}]',
            }
        self.query = ':8000/distributed-query?' + urllib.urlencode(params)
        self.response = '{"status":"ok","results":{"%s":0}}\n' % date

    def test(self, host, status):
        oldstatus = status[self.name]
        if self.is_up(status['ip']):
            status[self.name] = 'up'
        else:
            if oldstatus == 'up':
                status[self.name] = 'down 1'
            else:
                status[self.name] = 'down 2'
        if status[self.name] != oldstatus and (oldstatus == 'down 2' or status[self.name] == 'down 2'):
            self.email.add('%s arb status change: %s -> %s' % (host, oldstatus, status[self.name]))

    def discover(self, ip, status):
        if self.is_up(ip):
            status[self.name] = 'up'
        # don't set status to down on discovery

    def is_up(self, ip):
        try:
            response = urllib2.urlopen('http://' + ip + self.query, timeout=5).read()
            if response == self.response:
                return True
        except:
            pass
