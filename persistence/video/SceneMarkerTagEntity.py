class SceneMarkerTagEntity:
    def __init__(self, scene_marker_id: int, tag_id: int, name: str):
        self.scene_marker_id = scene_marker_id
        self.tag_id = tag_id
        self.name = name

    def __repr__(self):
        return f"SceneMarkerTagEntity({self.scene_marker_id}, {self.tag_id}, {self.name})"


def convert_scene_marker_tag_entities(rows: list[tuple]) -> list[SceneMarkerTagEntity]:
    return list(map(convert_scene_marker_tag_entity, rows))

def convert_scene_marker_tag_entity(row: tuple):
    scene_marker_id, tag_id, name = row
    return SceneMarkerTagEntity(scene_marker_id, tag_id, name)
