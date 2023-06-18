from sqlite3 import Connection

from persistence.video.SceneEntity import convert_scene_entities, SceneEntity


class SceneRepository:
    def __init__(self, con: Connection):
        self.con = con

    def get_all_scenes(self) -> list[SceneEntity]:
        cur = self.con.cursor()
        res = cur.execute("""
        SELECT s.id, s.title, f.basename, vf.duration, fo.path
        from files f
         JOIN scenes_files sf on f.id = sf.file_id
         JOIN scenes s on sf.scene_id = s.id
         JOIN folders fo on f.parent_folder_id = fo.id
         JOIN video_files vf on f.id = vf.file_id
        WHERE s.organized = false
        """)

        return convert_scene_entities(res.fetchall())
