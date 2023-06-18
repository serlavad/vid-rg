from pprint import pprint

from config import PATHS
from domain.tag.TagService import TagService
from domain.video.VideoCutterService import VideoCutterService
from domain.video.VideoService import VideoService
from domain.video.VideoWithMarkers import VideoWithMarkers


class VideoManager:
    def __init__(self):
        self._video_service = VideoService()
        self._tag_service = TagService()
        self._video_cut_service = VideoCutterService("{}/stashapp".format(PATHS.HOME),
                                                     "{}/stashapp/".format(PATHS.HOME))

    def generate_all_samples(self, print_videos=False):
        videos_with_markers = self._video_service.get_all_videos_with_markers()
        print_videos and pprint(videos_with_markers)
        _generate_all_samples(videos_with_markers)

    def generate_tag_images(self, print_videos=False):
        videos_with_markers = self._video_service.get_all_videos_with_markers()
        print_videos and pprint(videos_with_markers)
        markers_by_tag = self._tag_service.group_markers_by_tag(videos_with_markers)
        self._video_cut_service.generate_tag_images(markers_by_tag)


def _generate_all_samples(videos: list[VideoWithMarkers]):
    video_cutter = VideoCutterService("{}/stashapp".format(PATHS.HOME), "{}/stashapp/cuts".format(PATHS.HOME))
    for video in videos:
        video_cutter.generate_samples(video)
