from sqlite3 import Connection

from persistence.video.SceneMarkerEntity import convert_scene_marker_entities, SceneMarkerEntity


class SceneMarkerRepository:
    def __init__(self, con: Connection):
        self.con = con

    def get_scene_markers(self, scene_ids: list[int]) -> list[SceneMarkerEntity]:
        cur = self.con.cursor()
        res = cur.execute("""
        SELECT t.name, seconds, sm.scene_id, sm.id
        FROM scene_markers sm
         JOIN tags t on sm.primary_tag_id = t.id
        WHERE scene_id IN ({scene_ids})
        """.format(scene_ids=",".join(map(str, scene_ids))))

        return convert_scene_marker_entities(res.fetchall())
