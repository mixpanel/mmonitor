from test import Test

class Memcache(Test):
    def __init__(self, email):
        super(Memcache, self).__init__(email)
        self.name = 'memcache'

    def test(self, host, status):
        oldstatus = status[self.name]
        if self.is_up(status['ip']):
            status[self.name] = 'up'
        else:
            status[self.name] = 'down'
        if status[self.name] != oldstatus:
            self.email.add('%s memcache status change: %s -> %s' % (status['hostname'], oldstatus, status[self.name]))

    def discover(self, ip, status):
        if self.is_up(ip):
            status[self.name] = 'up'
        # don't set status to down on discovery

    def is_up(self, ip):
        import socket
        try:
            sock = socket.create_connection((ip, 11211), timeout=5)
            sock.send('stats\n')
            if 'STAT accepting_conns 1' in sock.recv(1024):
                return True
            sock.close()
        except:
            pass
