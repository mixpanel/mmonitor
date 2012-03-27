import settings, logging
from eventlet.greenpool import GreenPool

def discovery(status, test):
    pool = GreenPool(size=500)
    for d in settings.discovery:
        servers = d().get_servers() # [('ip', 'host')]
        for server in servers:
            ip = server[0]
            host = server[1]
            if host in settings.exclude:
                continue
            if host not in status['servers']: # do discovery
                status['servers'][host] = {}
                logging.info('performing discovery on %r', server)
                for t in test:
                    pool.spawn_n(t.discover, ip, status['servers'][host])
            status['servers'][host]['ip'] = ip
    pool.waitall()
