# Trouble-shooting after pushing sensitive data to your GitHub-repo
1. Revoke your data/keys/credentials if its possible

2. Download bfg-repo-cleaner and add it to your sources
```sh
### download
wget https://repo1.maven.org/maven2/com/madgag/bfg/1.14.0/bfg-1.14.0.jar # This is just an example. Make sure to get the latest version.

# move to /opt directory for additional software
sudo mkdir /opt/bfg-repo-cleaner
sudo mv bfg*.jar /opt/bfg-repo-cleaner

# add alias like this
nano ~/.bashrc 
# write into alias-section: 
alias bfg ='/usr/bin/java -jar /opt/bfg-repo-cleaner/bfg-1.14.0.jar'
# save and close ~/.bashrc. Then type in into terminal
source ~/.bashrc
# if you open a new shell you can use the alias bfg to use your jar
```

3. Rewrite your git history  
```sh
### delete git-history
# run this command from root-dir of your repo.  this deletes the file in each commit 
# replaace the placeholders
sudo bfg --delete-files <file-to-delete> <your-github-repo-name>  

# run the following commands to push to the HEAD
sudo git reflog expire --expire=now --all
sudo git reflog expire --expire=now --al
git push --force origin
```
