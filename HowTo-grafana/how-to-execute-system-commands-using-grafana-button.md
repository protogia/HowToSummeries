# how to execute systemcommands with grafana button


### hello world example
0. install button-plugin
In terminal:
```bash
sudo grafana-cli plugins install cloudspout-button-panel 
sudo systemctl restart grafana
```
Afterwards click reload in webbrowser  
1. Create button-panel
2. In settings of the buttonpannel edit Settings > REST integration > URL : http://localhost:3001/helloworld
3. save & exit

4. Open Terminal and create a python script working as grafana-endpoint like shown in grafana-expoint-example.py. Edit the redirect-url:
```python
  GNU nano 4.8                                                                               main.py                                                                                          
from simple_http_server import request_map
from simple_http_server import Redirect
import simple_http_server.server as server

import os

@request_map("/helloworld", method="GET")
def hello():
  try:
    os.system("echo 'hello world!'")
    return Redirect("localhost:3000/d/jdefQwnsnk/button-test-dashboard?orgId=1") # type the url of the grafana-dashboard containing the button
  except:
    raise HttpError(400, "Exception")

if __name__ == "__main__":
  server.start(host="localhost",port=3001)
```

5. Install simple_http_server from pypi 
```bash
pip3 install simple_http_sever
```

6. Run in Terminal and show output while clicking on the grafana endpoint
```bash
python3 run grafana-endpoint-example.py
```

