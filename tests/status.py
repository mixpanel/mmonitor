import urllib2
from datetime import datetime

from test import Test

class Status(Test):
    def __init__(self, email):
        super(Status, self).__init__(email)
        self.name = 'status'

    def test(self, host, status):
        oldstatus = status[self.name]
        if self.is_up(status['ip']):
            status[self.name] = 'up'
        else:
            status[self.name] = 'down'

        if status[self.name] != oldstatus:
            self.email.add('%s status.mixpanel.com status change: %s -> %s' % (host, oldstatus, status[self.name]))

    def discover(self, ip, status):
        return False # this must be added manually to status.json

    def is_up(self, ip):
        try:
            response = urllib2.urlopen('http://status.mixpanel.com', timeout=5)
            last_mod = response.headers['last-modified']
            last_mod_date = datetime.strptime(last_mod, '%a, %d %b %Y %H:%M:%S %Z')
            delta = datetime.now() - last_mod_date

            if delta.seconds < 300:
                return True
        except:
            pass
