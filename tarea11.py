import cv2
import threading
from video_classes import IterPerSec
from video_classes import putIterationsPerSec

# Grab and show video frames without multithreading.
def video_thread(self, source=0):
    video_getter = cv2.VideoCapture(source)
    (grabbed, frame) = video_getter.read()
    itps = IterPerSec().start()

    while True:
        (grabbed, frame) = video_getter.read()
        if not grabbed or cv2.waitKey(1) == ord("q"):
            video_getter.release()
            break

        frame = putIterationsPerSec(frame, itps.itPerSec())
        cv2.imshow("Video", frame)
        itps.increment()

def main():
    source = 2
    threading.Thread(target=video_thread, args = (source,)).start()

if __name__ == "__main__":
    main()