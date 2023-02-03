import mido
import keyboard

Array = []

Array = ['shift+0' for i in range(127)]

# Midi note 0 correspond to the lowest C, 61 to C3... Just add the desired notes.
# 'shift+0' will be typed by default if you play an unrenseigned note. See above in order to change that.

Array[0] = 'left'
Array[1] = 'right'
Array[2] = 'up'
Array[3] = 'down'
Array[4] = 'shift'
Array[5] = '0'


with mido.open_input() as inport:
    for msg in inport:
        if msg.type == 'note_on' :
            keyboard.press(Array[msg.note])
            print(msg.note)
        elif msg.type == 'note_off' :
            keyboard.release(Array[msg.note])
        else :
            pass
