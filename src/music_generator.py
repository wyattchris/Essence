import mido as mido
import pygame as pygame
from mido import MidiFile, MidiTrack, Message
import numpy as np
import math
import time

class Instrument:
    def __init__(self, sampleRate, bitDepth):
        self.sampleRate = sampleRate
        self.bitDepth = bitDepth
        pygame.mixer.init(self.sampleRate, self.bitDepth)

    def stereo_sawtooth_wave(self, duration, frequency, sample_rate):
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        left_wave = 2 * (t * frequency - np.floor(t * frequency + 0.5))
        right_wave = left_wave * 0.5  # Generate a stereo waveform with a quieter right channel
        return np.column_stack((left_wave, right_wave))

    def stereo_sine_wave(self, duration, frequency, sample_rate):
        #samples
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        print(t)
        left_sin = np.sin(t) * np.pi * 100
        
        right_sin = left_sin
        return np.column_stack((left_sin, right_sin))

    def sinex(self, amp, time, frequency):
        sine_out = int(round(amp * math.sin(2 * math.pi * frequency * time)))
        return sine_out

    def sine(self, freq, duration = 1, speaker = None):
        num_samples = int(round(duration * self.sampleRate))

        #generate a buffer that is num_samples long and 2 channels wide
        sound_buffer = np.zeros((num_samples, 2), dtype=np.int16)
        amplitude = 2 ** (self.bitDepth - 1) - 1
        for sample_num in range(num_samples):
            t = float(sample_num) / self.sampleRate
            sine = self.sinex(amplitude, t, freq)
            if speaker == 'r': 
                sound_buffer[sample_num][1] = sine
            elif speaker == 'l':
                sound_buffer[sample_num][0] = sine
            else:
                sound_buffer[sample_num][1] = sine
                sound_buffer[sample_num][0] = sine
        sound = pygame.sndarray.make_sound(sound_buffer)
        sound.set_volume(1.0)
        sound.play(loops=1, maxtime=int(duration*1000))
        
        time.sleep(duration)


    def play_note(self, note_number, velocity, duration):
        midi_note = note_number + 21  # Adjust to the MIDI note range
        frequency = 440 * (2 ** ((midi_note - 69) / 12))
        
        
        
        # Generate a stereo waveform
        stereo_waveform = self.stereo_sine_wave(duration, frequency, 44100)


        mono_sine = self.sinex(duration, frequency)
        # Create a stereo Sound object
        sound = pygame.mixer.Sound(mono_waveform)

        sound.set_volume(velocity / 127.0)
        sound.play()

        pygame.time.wait(int(duration * 1000))  # Convert duration to milliseconds
        pygame.mixer.quit()
        pygame.quit()


    def create_midi_composition(main_frequency, harmony_intervals):
        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)

        # Add main melody note
        track.append(Message('note_on', note=60, velocity=64, time=0))
        track.append(Message('note_off', note=60, velocity=64, time=500))

        # Add harmonies based on intervals
        for interval in harmony_intervals:
            harmony_note = round(main_frequency * interval) % 128  # Wrap within 0-127 range
            track.append(Message('note_on', note=harmony_note, velocity=64, time=0))
            track.append(Message('note_off', note=harmony_note, velocity=64, time=500))
        return mid
    
    def quit(self):
        try:
            pygame.mixer.quit()
            pygame.quit()
            return True
        except:
            return False
    
nikIn = Instrument(44100,16)
nikIn.sine(440, duration = 1)