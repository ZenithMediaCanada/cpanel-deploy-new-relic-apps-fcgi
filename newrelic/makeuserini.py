#!/usr/bin/python
import sys, pwd, grp, os
import simplejson as json

rawData = sys.stdin.readlines()

hookdata = json.loads(rawData[0])

data = hookdata['data']
username = data['user']
domain = data['domain']
path = '/home/%s/public_html/.user.ini' % username

uid = pwd.getpwnam(username).pw_uid
gid = grp.getgrnam(username).gr_gid

file_content = """\
newrelic.appname = "%s"
""" % domain

with open(path, 'w') as f:
    f.write(file_content)

os.chown(path, uid, gid)
