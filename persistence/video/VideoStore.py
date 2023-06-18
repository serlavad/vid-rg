import sqlite3
from operator import attrgetter

from domain.video.VideoWithMarkers import VideoWithMarkers
from persistence.video.SceneMarkerRepository import SceneMarkerRepository
from persistence.video.SceneMarkerTagRepository import SceneMarkerTagRepository
from persistence.video.ScenePerformerRepository import ScenePerformerRepository
from persistence.video.SceneRepository import SceneRepository
from config import SQLITE
from persistence.video.VideoWithMarkersEntityMapper import to_videos_with_markers




class VideoStore:
    def __init__(self):
        con = sqlite3.connect(SQLITE.DB_PATH)
        self.scene_repo = SceneRepository(con)
        self.scene_marker_repo = SceneMarkerRepository(con)
        self.scene_marker_tag_repo = SceneMarkerTagRepository(con)
        self.scene_performer_repo = ScenePerformerRepository(con)

    def get_all_videos_with_markers(self) -> list[VideoWithMarkers]:
        scenes = self.scene_repo.get_all_scenes()
        scene_ids = list(map(lambda scene: scene.id, scenes))
        scene_markers = self.scene_marker_repo.get_scene_markers(scene_ids)
        scene_secondary_markers = self.scene_marker_tag_repo.get_scene_marker_tags(list(map(attrgetter("id"), scene_markers)))
        scene_performers = self.scene_performer_repo.get_scenes_performers(scene_ids)

        scenes_with_markers = to_videos_with_markers(scenes, scene_markers, scene_secondary_markers, scene_performers)

        return scenes_with_markers

    def get_all_videos_with_markers_details(self) -> list[VideoWithMarkers]:
        scenes = self.scene_repo.get_all_scenes()
        scene_ids = list(map(lambda scene: scene.id, scenes))
        scene_markers = self.scene_marker_repo.get_scene_markers(scene_ids)
        scene_secondary_markers = self.scene_marker_tag_repo.get_scene_marker_tags(list(map(attrgetter("id"), scene_markers)))
        scene_performers = self.scene_performer_repo.get_scenes_performers(scene_ids)

        scenes_with_markers = to_videos_with_markers_details(scenes, scene_markers, scene_secondary_markers, scene_performers)

        return scenes_with_markers