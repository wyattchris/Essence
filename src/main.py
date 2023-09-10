import cv2 as cv
from video_processor import process_video
from music_generator import play_music

def main():
    # initialize the video capture (webcam)
    capture = cv.VideoCapture(0)

    # Set the duration of the capture in seconds
    capture_duration = 10  # for example, 10 seconds

    # Calculate the number of frames to capture based on the frame rate
    frame_rate = int(capture.get(cv.CAP_PROP_FPS))
    total_frames = frame_rate * capture_duration

    frame_count = 0

    while frame_count < total_frames:
        ret, frame = capture.read()
        if not ret:
            break

        # process the video frame and get the average brightness
        average_brightness = process_video(frame)

        # calculate main frequency based on brightness
        main_frequency = 60 + int(average_brightness)  # Adjust as needed

        # play music based on the main frequency
        play_music(main_frequency)

        # display the webcam feed
        cv.imshow("webcam! :3", frame)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break

        frame_count += 1

    capture.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
