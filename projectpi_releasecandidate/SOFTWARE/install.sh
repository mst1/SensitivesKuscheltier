#!/bin/bash
#EXECUTE THIS AS ROOT
#Cleanup
rm /usr/projectpi/ -r
rm /usr/bin/projectpi
rm /etc/rc.local

#Copying new files
mkdir /usr/projectpi
tar -xf content.tar /usr/projectpi/
cp projectpi /usr/bin/
cp rc.local /etc/
chmod +x /usr/bin/projectpi
chmod +x /etc/rc.local