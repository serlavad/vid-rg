from os import path

from domain.video.VideoPerformer import VideoPerformer


class VideoMarker:
    def __init__(self, tag="", secondary_tags: list[str] = [], rg_tags: list[str] = [], time=0):
        self.tag: str = tag
        self.secondary_tags: list[str] = secondary_tags
        self.rg_tags: list[str] = rg_tags
        self.time: int = time

    def __repr__(self):
        return f"VideoMarker(" \
               f"{self.time}, " \
               f"{self.tag}, " \
               f"[{', '.join(self.secondary_tags)}], " \
               f"[{', '.join(self.rg_tags)}]) "

    def to_filename(self) -> str:
        return str(self.time) + "_" + self.tag.replace(" ", "-").upper() + (
            "_" + "_".join(
                map(lambda secondary_tag: secondary_tag.replace(" ", "-"), sorted(self.secondary_tags))) if len(
                self.secondary_tags) else "")

    def to_rg_filename(self) -> str:
        return str(self.time) + "_" + "_".join(
            map(lambda rg_tag: rg_tag.replace(" ", "-").replace("/", "-"), sorted(self.rg_tags))) if len(
            self.rg_tags) else ""


class VideoMarkerDetails(VideoMarker):
    """Same as VideoMarker but also holds some of the parent video information"""

    def __init__(self):
        self.video_path: str = ""
        self.video_filename: str = ""
        self.video_markers: list[VideoMarker] = []
        self.video_performers: list[VideoPerformer] = []
        self.video_duration: int = 0
        self.scene_id: int = VideoMarker

    def __repr__(self):
        marker = VideoMarker(tag=self.tag, secondary_tags=self.secondary_tags, rg_tags=self.rg_tags, time=self.time)
        return repr(marker)

    def get_performers_as_string(self) -> str:
        return "_".join([performer.name.replace(" ", "") for performer in self.video_performers])

    def get_full_path(self) -> str:
        return path.join(self.video_path, self.video_filename)
