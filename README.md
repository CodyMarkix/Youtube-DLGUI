# Youtube-DLGUI

A program that is basically youtube-dl but with a GUI!
This program exists for the people who are afraid of the terminal
but they can download software off of Github... whatever. ¯\_(ツ)_/¯

## Installing

### Buiding from source:

There are some requirements that neeed to be met. You need:

- Python 3 (3.10 is not reccomended)
- pyinstaller
- youtube_dl

Install [Python 3](https://www.python.org/downloads/release/python-399/) and the dependencies:

```
pip install pyinstaller youtube_dl
```

Download the git repository.

```
git clone https://github.com/CodyMarkix/Youtube-DLGUI
```

Then cd into the repository...

```
cd Youtube-DLGUI
```

cd into the folder where the binary is supposed to be built

```
cd bin/YoutubedlGUI-0.3_amd64/usr/bin
```

and build the program.

```
pyinstaller --onefile ../../../../src/youtubedlgui.py
```

### Installing the binary:

So far, the macOS binary is not yet included in the repo/releases. You need to build it yourself. Same with Arch/RedHat/Suse based Linux distros.

But, a binary for Debian is included. Click on the releases tab and find the latest release. Then click on the deb and it should be downloading. Then double click the downloaded deb and click install.

Alternatively, you can download the deb and do.

```
sudo dpkg -i YoutubedlGUI-0.3_amd64.deb
```