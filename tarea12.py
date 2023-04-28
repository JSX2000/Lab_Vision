import cv2 as cv
from video_classes import IterPerSec
from video_classes import putIterationsPerSec

from video_classes import VideoGet
from video_classes import VideoShow

# Dedicated thread for grabbing video frames with VideoGet object.
# Main thread shows video frames.
def threadVideoGet(source=0):
    video_getter = VideoGet(source).start()
    (grabbed, frame) = (video_getter.grabbed, video_getter.frame)
    itps = IterPerSec().start()
    video_show = VideoShow(frame).start()

    while True:
        (grabbed, frame) = (video_getter.grabbed, video_getter.frame)
        if not grabbed or video_show.stopped:
            video_show.stop()
            break

        frame = video_getter.frame
        frame = putIterationsPerSec(frame, itps.itPerSec())
        video_show.frame = frame
        itps.increment()

def main():
    source = 2
    threadVideoGet(source)

if __name__ == "__main__":
    main()
