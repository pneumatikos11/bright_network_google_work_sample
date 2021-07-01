"""A video player class."""
from random import choice
from .video_library import VideoLibrary



class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.is_playing = False
        self.playing_now = ''
        self.is_paused = False
        self.playlist = {}
        self.playlist_list = []


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        temp_list = []
        for vid in videos:
            tags = "["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"
            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"

            temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]
        sorted_list = sorted(temp_list)
        for x in sorted_list:
            print(x)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        videos = self._video_library.get_all_videos()
        video_id_list = []
        for vid in videos:
            video_id_list.append(vid.video_id)
            if vid.video_id == video_id:
                if self.is_playing is False:
                    print(f"Playing video: {vid.title}")
                    self.playing_now = vid.title
                    self.is_playing = True
                    self.is_paused = False
                elif self.is_playing is True:
                    print(f"Stopping video: {self.playing_now}")
                    print(f"Playing video: {vid.title}")
                    self.playing_now = vid.title
                    self.is_paused = False
        if video_id not in video_id_list:
            print("Cannot play video: Video does not exist")
    def stop_video(self):
        """Stops the current video."""
        if self.is_playing:
            print(f"Stopping video: {self.playing_now}")
            self.is_playing = False
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        currently_playing = choice(self._video_library.get_all_videos())
        if self.is_playing is False:
            print(f"Playing video: {currently_playing.title}")
            self.playing_now = currently_playing.title
            self.is_playing = True
        elif self.is_playing is True:
            print(f"Stopping video: {self.playing_now}")
            print(f"Playing video: {currently_playing.title}")
            self.playing_now = currently_playing.title

    def pause_video(self):
        """Pauses the current video."""

        if self.is_playing and self.is_paused is False:
            print(f"Pausing video: {self.playing_now}")
            self.is_paused = True
        elif self.is_paused:
            print(f"Video already paused: {self.playing_now}")
        elif self.is_playing is False:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if self.is_paused:
            print(f"Continuing video: {self.playing_now}")
            self.is_paused = False
        elif self.is_playing and self.is_paused is False:
            print("Cannot continue video: Video is not paused")
        elif self.is_playing is False:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        temp_list = []
        if self.is_playing is False:
            print("No video is currently playing")
        else:
            videos = self._video_library.get_all_videos()
            for vid in videos:
                if vid.title == self.playing_now:
                    tags = "["
                    for tag in vid.tags:
                        tags = tags + tag + " "
                    tags = tags + "]"
                    if tags != "[]":
                        tags = tags[0:len(tags) - 2] + "]"

                    temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]
                    if self.is_paused is True:
                        print("Currently playing: " + temp_list[0] + " - PAUSED")
                    if self.is_paused is False:
                        print("Currently playing: " + temp_list[0])

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.upper() in self.playlist.keys():
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playlist[playlist_name.upper()] = []
            self.playlist_list.append(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        videos = self._video_library.get_all_videos()
        video_id_list = []
        for vid in videos:
            video_id_list.append(vid.video_id)
            if vid.video_id == video_id:
                if playlist_name.upper() in self.playlist.keys():
                    if vid.title not in self.playlist[playlist_name.upper()]:
                        self.playlist[playlist_name.upper()].append(vid.title)
                        print(f"Added video to {playlist_name}: {vid.title}")
                    else:
                        print(f"Cannot add video to {playlist_name}: Video already added")
        if playlist_name.upper() not in self.playlist.keys() and video_id not in video_id_list:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        if playlist_name.upper() not in self.playlist.keys() and video_id in video_id_list:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        if playlist_name.upper() in self.playlist.keys() and video_id not in video_id_list:
            print(f"Cannot add video to {playlist_name}: Video does not exist")


    def show_all_playlists(self):
        """Display all playlists."""
        if self.playlist == {}:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for x in sorted(self.playlist_list):
                print(f"{x}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        temp_list = []
        if playlist_name.upper() not in self.playlist.keys():
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
        else:
            print(f"Showing playlist: {playlist_name}")
            if not self.playlist[playlist_name.upper()]:
                print("\tNo videos here yet")
            else:
                videos = self._video_library.get_all_videos()
                for i in self.playlist[playlist_name.upper()]:
                    for vid in videos:
                        if vid.title == i:
                            tags = "["
                            for tag in vid.tags:
                                tags = tags + tag + " "
                            tags = tags + "]"
                            if tags != "[]":
                                tags = tags[0:len(tags) - 2] + "]"

                            temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]
                for x in temp_list:
                    print(f"\t{x}")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        videos = self._video_library.get_all_videos()
        video_id_list = []
        for vid in videos:
            video_id_list.append(vid.video_id)
            if video_id == vid.video_id:
                video = vid
                if playlist_name.upper() in self.playlist.keys() and video.title in self.playlist[playlist_name.upper()]:
                    self.playlist[playlist_name.upper()].remove(video.title)
                    print(f"Removed video from {playlist_name}: {video.title}")
                if playlist_name.upper() in self.playlist.keys() and video.title not in self.playlist[playlist_name.upper()]:
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
        if playlist_name.upper() in self.playlist.keys() and video_id not in video_id_list:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
        if playlist_name.upper() not in self.playlist.keys() and video_id not in video_id_list:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        if playlist_name.upper() not in self.playlist.keys() and video_id in video_id_list:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.upper() in self.playlist.keys():
            self.playlist[playlist_name.upper()].clear()
            print(f"Successfully removed all videos from {playlist_name}")
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.upper() in self.playlist.keys():
            del self.playlist[playlist_name.upper()]
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

    def refresh_variables(self):

        is_playing = False
        playing_now = ''
        is_paused = False
