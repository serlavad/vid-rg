import sqlite3
from sqlite3 import Connection
from typing import List

class TagRepository:
    def __init__(self, con: Connection):
        self.con = con

    def getAllTags(self) -> List[str]:
        cur = self.con.cursor()
        res = cur.execute("SELECT name from tags")
        return res.fetchall()
    