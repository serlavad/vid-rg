class ScenePerformerEntity:
    def __init__(self, id, name, scene_id):
        self.performer_id, self.name, self.scene_id = id, name, scene_id

    def __repr__(self):
        return f"ScenePerformerEntity({self.performer_id}, {self.name}, {self.scene_id})"

def convert_scene_performer_entities(rows: list[tuple]) -> list[ScenePerformerEntity]:
    return list(map(convert_scene_performer_entity, rows))


def convert_scene_performer_entity(row: tuple) -> ScenePerformerEntity:
    id, name, scene_id = row
    return ScenePerformerEntity(id, name, scene_id)
