# @Author: Paolo Rosettani
# @Date: 24/05/2021 (DD/MM/YYY)
#
# @Description:
# This code receive any kind of message received from an external MIDI device (like a Cymatic)
# Forward the received MIDI message to a loopMIDI channel with an addition MIDI command that trigger
# the play button on "LivePrompter".
#
# For build the .exe run: 
# pyinstaller --clean --onefile --icon ananas.ico .\AutoPlayer.py

import mido # MIDI library
import mido.backends.rtmidi # Necessary for build the .exe
import time

#outputMIDIport = 'Microsoft GS Wavetable Synth 0'
outputMIDIport = 'APC MINI 1'
inputMIDIport = 'APC MINI 0'

try:
    outport = mido.open_output(outputMIDIport, autoreset=True) # Open output MIDI port
    time.sleep(1)
    inport = mido.open_input(inputMIDIport, autoreset=True) # Open input MIDI port
    print('Connected to APC MINI.')

    print()
    print('>>> Waiting MIDI message...')

    while True:
        msg = inport.receive() # Read MIDI message received from Cymatic
        local_time = time.ctime(time.time()) # Timestamp
        
        outport.send(msg) # Forward message to Live Prompter
        #time.sleep(0.001) # LivePrompter needs time to load the song
        
        print(msg, '  \t@', local_time)
        

except:
    print('ERROR')
    print('Unable to open MIDI port(s)!')
    print()
    print('MIDI ports available:')
    print('INPUT:\t', mido.get_input_names())
    print('OUTPUT:\t', mido.get_output_names())
    print()
    input('Close this window or press Enter to Exit.')
