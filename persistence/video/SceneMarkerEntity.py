from typing import Tuple, List


class SceneMarkerEntity:
    def __init__(self, name: str, seconds: int, scene_id: int, id: int):
        self.name, self.seconds, self.scene_id, self.id = name, seconds, scene_id, id

    def __repr__(self):
        return f"SceneMarkerEntity({self.name}, {self.seconds}, {self.scene_id})"


def convert_scene_marker_entities(rows: list[tuple]) -> list[SceneMarkerEntity]:
    return list(map(convert_scene_marker_entity, rows))


def convert_scene_marker_entity(row: tuple):
    name, seconds, scene_id, id = row
    return SceneMarkerEntity(name, seconds, scene_id, id)
