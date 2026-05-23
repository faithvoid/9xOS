# 9xOS
Classic Windows 9x style themer and configuration utility for Raspberry Pi OS on the Raspberry Pi 4/5, to assist the user in setting up a pseudo-retro retro gaming PC on their SBC.

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=8GF4A3XS7ZHFY)

## External Components
- ![Pastel2K](https://github.com/faithvoid/Pastel2K) - Windows 9X/2K style themes, a few converted directly from compatible .theme files (will soon include 'Windows Theme Installer', a one-click solution to install Windows 2000 theme files directly on XFCE, no manual conversion required!)
- ![ARM64Binaries](https://github.com/faithvoid/ARM64Binaries) - A library of compiled ARM64 binaries for retro PC games.

## Parts Required
- Raspberry Pi 4/5 or similar ARM64-based SBC (this script specifically targets the Raspberry Pi OS flavour of Debian)
- (Optional) A 3.5mm to composite output cable for a Pi 4, a composite video cable soldered to the TV OUT pins a Pi 5, or a VGA666 adapter for the most authentic experience. No shame in just using HDMI if that's all that you've got, though. Be warned that if using an HDMI-to-VGA or HDMI-to-composite adapter, you may get quality or latency issues that wouldn't exist using the native output methods.
- Ideally a 64GB or larger microSD card, USB drive or SSD (early retro games may be small, but even installing about 15 or so games can fill up a 32GB microSD card really quick, so if you're using a 32GB microSD, I'd highly advise installing all of your games onto an external drive. Don't worry about R/W speeds too much, I'm using a crappy unbranded USB 2.0 stick I got for free from a corporate meeting and games from that era load lightning quick on it, it's only the write speeds that really suck on it). You can also symlink your ~/.wine folder to an external USB drive so that it doesn't take up any space on your actual partition itself.

## Installation
``` sudo apt install icoextract exe-thumbnailer smplayer audacious pidgin xfce4 xfce4-goodies innoextract cabextract msitools dosbox-x scummvm```

This will install SMPlayer and Audacious, a music and video player combination that can be themed to look like Winamp and classic Windows Media Player, icoextract and exe-thumbnailer to display and extract EXE thumbnails, Pidgin as an all-in-one retro-looking instant messaging client, XFCE4 + Goodies as the primary desktop environment for a lightweight 9x-style UI experience, and innoextract + cabextract + msitools for manually extracting .cab/.exe files for installers that won't play nicely with WINE (rare, but it happens! It's also faster to install certain games this way in my experience.)

To set XFCE4 as your primary desktop environment, run ``` sudo update-alternatives --config x-session-manager ``` and restart. If you're still not seeing XFCE4 on boot, try ``` sudo update-alternatives --config startxfce4 ```, and/or add "exec startxfce4" to ~/.xsession

Once all of that is configured, install Pi-Apps, and, via Pi-Apps, install WINE. The installer will ask you if you'd like to change your page file size, select "Yes", reboot your Pi, then run the Pi-Apps WINE installer again, and after about 10-15 minutes you'll have a fully functional instance of WINE ready to go!

Once you've installed WINE, type "winecfg" into your start menu, and set compatibility mode to "Windows XP" (not always necessary, but helpful, especially if you're only installing XP and prior games), and under Graphics, I'd advise setting an 800x600 virtual window (or one size below your native resolution). Some games will forcibly change your desktop resolution to the game's resolution, and this helps prevents that, as well as allowing you to play games that are lacking native windowed mode in windowed mode without installing custom DLLs like dgvoodoo2.

## Post Install
- If using a 1GB/2GB Pi model, you may want to install and configure ZRAM to improve Pi conditions under high memory load, I've done this on my Pi 5 and it works swimmingly (~350MB of RAM at idle in XFCE vs ~550-600MB without ZRAM) - https://linuxblog.io/raspberry-pi-performance-add-zram-kernel-parameters/
- For various ARM64 binaries of retro games for best performance, check out my ARM64Ports GitHub repository! https://github.com/faithvoid/ARM64Ports
- For retro messenger support, Pidgin is included in the default install script. You can use Retro AIM Server to connect to an AIM instance, connect to IRC chats, or install ```msn-pecan``` to connect to Escargot, an MSN Messenger private server. You can also use native builds of MSN Messenger (versions 3.0 and 4.0 have been tested and work with the Escargot Patcher), but note that MSN seems to use a LOT of memory in WINE, so I would not recommend using it on Pi systems with less than 2GB of RAM (on a 1GB Pi 5, having MSN in the background plus running other applications tends to crash the system, whereas Pidgin is lightweight and barely noticeable, even with several chats open).
- For web browsing, I'd recommend using Pale Moon over Firefox, especially on lower-end devices. It both looks closer to the 00s era of Firefox and runs much better on RAM-limited devices such as the 1GB Pi 4/5. Some websites may have issues, but most you'd visit on a system like this don't (for example, Newgrounds might give you a security error if browsing on an unknown IP, but if you visit Newgrounds on another device then revisit it on the Pi, it'll work just fine). 
- If VGA output is giving you issues, add the following to the end of /boot/firmware/cmdline.txt: "video=VGA-1:800x600@60"
- To use any Windows 9x/2x era theme you find online, run "Windows Theme Installer" from the terminal, point it towards the folder that contains your Windows ".theme" file, and watch as it automagically converts your theme to a Redmond97-based theme, complete with system sounds and custom cursors if found!
