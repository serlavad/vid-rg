from persistence.video.VideoStore import VideoStore


class VideoService:
    def __init__(self):
        self.video_store = VideoStore()

    def get_all_videos_with_markers(self):
        return self.video_store.get_all_videos_with_markers()
