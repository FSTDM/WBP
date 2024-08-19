import base64
import json
import urllib.request

class GithubAPI():
    def __init__(self,user,repo):
        self.path = "https://api.github.com/repos/{}/{}/contents/".format(user,repo)
    def get(self,pPath = ""):
        jres = json.loads(urllib.request.urlopen("{}{}".format(self.path,pPath)).read().decode('utf-8'))
        return (jres["name"],jres["size"],base64.b64decode(jres["content"]))
    def dir(self,pPath = ""):
        jres = json.loads(urllib.request.urlopen("{}{}".format(self.path,pPath)).read().decode('utf-8'))
        result = []
        for entry in jres:
            result.append((entry["name"],entry["type"]))
        return result

x = GithubAPI("FSTDM","WBP")
print(x.dir())
print(x.get("index.py"))
