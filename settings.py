from discovery import softlayer
from tests import mongo, arb, memcache

discovery = [softlayer.SoftLayer]
tests = [mongo.Mongo, arb.Arb, memcache.Memcache]

exclude = ['tim', 'suhail', 'raylu', 'avery', 'carl', 'anlu', 'neil', 'peter']

smtp_host = 'localhost'
smtp_port = 25
smtp_tls = False
smtp_user = None
smtp_password = None
from_addr = 'mmonitor@monitor01.mixpanel.com'
to_addr = 'servers@example.com'
