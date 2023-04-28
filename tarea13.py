import cv2 as cv
import threading
from video_classes import IterPerSec
from video_classes import putIterationsPerSec

from video_classes import VideoGet2
from video_classes import VideoShow

# Dedicated thread for grabbing video frames with VideoGet object.
# Main thread shows video frames.
def threadVideoGet(source1, source2):
    video_getter = VideoGet2(source1, source2).start()
    (grabbed, frame) = (video_getter.grabbed, video_getter.frame)
    video_show = VideoShow(frame).start()
    itps = IterPerSec().start()

    while True:
        (grabbed, frame) = (video_getter.grabbed, video_getter.frame)
        if not grabbed or video_show.stopped:
            video_show.stop()
            video_getter.stop()
            break

        frame = putIterationsPerSec(frame, itps.itPerSec())
        video_show.frame = frame
        itps.increment()

def main():
    source1 = 0
    source2 = 4 
    threadVideoGet(source1, source2)

if __name__ == "__main__":
    main()
