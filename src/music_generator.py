import mido as mido
import pygame as pygame
from mido import MidiFile, MidiTrack, Message
import numpy as np
import fluidsynth as fs

def stereo_sawtooth_wave(duration, frequency, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    left_wave = 2 * (t * frequency - np.floor(t * frequency + 0.5))
    right_wave = left_wave * 0.5  # Generate a stereo waveform with a quieter right channel
    return np.column_stack((left_wave, right_wave))

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

def play_note(note_number, velocity, duration):
    midi_note = note_number + 21  # Adjust to the MIDI note range
    frequency = 440 * (2 ** ((midi_note - 69) / 12))
    pygame.init()
    pygame.mixer.init()

    # Generate a stereo waveform
    stereo_waveform = stereo_sawtooth_wave(duration, frequency, 44100)

    # Create a stereo Sound object
    sound = pygame.mixer.Sound(stereo_waveform)

    sound.set_volume(velocity / 127.0)
    sound.play()

    pygame.time.wait(int(duration * 1000))  # Convert duration to milliseconds
    pygame.mixer.quit()
    pygame.quit()
