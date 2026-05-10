# 9xOS
Classic Windows 9x style themer and configuration utility for Raspberry Pi OS on the Raspberry Pi 4/5, to assist the user in setting up a pseudo-retro retro gaming PC on their SBC.

## Parts Required
- Raspberry Pi 4/5 or similar ARM64-based SBC (this script specifically targets the Raspberry Pi OS flavour of Debian)
- (Optional) A 3.5mm to composite output cable for a Pi 4, a composite video cable soldered to a Pi 5, or a VGA666 adapter for the most authentic experience. No shame in just using HDMI if that's all that you've got, though. Be warned that using an HDMI-to-VGA or HDMI-to-composite adapter, you may get quality or latency issues that wouldn't exist using the native output methods.
- Ideally a 64GB or larger microSD card, USB drive or SSD (early retro games may be small, but even installing about 15 or so games can fill up a 32GB microSD card really quick, if using a 32GB microSD, I'd advise installing all games on an external drive). 

## Installation
``` sudo apt install icoextract exe-thumbnailer smplayer audacious pidgin xfce4 xfce4-goodies innoextract cabextract msitools ```
This will install SMPlayer and Audacious, a music and video player combination that can be themed to look like Winamp and classic Windows Media Player, icoextract and exe-thumbnailer to display and extract EXE thumbnails, Pidgin as an all-in-one retro-looking instant messaging client, XFCE4 + Goodies as the primary desktop environment for a lightweight 9x-style UI experience, and innoextract + cabextract + msitools for manually extracting .cab/.exe files for installers that won't play nicely with WINE (rare, but it happens! It's also faster to install certain games this way in my experience.)

To set XFCE4 as your primary desktop environment, run ``` sudo update-alternatives --config x-session-manager ``` and restart. If you're still not seeing XFCE4 on boot, try ``` sudo update-alternatives --config startxfce4 ```, and/or add "exec startxfce4" to ~/.xsession

Once all of that is configured, install Pi-Apps, and, via Pi-Apps, install WINE. The installer will ask you if you'd like to change your page file size, select "Yes", reboot your Pi, then run the Pi-Apps WINE installer again, and after about 10-15 minutes you'll have a fully functional instance of WINE ready to go!

Once you've installed WINE, type "winecfg" into your start menu, and set compatibility mode to "Windows XP" (not always necessary, but helpful, especially if you're only installing XP and prior games), and under Graphics, I'd advise setting an 800x600 virtual window (or one size below your native resolution). Some games will forcibly change your desktop resolution to the game's resolution, and this helps prevents that, as well as allowing you to play games that are lacking native windowed mode in windowed mode without installing custom DLLs like dgvoodoo2.

## Post Install
- For various ARM64 binaries of retro games for best performance, check out my ARM64Ports GitHub repository! https://github.com/faithvoid/ARM64Ports
