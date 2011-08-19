import settings

def discovery(status, test):
    for d in settings.discovery:
        servers = d().get_servers() # [('ip', 'host')]
        for server in servers:
            ip = server[0]
            if ip not in status['servers']: # do discovery
                status['servers'][ip] = {}
                print 'performing discovery on', server
                for t in test:
                    t.discover(ip, status['servers'][ip])
            status['servers'][ip]['hostname'] = server[1]
