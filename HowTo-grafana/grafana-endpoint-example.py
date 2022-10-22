from simple_http_server import request_map
from simple_http_server import Redirect
import simple_http_server.server as server

import os


@request_map("/helloworld", method="GET")
def hello():
  try:
    os.system("echo 'hello world!'")
    return Redirect("localhost:3000/d/jdefQwnsnk/button-test-dashboard?orgId=1") # edit this url to to the url of the dashboard containing the button
  except:
    raise HttpError(400, "Exception")

if __name__ == "__main__":
  server.start(host="localhost",port=3001)
