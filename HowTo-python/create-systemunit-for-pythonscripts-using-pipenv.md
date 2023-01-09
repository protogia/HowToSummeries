# How to start pythonscripts on boot using systemd and virtualenv

## Preconditions
If your workingdirectory contains a virtualenv, which was set up with:

```bash 
cd /home/user/path/to/workingdirectory/
pipenv shell
```

And you created a src-dir with an script you want to execute on boot, you can follow the instructions below

1. Create system-unit-file in `/etc/systemd/system/` called `your-servicename.service` and apply the location of your virtualenv (find out: `pipenv --where`)

```
[Unit]
Description=your-servicename

[Service]
Type=simple
User=user
WorkingDirectory=/home/user/path/to/workingdirectory/
ExecStart=/usr/bin/pipenv run path/to/your-virtualenv-name/bin/python /home/user/path/to/workingdirectory/src/your_script.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

2. After replacing with correct path and scriptname reload-unitfile-definitions and enable service for reboot
```bash
sudo systemctl daemon-reload 
sudo systemctl enable --now your-servicename.service
systemctl status your-servicename.service # should show activa & enabled
```
