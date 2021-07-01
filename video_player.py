"""A video player class."""

from video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playing = None
        self.is_paused = False
        self.playlist = {}
        self.flagged = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        video_list = self._video_library.get_all_videos()
        for videos in video_list:
            tags = ""
            tags = tags + "["
            for name in videos.tags:
                if name == videos.tags[0]:
                    tags = tags + name
                else:
                    tags = tags + f" {name}"
            tags = tags + "]"

            print(f"{videos.title} ({videos.video_id}) {tags}")

    def play_video(self, video_id):
        if self._video_library.get_video(video_id) is None:
            print("Cannot play video: Video does not exist")
        else:
            if self.playing is not None:
                print(f"Stopping video: {self.playing.title}")
            self.playing = self._video_library.get_video(video_id)
            print(f"Playing video: {self.playing.title}")
            self.is_paused = False

    def stop_video(self):
        """Stops the current video."""
        if self.playing is None:
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self.playing.title}")
            self.playing = None
            self.is_paused = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        if self.playing is None:
            pass
        else:
            print(f"Stopping video: {self.playing.title}")

        self.playing = self._video_library.get_all_videos()[random.randint(0, len(self._video_library.get_all_videos())- 1)]
        print(f"Playing video: {self.playing.title}")

    def pause_video(self):
        """Pauses the current video."""
        if self.playing is None:
            print("Cannot pause video: No video is currently playing")
        elif self.is_paused:
            print(f"Video already paused: {self.playing.title}")
        else:
            print(f"Pausing video: {self.playing.title}")
            self.is_paused = True

    def continue_video(self):
        """Resumes playing the current video."""
        if self.playing is None:
            print("Cannot continue video: No video is currently playing")
        elif not self.is_paused:
            print("Cannot continue video: Video is not paused")
        elif self.is_paused:
            print(f"Continuing video: {self.playing.title}")
            self.is_paused = False

    def show_playing(self):
        status = ""
        if self.playing is None:
            print("No video is currently playing")
        else:
            if self.is_paused:
                status = "- PAUSED"
            tags = "["
            for name in self.playing.tags:
                if name == self.playing.tags[0]:
                    tags = tags + name
                else:
                    tags = tags + f" {name}"
            tags = tags + "]"
            print(f"Currently playing: {self.playing.title} ({self.playing.video_id}) {tags} {status}")

    def create_playlist(self, playlist_name):
        for keys in list(self.playlist.keys()):
            if keys.lower() == playlist_name.lower():
                print("Cannot create playlist: A playlist with the same name already exists")
                return None
        self.playlist[playlist_name] = []
        print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        for keys in list(self.playlist.keys()):
            if keys.lower() == playlist_name.lower():
                if self._video_library.get_video(video_id) is not None:
                    video_data = self._video_library.get_video(video_id)
                    if video_data in self.playlist[keys]:
                        print("Cannot add video to my_cool_playlist: Video already added")
                    else:
                        self.playlist[keys].append(video_data)
                        print(f"Added video to {playlist_name}: {video_data.title}")
                else:
                    print(f"Cannot add video to {playlist_name}: Video does not exist")
                return None

        print(f"Cannot add video to {playlist_name}: Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        if self.playlist == {}:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for key_names in list(self.playlist.keys()):
                print(key_names)

    def show_playlist(self, playlist_name):
        if self.playlist == "{}":
            print("No playlists exist yet")
            return None
        for keys in list(self.playlist.keys()):
            if keys.lower() == playlist_name.lower():
                print(f"Showing playlist: {playlist_name}")
                if self.playlist[keys] == []:
                    print("No videos here yet")
                else:
                    for videos in self.playlist[keys]:
                        tags = "["
                        for name in videos.tags:
                            if name == videos.tags[0]:
                                tags = tags + name
                            else:
                                tags = tags + f" {name}"
                        tags = tags + "]"
                        print(f"{videos.title} ({videos.video_id}) {tags}")
                return None
        print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        for keys in list(self.playlist.keys()):
            if keys.lower() == playlist_name.lower():
                if self._video_library.get_video(video_id) is None:
                    print(f"Cannot remove video from {playlist_name}: Video does not exist")
                    return None
                else:
                    for video in self.playlist[keys]:
                        if video_id == video.video_id:
                            self.playlist[keys].remove(video)
                            print(f"Removed video from {playlist_name}: {video.video_id}")
                            return None
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
                    return None
        print(f"Cannot remove video from {playlist_name}: Playlist does not exist")

    def clear_playlist(self, playlist_name):
        for keys in list(self.playlist.keys()):
            if keys.lower() == playlist_name.lower():
                self.playlist[keys] = []
                print(f"Successfully removed all videos from {playlist_name}")
                return None
        print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        for keys in list(self.playlist.keys()):
            if keys.lower() == playlist_name.lower():
                del self.playlist[keys]
                print(f"Deleted playlist: {playlist_name}")
                return None
        print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")

    def search_videos(self, search_term):
        results = []
        index = 0
        for videos in self._video_library.get_all_videos():
            title = videos.title.lower()
            result_code = title.find(search_term.lower())
            if result_code == -1:
                pass
            else:
                results.append(videos)
        if results == []:
            print(f"No search results for {search_term}")
        else:
            print(f"Here are the results for {search_term}:")
            for video in results:
                index = index + 1
                tags = ""
                tags = tags + "["
                for name in video.tags:
                    if name == video.tags[0]:
                        tags = tags + name
                    else:
                        tags = tags + f" {name}"
                tags = tags + "]"
                print(f"{index}) {video.title} ({video.video_id}) {tags}")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            answer = input()
            for numbers in range(index):
                if answer == str(numbers+1):
                    self.play_video(results[int(answer) - 1].video_id)

    def search_videos_tag(self, video_tag):
        results = []
        index = 0
        for videos in self._video_library.get_all_videos():
            for tags_video in videos.tags:
                title_tag = tags_video.lower()
                result_code = title_tag.find(video_tag.lower())
                if result_code == -1:
                    pass
                else:
                    results.append(videos)
        if results == []:
            print(f"No search results for {video_tag}")
        else:
            print(f"Here are the results for {video_tag}:")
            for video in results:
                index = index + 1
                tags = ""
                tags = tags + "["
                for name in video.tags:
                    if name == video.tags[0]:
                        tags = tags + name
                    else:
                        tags = tags + f" {name}"
                tags = tags + "]"
                print(f"{index}) {video.title} ({video.video_id}) {tags}")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            answer = input()
            for numbers in range(index):
                if answer == str(numbers+1):
                    self.play_video(results[int(answer)-1].video_id)

    def flag_video(self, video_id, flag_reason=""):
        pass
    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
