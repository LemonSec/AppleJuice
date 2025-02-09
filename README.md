# AppleJuice
**Apple BLE Proximity Pairing Message Spoofing**


# Disclaimer

These scripts are an experimental PoC that uses Bluetooth Low Energy (BLE) to send proximity pairing messages to Apple devices.

This project is created for educational purposes and cannot be used for law violation or personal gain.
The author of this project is not responsible for any possible harm caused by the materials of this project.

# About This Project

This was created in response to the various AppleTV spoof messages being sent out during [DEF CON 31](https://techcrunch.com/2023/08/14/researcher-says-they-were-behind-iphone-popups-at-def-con/). After experiencing it first hand, I had to figure out what was happening. The existing research projects I could find *see credits* had great info but were both a couple years out of date with broken package dependancies, so I decided to take what I could from them and start building from there. 

*This is a work in progress, its only been two weeks since it was launched / showcased at DEF CON and I think I've made some decent progress in getting this working as simply as posible for everyone.  I'll eventually go back and re-work some of the more technical parts of the original projects but wanted to get something fun out there that people can start playing with right away.*

# Hardware Requirements

To run these scripts you need a Linux machine with an internal Bluetooth card or a USB Bluetooth adapter.

All original testing was done on a Lenovo T480 with a built-in Bluetooth adapter.\
Later tested on Raspberry Pi 3B+ running Kali Linux with a [Zexmte Long Range USB Bluetooth 5.1 Adapter with Dual Antenna](https://zexmte.com/collections/bluetooth-adapter/products/plug-play-long-range-bluetooth-5-1-usb-adapter).<br><br>

<img src="https://github.com/ECTO-1A/AppleJuice/assets/112792126/a6f2b9fa-ca26-45c1-a440-681beb55c76e" width="300"><br><br>


With the Lenovo computer running Kali Linux using the internal Bluetooth, the messages would only reach devices within a couple feet of the machine. 

With the Raspberry Pi and long range Bluetooth adapter, I'm able to get 20+ feet of range indoors in an area with loads of BLE traffic and noise. Outdoor range should be much greater but remains to be tested.

# Installation Instructions
Please follow in this exact order or you might run into issues with bluetooth dependencies.

**Clone the Main Repo**\
`git clone https://github.com/LemonSec/AppleJuice.git && cd ./AppleJuice`

**Install dependancies**\
`sudo apt update && sudo apt install -y bluez libpcap-dev libev-dev libnl-3-dev libnl-genl-3-dev libnl-route-3-dev cmake libbluetooth-dev`

**Install pybluez && pycryptodome**\
The pybluez library is broken on Github and needs to be installed manually
  - download the latest version from `pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez`
  - pycrypto is not maintained but you can install pycryptodome and it will work `pip install pycryptodome`

**Install Requirements**\
`sudo pip install -r requirements.txt`

**To Run Scripts Without Sudo**\
To be able to run without sudo, you need to set the capabilities of the python binary to allow it to access raw sockets. This is done with the following command:

`sudo setcap cap_net_raw,cap_net_admin+eip $(eval readlink -f $(which python))`


# Usage

Before running the script, check that your Bluetooth adapter is connected and showing as `hci0`\
Run `hcitool dev` to get a list of connected adapters
```
hcitool dev
Devices:
    hci0    00:00:7C:00:3A:13
```
*If the adapter is showing as* `hci1` *you will need to edit the* `dev_id` *variable in the scripts to match*
To update all scripts to hci1, CD to the scripts folder and run the following bash one liner

`find ./ -name "*.py" -exec sed -i 's/dev_id = 0/dev_id = 1/g' {} +`

# Examples
For a list of available scripts run `python menu.py` and select the number for the script you'd like to execute.

![menu](https://github.com/LemonSec/AppleJuice/assets/33465511/9c526633-ae74-4ffd-903e-a6448b5749f5)

**beatssolopro.py**

Model: Airpods
This script is used to send BLE pairing messages to Apple devices.


<img src="https://github.com/ECTO-1A/AppleJuice/assets/112792126/c3218a09-7aef-483b-957d-f3c19a55fc08" width="300">

**airpods_max.py**

Model: Airpods Max

<img src="https://github.com/ECTO-1A/AppleJuice/assets/112792126/5eea40e8-d7c1-4324-9f3d-1425228d0458" width="300">

# Credit

Credit to:
-The original author of the repo. I just forked it and added some quality of life updates for myself
https://github.com/ECTO-1A/AppleJuice
- [FuriousMAC](https://github.com/furiousMAC/continuity) and [Hexway](https://github.com/hexway/apple_bleee) for all the prior research on Apple BLE, Continuity, and building the Wireshark disector.
- [Jae Bochs](https://infosec.exchange/@jb0x168/110879394826675242) for [exposing this to me at DEF CON 31](https://techcrunch.com/2023/08/14/researcher-says-they-were-behind-iphone-popups-at-def-con/) which made me jump into learning about BLE.
- Guillaume Celosia and Mathieu Cunche for reverse engineering Proximity Pairing 
<a
href="https://petsymposium.org/2020/files/papers/issue1/popets-2020-0003.pdf">Discontinued
Privacy: Personal Data Leaks in Apple Bluetooth-Low-Energy Continuity
Protocols</a>.
