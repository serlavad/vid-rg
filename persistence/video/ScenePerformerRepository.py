from sqlite3 import Connection

from persistence.video.ScenePerformerEntity import convert_scene_performer_entities, ScenePerformerEntity


class ScenePerformerRepository:
    def __init__(self, con: Connection):
        self.con = con

    def get_scenes_performers(self, scene_ids: list[int]) -> list[ScenePerformerEntity]:
        cur = self.con.cursor()
        res = cur.execute("""
        SELECT p.id, p.name, scene_id
        FROM performers p
         JOIN performers_scenes ps on p.id = ps.performer_id
         JOIN scenes s on ps.scene_id = s.id
        WHERE scene_id IN ({scene_ids})
        """.format(scene_ids=",".join(map(str, scene_ids))))

        return convert_scene_performer_entities(res.fetchall())

