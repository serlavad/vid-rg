from domain.video.VideoMarker import VideoMarker, VideoMarkerDetails
from domain.video.VideoWithMarkers import VideoWithMarkers


class TagService:

    # TODO: maybe delete once we have the next one
    def group_markers_by_tag(self, videos: list[VideoWithMarkers]) -> dict[str, list[VideoMarkerDetails]]:
        markers_by_tag: dict[str, list[VideoMarkerDetails]] = {}
        for video in videos:
            for marker in video.get_marker_details():
                markers_by_tag = self.__add_or_append_marker(markers_by_tag, marker.tag, marker)
                for secondary_tag in marker.secondary_tags:
                    markers_by_tag = self.__add_or_append_marker(markers_by_tag, secondary_tag, marker)
        return markers_by_tag

    def __add_or_append_marker(
            self,
            markers_by_tag: dict[str, list[VideoMarkerDetails]],
            tag: str,
            marker: VideoMarkerDetails):

        if tag in markers_by_tag.keys():
            markers_by_tag.get(tag).append(marker)
        else:
            markers_by_tag.setdefault(tag, [marker])
        return markers_by_tag
