class Rackspace(object):
    def get_servers(self):
        import urllib2, json

        url = 'https://auth.api.rackspacecloud.com/v1.0/'
        headers = {
            'X-Auth-User': 'username',
            'X-Auth-Key': 'rs api key',
        }
        request = urllib2.Request(url, headers=headers)
        info = urllib2.urlopen(request).info()
        url = info['X-Server-Management-Url'] + '/servers/detail'
        auth_token = info['X-Auth-Token']

        headers = {
            'Accept': 'application/json',
            'X-Auth-Token': auth_token,
        }
        request = urllib2.Request(url, headers=headers)
        response = json.load(urllib2.urlopen(request))

        for server in response['servers']:
            yield (server['addresses']['public'][0], server['name'])
