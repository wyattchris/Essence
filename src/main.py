import cv2 as cv
import time
from video_processor import video_brightness
from music_generator import create_midi_composition, play_note
from synth import createSynth
from video_processor import pixel_info
import pygame
from music_generator import Instrument
import numpy as np

def main():
    #initialize pygame
    pygame.init()
    # initialize the video capture (webcam)
    capture = cv.VideoCapture(0)

    #instrument start
    sineGuy = Instrument(44100,32)    
    

    # Set the duration of the capture in seconds
    capture_duration = 0.1  # for example, 10 seconds

    # Calculate the number of frames to capture based on the frame rate
    frame_rate = int(capture.get(cv.CAP_PROP_FPS))
    total_frames = frame_rate * capture_duration
    frame_count = 0

    while frame_count < total_frames:
        ret, frame = capture.read()
        if not ret:
            break

        # process the video frame and get the average brightness
        average_brightness = video_brightness(frame)

        face = pixel_info(frame)
        # calculate main frequency and harmony intervals based on brightness
        
        main_frequency = 60 + int(average_brightness)  # Adjust as needed
        harmony_intervals = [1.5, 0.5]  # Adjust intervals as needed

        # generate MIDI composition
        midi_composition = create_midi_composition(main_frequency, harmony_intervals)
        n
        # play MIDI composition notes
        sineGuy.sine(10, 64, 0.5)  # Play main melody
        '''for interval in harmony_intervals:
            harmony_note = round(main_frequency * interval) % 128
            play_note(harmony_note, 64, 0.5)  # Play harmony notes'''

        # display the webcam feed
        cv.imshow("webcam! :3", face)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break

        frame_count += 1

    capture.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
