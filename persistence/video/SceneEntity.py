from typing import Tuple, List


class SceneEntity:
    def __init__(self, id: int, title: str, basename: str, duration: int, path: str):
        self.id = id
        self.title = title
        self.basename = basename
        self.duration = duration
        self.path = path

    def __repr__(self):
        return f"SceneEntity({self.title}, {self.basename})"


def convert_scene_entities(rows: list[tuple]) -> list[SceneEntity]:
    return list(map(convert_scene_entity, rows))


def convert_scene_entity(row: tuple):
    id, title, basename, duration, path = row
    return SceneEntity(id, title, basename, duration, path)
