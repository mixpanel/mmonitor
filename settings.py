from discovery import softlayer, rackspace
from tests import mongo, arb, memcache

discovery = [softlayer.SoftLayer, rackspace.Rackspace]
tests = [mongo.Mongo, arb.Arb, memcache.Memcache]

exclude = ['tim', 'suhail', 'raylu', 'avery', 'carl', 'anlu', 'eric']

smtp_host = 'localhost'
from_addr = 'mmonitor@corp.mixpanel.com'
to_addr = 'servers@example.com'
