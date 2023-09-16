import fluidsynth
import time
def createSynth(gain:float):
    filename = 'src\The_Ultimate Megadrive_Soundfont.sf2'
    fs = fluidsynth.Synth(gain=gain)
    fs.start()
    id = fs.sfload(filename)
    fs.program_select(0, id, 0, 2)
    return fs

def deleteSynth(synth:fluidsynth.Synth):
    try:
        synth.delete()
    except:
        raise('Could not delete synth object')

mySynth = createSynth(2.0)
#mySynth.bank_select(0, 1)
mySynth.noteon(0, 35, 100)
time.sleep(1)
mySynth.noteoff(0, 100)
deleteSynth(mySynth)
'''fs.set_reverb_level(100)
fs.noteon(0, 60, 30)'''
#time.sleep(1.0)
'''
fs.noteon(0, 63, 50)
fs.noteon(0, 67, 30)
fs.noteon(0, 70, 30)'''
#fs.noteon(0, 74, 30)
#fs.noteon(0, 76, 30)