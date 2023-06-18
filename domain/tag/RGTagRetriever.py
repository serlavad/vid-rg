import os
from datetime import datetime
from re import sub

import redgifs
import snakecase


class RGTagRetriever:
    FILENAME = "latest_tags.txt"
    TAG_FILE = os.getcwd() + "/resources/" + FILENAME

    def __init__(self):
        self.api = redgifs.API()

    def get_tag_names(self) -> list[str]:
        tags = self.api.get_tags()
        return list(map(lambda tag: tag["name"], tags))

    def get_tags_to_file(self):
        print(self.TAG_FILE)
        with open(self.TAG_FILE, 'w') as f:
            for tag in self.get_tag_names():
                f.write(f"{tag}\n")

        os.rename(self.TAG_FILE,
                  self.compute_filename())

    def compute_filename(self):
        return os.path.dirname(self.TAG_FILE) + "/" + (datetime.today().strftime('%Y%m%d') + "-" + self.FILENAME)

    def generate_enum(self):
        self.get_tags_to_file()
        with open(self.TAG_FILE + "_enum", "w") as f_dest:
            with open(self.compute_filename(), 'r') as f_src:
                tags = [tag.replace("\n", "") for tag in f_src]
                tags.sort()
                for tag in tags:
                    f_dest.write(f"{snake_case(tag)} = \"{tag}\"\n")


def snake_case(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
                s.replace('-', ' ').replace('/', ' '))).split()).lower().replace('.', '')
