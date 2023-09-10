import numpy as np
import soundfile as sf
import subprocess

def generate_chord(scale, chord_progression, chord_duration):
    combined_sound = np.zeros(int(chord_duration * 44100))

    for note in chord_progression:
        frequency = 440 * (2 ** ((note - 69) / 12))
        note_sound = np.sin(2 * np.pi * frequency * np.arange(0, chord_duration, 1/44100))
        combined_sound += note_sound

    return combined_sound

def apply_reverb(input_file, output_file):
    subprocess.run(["sox", input_file, output_file, "reverb", "50"])

def play_audio(audio_file):
    processed_sound, sr = sf.read(audio_file)
    sf.play(processed_sound, sr)

def play_music(main_frequency):
    scale = [main_frequency, main_frequency + 2, main_frequency + 3, main_frequency + 5, main_frequency + 7, main_frequency + 8, main_frequency + 10]
    chord_progressions = [
        [scale[0], scale[2], scale[4]],  # I chord
        [scale[1], scale[3], scale[5]],  # ii chord
        [scale[2], scale[4], scale[6]],  # iii chord
    ]

    # Generate and save the chord as a WAV file
    chord_duration = 2.0  # Longer duration for a more musical feel
    chord_sound = generate_chord(scale, chord_progressions[0], chord_duration)
    sf.write("output.wav", chord_sound, 44100)

    # Apply reverb using SoX
    apply_reverb("output.wav", "output_with_reverb.wav")

    # Play the processed audio using soundfile
    play_audio("output_with_reverb.wav")

# For testing
if __name__ == "__main__":
    play_music(440)  # Play a note of 440 Hz for testing
