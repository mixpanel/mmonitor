class SoftLayer(object):
    def get_servers(self):
        import urllib2, json

        pass_mgr = urllib2.HTTPPasswordMgr()
        auth_handler = urllib2.HTTPBasicAuthHandler(pass_mgr)
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)
        url = 'https://api.softlayer.com/rest/v3/SoftLayer_Account/Hardware.json'
        pass_mgr.add_password('SoftLayer API', url, 'username', 'sl api key')
        headers = {
            'Accept': 'application/json',
        }
        request = urllib2.Request(url, headers=headers)
        response = json.load(urllib2.urlopen(request))

        for server in response:
            yield (server['primaryIpAddress'], server['hostname'])
