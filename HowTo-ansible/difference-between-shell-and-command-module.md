# When should I use command-module and when shell-module?

### command-module
The command-module is the default module of ansible. If you use an ad-hoc command you do not need to specify the module:

```
ansible all -m command -a 'df -h /
```

equals 

```
ansible all -a "df -h /"
```

It executes a given command directly without using the shell of a target-host! As a result you cant use shell-operators like '|,&,>,>>'

### shell-module
The shell-module is executing the given command through a shell on the target-host so you can use shell-operators

```
ansible all -m shell -a 'df -h / > out.txt
```
