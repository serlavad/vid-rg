from operator import attrgetter

from domain.helpers import flatmap, unique
from domain.tag.RGTagMap import RGTagMap
from domain.video.VideoMarker import VideoMarkerDetails
from domain.video.VideoWithMarkers import VideoWithMarkers, VideoMarker, VideoPerformer
from persistence.video.SceneEntity import SceneEntity
from persistence.video.SceneMarkerEntity import SceneMarkerEntity
from persistence.video.SceneMarkerTagEntity import SceneMarkerTagEntity
from persistence.video.ScenePerformerEntity import ScenePerformerEntity


def to_videos_with_markers(
        scenes: list[SceneEntity],
        markers: list[SceneMarkerEntity],
        secondary_markers: list[SceneMarkerTagEntity],
        performers: list[ScenePerformerEntity]) -> list[VideoWithMarkers]:
    markers_by_scene_ids = {}
    secondary_markers_by_scene_marker_id = {}
    performers_by_scene_ids = {}

    for marker in markers:
        if marker.scene_id in markers_by_scene_ids.keys():
            markers_by_scene_ids.get(marker.scene_id).append(marker)
        else:
            markers_by_scene_ids.setdefault(marker.scene_id, [marker])

    for secondary_marker in secondary_markers:
        if secondary_marker.scene_marker_id in secondary_markers_by_scene_marker_id.keys():
            secondary_markers_by_scene_marker_id.get(secondary_marker.scene_marker_id).append(secondary_marker)
        else:
            secondary_markers_by_scene_marker_id.setdefault(secondary_marker.scene_marker_id, [secondary_marker])
            markers_by_scene_ids.setdefault(marker.scene_id, [marker])

    for performer in performers:
        if performer.scene_id in performers_by_scene_ids.keys():
            performers_by_scene_ids.get(performer.scene_id).append(performer)
        else:
            performers_by_scene_ids.setdefault(performer.scene_id, [performer])

    return list(__build_video_with_markers(scene, markers_by_scene_ids, secondary_markers_by_scene_marker_id,
                                           performers_by_scene_ids) for scene in scenes)


def to_videos_with_markers_details(scenes, scene_markers, scene_secondary_markers, scene_performers):
    pass


def __resolve_performers(performer_entities: list[ScenePerformerEntity]):
    return list(__to_video_performer(performer_entity) for performer_entity in performer_entities)


def __to_video_performer(performer_entity: ScenePerformerEntity) -> VideoPerformer:
    performer = VideoPerformer()
    performer.name = performer_entity.name
    return performer


def __build_video_with_markers(scene: SceneEntity, markers_by_scene_ids, secondary_markers_by_scene_marker_id,
                               performers_by_scene_ids) -> VideoWithMarkers:
    video_with_markers = VideoWithMarkers()
    video_with_markers.filename = scene.basename
    video_with_markers.duration = int(scene.duration)
    video_with_markers.scene_id = scene.id
    video_with_markers.path = scene.path
    if markers_by_scene_ids.get(scene.id):
        video_with_markers.markers = __resolve_markers(markers_by_scene_ids.get(scene.id),
                                                       secondary_markers_by_scene_marker_id,
                                                       performers_by_scene_ids.get(scene.id))
    if performers_by_scene_ids.get(scene.id):
        video_with_markers.performers = __resolve_performers(performers_by_scene_ids.get(scene.id))
    return video_with_markers


def __resolve_markers(marker_entities: list[SceneMarkerEntity],
                      secondary_markers_by_scene_marker_id: dict[int, list[SceneMarkerTagEntity]],
                      performers: list[ScenePerformerEntity]):
    return list(
        __to_video_marker(marker_entity, secondary_markers_by_scene_marker_id.get(marker_entity.id), performers) for
        marker_entity
        in marker_entities)


def __to_video_marker(marker_entity: SceneMarkerEntity, secondary_markers: list[SceneMarkerTagEntity] = None,
                      performers: list[ScenePerformerEntity] = []):
    if secondary_markers is None:
        secondary_markers = []
    marker = VideoMarkerDetails()
    marker.time = int(marker_entity.seconds)
    marker.tag = marker_entity.name
    marker.secondary_tags = list(map(attrgetter("name"), secondary_markers))

    marker.rg_tags = flatmap(
        [RGTagMap.get(marker.tag),
         flatmap(map(lambda tag: RGTagMap.get(tag), marker.secondary_tags)),
         [RGTagMap.get(performer.name) for performer in performers]])

    return marker
