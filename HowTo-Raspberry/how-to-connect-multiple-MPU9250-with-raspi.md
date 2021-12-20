# How to connect multiple MPU9250 with one Raspberry

## Problem
The standard usage of MPU9250 is in combination with i2c-bus. Even if i2c allows to communicate with multiple devices, you cant use more than 2 MPU9250 on the i2c-bus.
The Reason is that you can give this microchip only 2 adresses (0x68 and 0x69) by set its AD0-Pin High or low (shown below).

Therefore you need to use also the second i2c-bus or the SPI-Bus for more than 2 devices.

# Using the second i2c-bus to allow communication with up to 2 additional devices
The second i2c-bus (i2c-0) can be used by connecting SDA0 and SCL0 (Raspberry 3B+ Pin27 and Pin28)

1. Usually this is used to communicate with internal EEPROM and without internal resistors. Therefore you need to add additional 2kOhm pullup-resistors (pull up to 3.3V). (see sketch)

```
# DEVICE
3,3V	sda	scl	gnd
:	:	:	:
:--///--:       :       :
:---------///---:       :
:       :       :       :
:       :       :       :
3,3V    sda     scl     gnd
# Raspberry 3B+
```

2. Append the configuration to the end of `/boot/config.txt` by tiping into terminal:

```bash
sudo echo "dtparam=i2c_vc=on" >> /boot/config.txt
```

3. Reboot


