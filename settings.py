from discovery import softlayer
from tests import mongo, arb, memcache

discovery = [softlayer.SoftLayer]
tests = [mongo.Mongo, arb.Arb, memcache.Memcache]

smtp_host = 'localhost'
from_addr = 'mmonitor@corp.mixpanel.com'
to_addr = 'servers@example.com'
