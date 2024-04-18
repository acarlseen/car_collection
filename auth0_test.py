# this gets a token from Auth0, can save token to user DB
# will want to put client_id and Secret in .env

import http.client

conn = http.client.HTTPSConnection("dev-srlwsnr657fk16zf.us.auth0.com")

payload = "{\"client_id\":\"YlqsST7M35HmdJKnRmJQzu6SSjkGFEKh\",\"client_secret\":\"D8QOBypijjlAFjJ6rq3yJvqMxeassq_i9UNcifeuuYkRDWSc9jjAw7BdzS0IpKiW\",\"audience\":\"car-collection/api\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))