from sqlite3 import Connection

from persistence.video.SceneMarkerTagEntity import SceneMarkerTagEntity, convert_scene_marker_tag_entities


class SceneMarkerTagRepository:
    def __init__(self, con: Connection):
        self.con = con

    def get_scene_marker_tags(self, scene_marker_ids: list[str]) -> list[SceneMarkerTagEntity]:
        cur = self.con.cursor()
        res = cur.execute("""
        SELECT smt.scene_marker_id, smt.tag_id, t.name
        FROM scene_markers_tags smt
         JOIN tags t on smt.tag_id = t.id
        WHERE scene_marker_id IN ({scene_marker_ids})
        """.format(scene_marker_ids=",".join(map(str, scene_marker_ids))))

        return convert_scene_marker_tag_entities(res.fetchall())
