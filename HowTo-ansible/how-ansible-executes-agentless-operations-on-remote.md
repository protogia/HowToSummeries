# How ansible executes agentless operations on remote-host

Executing a simple command in with verbosity-level=3 will show the steps. 

Execute the following and replace 'host' with the name of your host or 'all'

```
ansible host -m ping -vvv
```

### Main-Steps of ansible when executing one module
1. ansible creates temporary-dir on remote host

2. ansible creates a stand-alone-executable on remote-host with all given config-params

3. transfer the created stand-alone-executable to the created temporary-dir of the target and start it

4. remove the temporary-dir on remote-host 

