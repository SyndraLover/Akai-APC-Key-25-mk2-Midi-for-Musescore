# APC Key 25 mk2 Midi>keypresses
    - Designed for Musescore4
    - Musescore3 only with jackctl for Midi assignment

## Dependencies
    - wtype (wayland)
    - xdotool (xorg)
    - python3
    - amidi
    - git

## RUN
    - install dependencies
    - git clone repo / copy main.py
    - cd repo
    - amidi -l 
        - Find IO  hw:x,y,z  APC Key 25 mk2 Control
        - change hw_midi=hw:x,y,z in main.py
    - change key_func in main.py for your Desktop
    - python main.py /python3 main.py / uv run main.py
    - Launch Mscore4

## Customization
    - change bindings in main.py
    - change colors in main.py

## Roadmap
    - key.conf in seperate file
    - Mask for non "blinking" led upon pressed
    - cli options

## References
    - https://cdn.inmusicbrands.com/akai/attachments/APC%20Key%2025%20mk2%20-%20Communication%20Protocol%20-%20v1.1.pdf