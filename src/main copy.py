import cv2 as cv
import time 
from video_processor import video_brightness
from video_processor import pixel_info 
from music_generator import create_midi_composition, play_note
from synth import createSynth, deleteSynth
import numpy as np

def main():
    # initialize the video capture (webcam)
    capture = cv.VideoCapture(0)
    '''try:
        capture.set(cv.CAP_PROP_FPS, 10)
    except:
        print("nope")'''
    #create synthesizer
    synth = createSynth(4.0)

    # Set the duration of the capture in seconds
    capture_duration = 3 # for example, 10 seconds

    # Calculate the number of frames to capture based on the frame rate
    frame_rate = int(capture.get(cv.CAP_PROP_FPS))
    print(frame_rate)
    total_frames = frame_rate * capture_duration
    frame_count = 0

    while frame_count < total_frames:
        ret, frame = capture.read()
        if not ret:
            break

        # process the video frame and get the average brightness
        average_brightness = video_brightness(frame)
        np.scale
        #detect face
        face = pixel_info(frame)
        

        # calculate main frequency and harmony intervals based on brightness
        main_frequency = 60 + int(average_brightness)  # Adjust as needed
        print(main_frequency)
        harmony_intervals = [1.5, 0.5]  # Adjust intervals as needed

        # generate MIDI composition
        #midi_composition = create_midi_composition(main_frequency, harmony_intervals)

        # play MIDI composition notes
        #cv.getGaborKernel(3.0,5.0,7.0,4.0)
       
        #NOTE THAT KEY RANGE IS BETWEEN 0 AND 96
        synth.noteon(0,400, 100)
        time.sleep(0.1)
        synth.noteoff(0,400)

        '''play_note(main_frequency, 64, 1)  # Play main melody
        for interval in harmony_intervals:
            harmony_note = round(main_frequency * interval) % 128
            play_note(harmony_note, 64, 0.5)'''  # Play harmony notes
        cv.imshow('my face', face)
        # display the webcam feed
        #cv.imshow("webcam! :3", frame)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break

        frame_count += 1

    capture.release()
    cv.destroyAllWindows()
    deleteSynth(synth)
    print('synth deleted')
if __name__ == "__main__":
    main()
