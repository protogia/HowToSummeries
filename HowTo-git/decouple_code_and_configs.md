# How to decouple code and private configs in python-projects

1. install decouple
```sh
pip3 install python-decouple
```

2. create .evn file and write vars/secrets into it
```sh
echo "SECRET_EXAMPLE_KEY = \'myExampleKey0123456789abcdefghijklmnopqrstuvwxyz\'" >> .env
```

3. add .env to your .gitignore 
```sh
touch .gitignore         # if its not already created
echo ./.env .gitignore
```

4. import decouple in your python-programm and load the var/secret from your private .env file
```sh
from decouple import config

# ... some of your python code ...

SECRET_KEY = config.load("SECRET_KEY")

# ... some your python code
```

