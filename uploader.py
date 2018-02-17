import requests, sys

requests.post("http://192.168.1.1:8081/uploader.cgi", data=open(sys.argv[1], "rb").read())