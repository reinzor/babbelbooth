# babbelbooth
Babbelbooth, Selfiebooth the next gen ..

# Installation 

## HOW-TO Install Kivypie from scratch

Download Kivypi:

    http://kivypie.mitako.eu/kivy-download.html

Flash it on an sd card using:

    http://www.tweaking4all.nl/download/raspberrypi/ApplePi-Baker.zip

Insert the sd card into the pi and login with the following credentials:

    username: sysop
    password: posys

Fix the locales using:

    sudo vim /etc/default/locales

Add the following line:

    LC_ALL=en_US.UTF-8

Add a new user:
 
    sudo adduser rein

Add user to the sudoers group:

    sudo adduser rein sudo

Set-up your wifi network:

    sudo vim /etc/network/interfaces

Configure your wifi:

    allow-hotplug wlan0
    iface wlan0 inet dhcp
      wpa-ssid <YOUR SSID>
      wpa-psk <YOUR PASSWD>

Restart networking:

    sudo ifdown wlan0
    sudo ifup wlan0

Connect via ssh to the assigned IP by DHCP
