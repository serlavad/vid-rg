from operator import attrgetter
from os import path

from domain.video.VideoMarker import VideoMarker, VideoMarkerDetails
from domain.video.VideoPerformer import VideoPerformer


class VideoWithMarkers:
    def __init__(self):
        self.path: str = ""
        self.filename: str = ""
        self.markers: list[VideoMarker] = []
        self.performers: list[VideoPerformer] = []
        self.duration: int = 0
        self.scene_id: int = 0

    def __repr__(self):
        return f"VideoWithMarkers(\n" \
               f"   {self.filename}, \n" \
               f"   {[repr(m) for m in self.markers]}\n" \
               f"   {[repr(p) for p in self.performers]}\n" \
               f"   {self.duration}\n" \
               f")"

    def get_sorted_performer_names(self) -> str:
        performer_names = map(attrgetter("name"), self.performers)
        return "-".join(sorted(performer_names))

    def get_markers_sorted_by_time(self) -> list[VideoMarker]:
        return sorted(self.markers, key=attrgetter("time"))

    def get_full_path(self) -> str:
        return path.join(self.path, self.filename)

    def get_marker_details(self) -> list[VideoMarkerDetails]:
        return [self.__to_marker_details(marker, self) for marker in self.markers]

    def __to_marker_details(self, marker: VideoMarker, video) -> VideoMarkerDetails:
        marker_details = VideoMarkerDetails()
        marker_details.tag = marker.tag
        marker_details.secondary_tags = marker.secondary_tags
        marker_details.rg_tags = marker.rg_tags
        marker_details.time = marker.time
        marker_details.video_path = video.path
        marker_details.video_filename = video.filename
        marker_details.video_performers = video.performers
        marker_details.video_markers = video.markers
        marker_details.video_duration = video.duration
        marker_details.scene_id = video.scene_id
        return marker_details