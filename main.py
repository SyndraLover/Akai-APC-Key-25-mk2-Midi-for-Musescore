import subprocess
import time
import sys
import itertools

#key_func="wtype"
key_func="xdotool"

hw_midi="hw:1,0,1"

color={"lighter_blue":"03","light_red":"04","light_green":"10","turquiose":"20","light_blue":"24","neon_blue":"29","dunno":"30","pink":"34","pinker":"38","dark_blue":"43","red":"48","green":"56","whiteish":"69"}
led_modes={"pulsing":"9a","blinking":"9e","low_light":"93","default":"96"}

apc_array=["20","21","22","23","24","25","26","27"]
apc_array=apc_array+["18","19","1a","1b","1c","1d","1e","1f"]
apc_array=apc_array+["10","11","12","13","14","15","16","17"]
apc_array=apc_array+["08","09","0a","0b","0c","0d","0e","0f"]
apc_array=apc_array+["00","01","02","03","04","05","06","07"]

############################################################################################################################# 8x5
# CHANGE HERE
color_array=["dark_blue","turquiose","light_blue","pinker","light_red","light_red","light_red","neon_blue"]
color_array=color_array+["dark_blue","turquiose","lighter_blue","pinker","lighter_blue","lighter_blue","light_red","light_green"]
color_array=color_array+["dark_blue","light_blue","lighter_blue","pinker","lighter_blue","lighter_blue","light_red","red"]
color_array=color_array+["dark_blue","light_blue","light_blue","light_blue","lighter_blue","lighter_blue","light_red","pink"]
color_array=color_array+["light_green","red","neon_blue","red","lighter_blue","lighter_blue","light_red","light_blue"]
#############################################################################################################################
# CHANGE HERE
func_conf=["7","Alt+period","Shift+v","Ctrl+d","Ctrl+9","Ctrl+7","Ctrl+6","Ctrl+Alt+1"]
func_conf=func_conf+["6","Alt+minus","Shift+o","","Shift+b","Ctrl+Shift+b","Ctrl+5","Ctrl+Alt+2"]
func_conf=func_conf+["5","Ctrl+period","Shift+s","","Ctrl+m","Ctrl+Shift+m","Ctrl+4","Ctrl+Alt+3"]
func_conf=func_conf+["4","period","Shift+n","m","asterisk","slash","Ctrl+3","Ctrl+Alt+4"]
func_conf=func_conf+["w","q","n","0","t","Shift+t","Ctrl+2","x"]
###########################################################################################################################

# UI BUTTONS
#################################################### red bottom and vertical green
ui_but=["40","41","42","43","44","45","46","47"]#——
ui_but=ui_but+["52","53","54","55","56","51"]# |
ui_but=ui_but+["5b","5d"]#play rec

#################################################
# CHANGE HERE
ui_func=["Alt+Up","Alt+Down","Ctrl+Left","Ctrl+Right","Left","Right","BackSpace","Ctrl+Shift+BackSpace"]#——Left>Right
ui_func=ui_func+["plus","equal","minus","Ctrl+Up","Ctrl+Down",""]# | top>bottom
ui_func=ui_func+["space","n"]# Play/Pause REC

#############
# BLINK ON PRESS
blink=["02","27","1f","17","0f"]

dynamic="23"

#################################################
A=list(zip(itertools.repeat("default"),apc_array,color_array,func_conf))#[LED_Mode,Button,colors,functions]
B=list(zip(ui_func,ui_but))#[UI_FUNCTIO,UI_BUTTON]

def wayland_xorg(f):
    if key_func=="wtype":
        new=[key_func,f]
        return new
    else:
        new=[key_func,"key",f]
        return new

def init():# A[led,button,color]
    for _ in A:#list(zip(apc_array,itertools.cycle(["light_green","lighter_blue","neon_blue","whiteish","pinker","pinker","red","dunno"]))):
        subprocess.run(["amidi","--send-hex",str(led_modes[_[0]])+str(_[1])+color[_[2]],"-p",hw_midi])
    for _ in ui_but:
        subprocess.run(["amidi","--send-hex","96"+str(_)+"45","-p",hw_midi])


def change_led(inp,key=True,set_mode="default"):

    mode=A[apc_array.index(cur_input)][0]
    button=A[apc_array.index(cur_input)][1]
    c=A[apc_array.index(cur_input)][2]
    func=A[apc_array.index(cur_input)][3]
    if mode=="blinking":
        subprocess.run(["amidi","--send-hex",str(led_modes["default"])+button+color[c],"-p",hw_midi])
        mode="default"
    else:
        subprocess.run(["amidi","--send-hex",str(led_modes[set_mode])+button+color[c],"-p",hw_midi])
        mode=set_mode
    if key:
        subprocess.run(wayland_xorg(func))
    return [mode,button,c,func]
       
init()
with open("test.log", "w") as f:
    process = subprocess.Popen(["amidi","--dump","-p",hw_midi], stdout=subprocess.PIPE)
    # replace "" with b"" for Python 3
    for line in iter(process.stdout.readline, ""):
        #sys.stdout.write(str(line))
        cur=str(line)[2:8]
        if str(line)[2:4]=="90":
            if str(cur).split(" ")[1].lower() in ui_but:
                cur_input=str(cur).split(" ")[1].lower()
                B[ui_but.index(cur_input)][0]

                subprocess.run(wayland_xorg((str(B[ui_but.index(cur_input)][0]))))
                
                subprocess.run(["echo",str(B[ui_but.index(cur_input)])])

            else:
                cur_input=str(cur).split(" ")[1].lower()

                #if cur_input in ["27","1f","17","0f"]:
                #    for _ in ["27","1f","17","0f"]:
                #        A[apc_array.index(_)]=change_led(_,key=False,set_mode="default")
                #
                if cur_input in blink:
                    A[apc_array.index(cur_input)]=change_led(cur_input,set_mode="blinking")
                else:
                    A[apc_array.index(cur_input)]=change_led(cur_input)

                subprocess.run(["echo",str(A[apc_array.index(cur_input)])])
