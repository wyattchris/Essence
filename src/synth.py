import fluidsynth
import time

fs = fluidsynth.Synth(gain=3.0)
fs.start()

fs.program_select(0, sfid, 0, 0)

fs.set_reverb_level(100)
fs.noteon(0, 60, 30)
#time.sleep(1.0)

fs.noteon(0, 63, 50)
fs.noteon(0, 67, 30)
fs.noteon(0, 70, 30)
#fs.noteon(0, 74, 30)

#fs.noteon(0, 76, 30)

time.sleep(1.0)

fs.noteoff(0, 60)
fs.noteoff(0, 72)
#fs.noteoff(0, 76)

time.sleep(1.0)

fs.delete()