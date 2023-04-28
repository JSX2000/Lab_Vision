import cv2 as cv
from video_classes import IterPerSec
from video_classes import putIterationsPerSec

from video_classes import VideoGet
from video_classes import VideoShow

# Dedicated thread for grabbing video frames with VideoGet object.
# Main thread shows video frames.
def threadVideoGet(source1, source2):
    video_getter1 = VideoGet(source1).start()
    video_getter2 = VideoGet(source2).start()
    (grabbed1, frame1) = (video_getter1.grabbed, video_getter1.frame)
    (grabbed2, frame2) = (video_getter2.grabbed, video_getter2.frame)
    itps1 = IterPerSec().start()
    itps2 = IterPerSec().start()
    video_show1 = VideoShow(video_getter1.frame, 'video1').start()
    video_show2 = VideoShow(video_getter2.frame, 'video2').start()

    while True:
        (grabbed1, frame1) = (video_getter1.grabbed, video_getter1.frame)
        (grabbed2, frame2) = (video_getter2.grabbed, video_getter2.frame)
        grabbed = grabbed1 and grabbed2
        stopped = video_show1.stopped and video_show2.stopped
        if not grabbed or stopped:
            video_show1.stop()
            video_show2.stop()
            video_getter1.stop()
            video_getter2.stop()
            break

        frame1 = putIterationsPerSec(frame1, itps1.itPerSec())
        frame2 = putIterationsPerSec(frame2, itps2.itPerSec())
        video_show1.frame = frame1
        video_show2.frame = frame2
        itps1.increment()
        itps2.increment()

def main():
    source1 = 2
    source2 = 0 
    threadVideoGet(source1, source2)

if __name__ == "__main__":
    main()
