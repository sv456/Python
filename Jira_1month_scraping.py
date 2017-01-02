import requests
url='https://jira.successfactors.com/secure/Dashboard.jspa'
values={'username':'os_username','password':'os_password'}
r=requests.post(url,data=values)
print r.content

