# How to start pythonscripts on boot using systemd and virtualenv

## Preconditions
If your workingdirectory contains a virtualenv, which was set up with:

```bash 
cd /home/user/path/to/workingdirectory/
virtualenv -p python3 .
```

And you created a src-dir with an script you want to execute on boot, you can follow the instructions below

1. Create system-unit-file in `/etc/systemd/system/` called `your-servicename.service`

```
[Unit]
Description=your-servicename

[Service]
Type=simple
User=user
WorkingDirectory=/home/user/path/to/workingdirectory/
ExecStart=/home/user/path/to/workingdirectory/bin/python3 /home/user/path/to/workingdirectory/src/your_script.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
Alias=servicename.service
```

2. After replacing with correct path and scriptname reload-unitfile-definitions and enable service for reboot
```bash
sudo systemctl daemon-reload 
sudo systemctl enable --now your-servicename.service
systemctl status your-servicename.service # should show activa & enabled
```
