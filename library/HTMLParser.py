from fake_useragent import UserAgent
import requests as req
import urllib.request as lib
class Parse:

    origin = 'https://survey.porsline.ir'

    def getLink(base):
        file = lib.urlopen(base)
        html = str(file.read())
        if html.find('</body>') < 0 :
            return (base, True)
        start = 'var url = window.location.origin + \\\''
        startIndex = html.find(start) + len(start)
        end = '\\\';\\n        xhttp.open'
        endIndex = html.find(end)
        script = html[startIndex:endIndex]
        url = Parse.origin + script
        file.close()
        return (url, False)

    def getDownload(url):
        (new_url , flag) = Parse.getLink(url)
        if flag:
            return new_url
        r = req.get(new_url, timeout=30, allow_redirects=True)
        last_url = str(r.content)[2:]
        return last_url

