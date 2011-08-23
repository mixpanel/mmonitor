import pymongo

from test import Test

class Mongo(Test):
    def __init__(self, email):
        super(Mongo, self).__init__(email)
        self.name = 'mongo'

    def test(self, ip, status):
        for port in status[self.name]:
            try:
                result = self.get_status(ip, port)
            except Exception as e:
                status[self.name][port] = 'error'
                continue

            oldstatus = status[self.name][port]
            status[self.name][port] = self.parse_status(result)
            if status[self.name][port] != oldstatus:
                self.email.add('%s:%s mongo status change: %s -> %s' % (status['hostname'], port, oldstatus, status[self.name][port]))

    def discover(self, ip, status):
        s = {}
        for port in ['27017', '27018', '27019']: # db, arbiter, config
            try:
                s[port] = self.parse_status(self.get_status(ip, port))
            except pymongo.errors.AutoReconnect:
                pass
        if s:
            status[self.name] = s

    def get_status(self, ip, port):
        conn = pymongo.Connection(ip, int(port), max_pool_size=1, network_timeout=5)
        db = conn.local
        result = db.command('isMaster')
        conn.disconnect()
        return result

    def parse_status(self, result):
        if result['ismaster']:
            return 'primary'
        elif result['secondary']:
            return 'secondary'
        else:
            return 'error'
