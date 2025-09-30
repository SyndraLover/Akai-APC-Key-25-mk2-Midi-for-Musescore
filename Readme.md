# APC Key 25 mk2 Midi>keypresses
- Designed for Musescore4
- Musescore3 only with jackctl for Midi assignment
- Tested on Debian13

## Dependencies
- xdotool (Recommended) or wtype
- python3
- alsa-utils (amidi)
- git

## RUN
1. install dependencies
2. Run in terminal
```
    git clone https://github.com/SyndraLover/Akai-APC-Key-25-mk2-Midi-for-Musescore.git
    cd Akai-APC-Key-25-mk2-Midi-for-Musescore
    amidi -l
```
- You should see this
```
Dir Device    Name
IO  hw:1,0,0  APC Key 25 mk2 Keys
IO  hw:1,0,1  APC Key 25 mk2 Control
IO  hw:1,0,2  APC Key 25 mk2 MIDI 3
IO  hw:1,0,3  APC Key 25 mk2 MIDI 4
```
- Find `IO  hw:x,y,z  APC Key 25 mk2 Control`
- change hw_midi=hw:x,y,z in main.py. If not equal to hw:1,0,1
- change key_func=wtype if you use Wayland 
6. Start daemon in terminal 
``` 
python main.py
```
- `python3 main.py`
- `uv run main.py`
7. Launch Musescore4
8. import keybindings for xorg only.
9. Enable midi Input in Musescore. Only enabling the first input of Akai APC Key 25 mk2 Keys.
10. Focus Musescore Window and everything should work. You can see your inputs in terminal window.
## Customization
- change bindings in main.py
- change colors in main.py
- change append button to blink

## Current Layout
![Current Layout](Layout.png)
## Roadmap
- dynamic button that works without keyboard and mouse
- Voice exclusively blinks. If one is blinking every other should not
- key.conf in seperate file
- cli options (-d debugging -c config.file)
- Gui
- Windows port

## References
- https://github.com/sickcodes/xdotool-gui/blob/master/key_list.csv
- https://cdn.inmusicbrands.com/akai/attachments/APC%20Key%2025%20mk2%20-%20Communication%20Protocol%20-%20v1.1.pdf