# Setup python-package: speechrecognition

You have to install the following packages. 

```bash
sudpo apt update
sudo apt install portaudio19-dev -y && pip3 install pyaudio
pip3 install pyttsx3==2.90
pip3 install SpeechRecognition==3.8.1
```

Test if it works by running the module. It will calibrate for a second and please you to say something. After you say some words, it will printout.
```bash
python3 -m speech_recognition
#...
#say something!
```


Sometimes theres a problem when running a python-script using speech_recognition in live-mode with jackd2. It throws the error "cannot allocate memory-error". Please try the following
```bash
# make suer jack2d is installed
sudo apt install jack2d

# add your username by replacing "yourusername" to audio-group
chmod -a -G audio yourusername

# set realtimepriority of audio-group and unlimit memorylock 
sudo echo "@audio	hard	rtprio	95" >> /etc/security/limits.conf
sudo echo "@audio	soft	rtprio	95" >> /etc/security/limits.conf
sudo echo "@audio	hard	memlock	unlimited" >> /etc/security/limits.conf
sudo echo "@audio	soft	memlock	unlimited" >> /etc/security/limits.conf

# after that logout and login again to apply changes. (or reboot)
  
# check the realtimepriority and limits
ulimit -l -r 
### should show: unlimited and rtprio 95

# set jack2d to active:
jack_control start
```

Now retry your script. It trys out each sound-handling-framework and then waits for your words...
