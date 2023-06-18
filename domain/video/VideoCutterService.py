import os
import pathlib
import cv2
import sys
from os import path

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from domain.video.VideoMarker import VideoMarkerDetails
from domain.video.VideoWithMarkers import VideoWithMarkers

CLIP_DURATION = 60  # in seconds
GAP = 8 # in seconds
TAG_IMAGES_FOLDER = "tag-images"


class VideoCutterService:
    def __init__(self, src_folder: str, dest_folder: str, debug=True):
        self.src_folder = src_folder
        self.dest_folder = dest_folder
        self.debug = debug

    def generate_samples(self, video: VideoWithMarkers):
        final_dest_folder = path.join(self.dest_folder, video.get_sorted_performer_names())
        self._create_dir_if_not_exists(final_dest_folder)
        sorted_markers = video.get_markers_sorted_by_time()
        for i in range(0, len(sorted_markers)):
            marker = sorted_markers[i]
            end_time = self._compute_end_time(i, marker, sorted_markers, video)
            new_filename = self._compute_new_filename(marker, video)

            target_full_path = path.join(final_dest_folder, new_filename)
            self._cut_video(video.get_full_path(), marker.time, end_time, target_full_path)

    def _compute_end_time(self, i, marker, sorted_markers, video):

        if i == (len(sorted_markers) - 1):
            return min(marker.time + CLIP_DURATION, video.duration)
        else:
            return min(marker.time + CLIP_DURATION, sorted_markers[i + 1].time - GAP)

    def generate_tag_images(self, markers_by_tag: dict[str, list[VideoMarkerDetails]]) -> None:
        print(cv2.__version__)
        print(sys.path)
        for tag in markers_by_tag:
            final_basename = path.join(self.dest_folder, TAG_IMAGES_FOLDER, tag)
            if path.exists(final_basename):
                print(final_basename, "already exists, skipping...")
                continue

            for marker in markers_by_tag.get(tag):
                start_time = 2000
                interval_time = 2000
                nb_images = 20
                times = self._generate_times(interval_time, marker, nb_images, start_time)

                for time in times:
                    self._generate_image(tag, marker, time)

    def _generate_times(self, interval_time, marker, nb_images, start_time):
        init_time: float = marker.time * 1000 + start_time
        times = [init_time]
        for i in range(0, nb_images):
            times.append(times[i] + interval_time)
        return times

    def _generate_image(self, tag, marker, time: int):
        img_name = "{scene_id}_{performers}_{time}.jpg".format(
            scene_id=marker.scene_id,
            performers=marker.get_performers_as_string(),
            time=time)
        final_basename = path.join(self.dest_folder, TAG_IMAGES_FOLDER, tag)
        final_dest = path.join(final_basename, img_name)

        video_capture = cv2.VideoCapture(path.join(self.dest_folder, marker.get_full_path().removeprefix("/")))
        video_capture.set(cv2.CAP_PROP_POS_MSEC, time)
        success, image = video_capture.read()

        if (success):
            os.makedirs(final_basename, exist_ok=True)
            cv2.imwrite(final_dest, image)
            print("generated: ", final_dest)
        else:
            print("fail: ", final_dest)

    def _compute_new_filename(self, marker, video):
        return str(video.scene_id) + "_" + marker.to_rg_filename()

    def _create_dir_if_not_exists(self, final_dest_folder):
        if (not path.exists(final_dest_folder)):
            os.makedirs(final_dest_folder)
            print("folder created:", final_dest_folder)
        else:
            print("already exists:", final_dest_folder)

    def _cut_video(self, filename: str, start: int, end: int, new_name_without_extension="") -> None:
        extension = pathlib.Path(filename).suffix
        # Remove "absolute path"
        src_path = path.join(self.src_folder, filename.removeprefix("/"))
        dest_path = path.join(self.dest_folder,
                              new_name_without_extension + extension if new_name_without_extension != "" else filename)
        if path.exists(dest_path):
            return

        self.validate_path(src_path, dest_path)

        if self.debug:
            print("Cutting file", src_path, "into", dest_path, "from", start, "to", end)
        ffmpeg_extract_subclip(src_path, start, end, dest_path)

    def validate_path(self, src_path, dest_path):
        if path.exists(dest_path):
            raise Exception("ERROR:", dest_path, "already exist")
        if src_path == dest_path:
            raise Exception("ERROR: source and dest path cannot be the same")
