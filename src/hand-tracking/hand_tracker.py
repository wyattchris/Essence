import cv2 as cv
import mediapipe as mp
from pydub import AudioSegment
from pydub.playback import play
import time as time

class hand_tracker():
    def __init__(self, mode=False, max_hands=2, detection_con=0.5, model_complexity=1, track_con=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.model_complexity = model_complexity
        self.track_con = track_con
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands, self.model_complexity,
                                        self.detection_con, self.track_con)
        self.mp_draw = mp.solutions.drawing_utils

    def hands_finder(self, image, draw=True):
        image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(image_rgb)

        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(image, hand_lms, self.mp_hands.HAND_CONNECTIONS)
        return image

    def position_finder(self, image, hand_no=0, draw=True):
        lm_list = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(hand.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])
            if draw:
                cv.circle(image, (cx, cy), 15, (255, 0, 255), cv.FILLED)
        return lm_list

def main():
    cap = cv.VideoCapture(1)
    tracker = hand_tracker()

    # Load WAV file using pydub & play audio :D
    audio = AudioSegment.from_file("audio/chords.wav")
    # play(audio)

    while True:
        success, image = cap.read()
        image = tracker.hands_finder(image)
        lm_list = tracker.position_finder(image)
        if len(lm_list) != 0:
            print(lm_list[4])

        cv.imshow("Video", image)

        # Exit the loop if the 'q' key is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()