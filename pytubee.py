# This is Youtube Video Downloader Python Program
from pytube import Playlist
from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os
import shutil


# Gives download progress
def on_progress(stream, chunk, bytes_remaining):
    progress = f"{round(100 - (bytes_remaining/stream.filesize * 100), 2)}%"
    print("")
    print(f"\033[1m Progress: {progress} \033[0m")


# Do this on download completion
def on_complete(stream, file_path):
    print("")
    print("######################################################")
    print("\033[1m Download Completed \033[0m")
    print(f"\033[1m Download path: {file_path} \033[0m")
    print("######################################################")


# download directory
def download_directory():
    user_download_directory = os.path.join(
        os.path.expanduser("~"), "Downloads")
    return user_download_directory


# download file function
def download_file(title, video):
    print("")
    print("######################################################")
    print(f"\033[1m Video title: {title} \033[0m")
    file_size = round((video.filesize / 1000000), 2)
    print(f"\033[1m File Size: {file_size} MB\033[1m")
    print("")
    print("\033[1m Please wait... \033[0m")
    print("")
    output_path = download_directory()
    file_path = video.download(f"{output_path}\\temp")
    print("")
    return file_path


# combine audio and video function
def combine_audio_and_video(video_path, audio_path):
    # Load video clip
    video_clip = VideoFileClip(video_path)
    # Load audio clip
    audio_clip = AudioFileClip(audio_path)
    # Set video clip's audio to the loaded audio clip
    video_clip = video_clip.set_audio(audio_clip)
    # Write the combined video with audio to a new file
    output_path = download_directory()
    file_name = os.path.basename(audio_path)
    # print(f"file_name: {file_name}")
    file_name_without_extension = os.path.splitext(file_name)[0]
    # print(f"file_name_without_extension: {file_name_without_extension}")
    video_clip.write_videofile(
        f"{output_path}\\{file_name}", codec="libx264", audio_codec="aac"
    )


# checking audio and video
def checking_audio_and_video(audio, video, title, is_playlist):
    if not audio:
        print("")
        print("################################################")
        print("\033[1m Audio not found \033[0m")
        print("################################################")
        print("")
        if not is_playlist:
            on_init()
    elif not video:
        print("")
        print("################################################")
        print("\033[1m Video not found \033[0m")
        print("################################################")
        print("")
        if not is_playlist:
            on_init()
    elif not audio and video:
        print("")
        print("################################################")
        print("\033[1m Audio and Video not found \033[0m")
        print("################################################")
        print("")
        if not is_playlist:
            on_init()
    else:
        print("")
        print(f"audio_streams: {audio}")
        print(f"video_stream: {video}")
        video_path = download_file(title, video[0])
        audio_path = download_file(title, audio)
        # print(f"audio_path : {audio_path}")
        # print(f"video_path : {video_path}")
        combine_audio_and_video(video_path, audio_path)
        # delete temp directory
        file_path = download_directory()
        shutil.rmtree(f"{file_path}\\temp", ignore_errors=True)


# download video main function
def download_video():
    # get playlist url from user
    print("")
    video_url = input(
        "\033[1m Please enter a Video URL (Ex. https://youtu.be/bON-KPi) : \n ## \033[0m")
    print("")
    print("\033[1m Fetching data !! Please wait... \033[0m")
    print("")

    try:
        yt = YouTube(url=video_url, on_progress_callback=on_progress,
                     on_complete_callback=on_complete)
        # print all available stream
        streams = yt.streams
        for stream in streams:
            print(stream)

        print("")
        print("######################################################")
        print("\033[1m ## Select a Audio or Video ## \033[0m")
        print("")
        print("\033[1m 1. Music MP3 \033[0m")
        print("\033[1m 2. Video 240P \033[0m")
        print("\033[1m 3. Video 360P \033[0m")
        print("\033[1m 4. Video 480P \033[0m")
        print("\033[1m 5. Video 720P \033[0m")
        print("\033[1m 6. Video 1080P \033[0m")
        print("\033[1m 7. Video 1440P \033[0m")
        print("\033[1m 8. Video 2160P \033[0m")
        print("\033[1m 9. Exit \033[0m")
        print("")
        print("######################################################")

        # getting choice input from user
        while True:
            try:
                choice = int(
                    input("\033[1m Enter your choice (Ex. 1,2,3,4,...) : \033[0m"))
                break
            except:
                print("######################################################")
                print("\033[1m That's not a valid option! \033[0m")
                print("######################################################")

        # filtering data as per user choice
        if choice == 1:
            audio = yt.streams.get_audio_only()
            print(audio)
            if audio:
                print("################################################")
                print(f"\033[1m Video title: {yt.title} \033[0m")
                file_size = round((audio.filesize / 1000000), 2)
                print(f"\033[1m File Size: {file_size} MB \033[0m \n")
                print("\033[1m Please wait... \033[0m")
                output_path = download_directory()
                audio.download(output_path)
                print("")
            else:
                print("################################################")
                print("\033[1m Audio not found \033[0m")
                print("################################################")
                on_init()
        elif choice == 2:
            video = yt.streams.filter(
                type="video", res="240p", mime_type="video/webm")
            audio = yt.streams.get_audio_only()
            checking_audio_and_video(audio, video, yt.title, False)
        elif choice == 3:
            # download video
            video = yt.streams.filter(
                type="video", res="360p", mime_type="video/webm")
            audio = yt.streams.get_audio_only()
            checking_audio_and_video(audio, video, yt.title, False)
        elif choice == 4:
            # download video
            video = yt.streams.filter(
                type="video", res="480p", mime_type="video/webm")
            audio = yt.streams.get_audio_only()
            checking_audio_and_video(audio, video, yt.title, False)
        elif choice == 5:
            # download video
            video = yt.streams.filter(
                type="video", res="720p", mime_type="video/webm")
            audio = yt.streams.get_audio_only()
            checking_audio_and_video(audio, video, yt.title, False)
        elif choice == 6:
            # download video
            video = yt.streams.filter(
                type="video", res="1080p", mime_type="video/webm")
            audio = yt.streams.get_audio_only()
            checking_audio_and_video(audio, video, yt.title, False)
        elif choice == 7:
            # download video
            video = yt.streams.filter(
                type="video", res="1440p", mime_type="video/webm")
            audio = yt.streams.get_audio_only()
            checking_audio_and_video(audio, video, yt.title, False)
        elif choice == 8:
            # download video
            video = yt.streams.filter(
                type="video", res="2160p", mime_type="video/webm")
            audio = yt.streams.get_audio_only()
            checking_audio_and_video(audio, video, yt.title, False)
        elif choice == 9:
            print("################################################")
            print("\033[1m Program closed !! \033[0m")
            print("################################################")
        else:
            print("################################################")
            print("\033[1m Invalid input !! \033[0m")
            print("################################################")

    except Exception as e:
        print("################################################")
        print("\033[1m Invalid input !! \033[0m")
        print("################################################")
        on_init()


# download playlist function
def download_playlist():
    # get playlist url from user
    print("")
    playlist_url = input(
        "\033[1m Please enter a Playlist URL (Ex. https://youtu.be/bON-KPi) : \n ## \033[0m")
    print("")
    print("\033[1m Fetching data !! Please wait... \033[0m")
    print("")

    # Create Playlist obj
    playlist = Playlist(playlist_url)

    # Num of videos in playlist
    video_count = playlist.length

    print(f"\033[1m Number of videos in the playlist: {video_count} \033[0m")

    try:
        print("")
        print("######################################################")
        print("\033[1m ## Select a Audio or Video ## \033[0m")
        print("")
        print("\033[1m 1. Music MP3 \033[0m")
        print("\033[1m 2. Video 240P \033[0m")
        print("\033[1m 3. Video 360P \033[0m")
        print("\033[1m 4. Video 480P \033[0m")
        print("\033[1m 5. Video 720P \033[0m")
        print("\033[1m 6. Video 1080P \033[0m")
        print("\033[1m 7. Video 1440P \033[0m")
        print("\033[1m 8. Video 2160P \033[0m")
        print("\033[1m 9. Exit \033[0m")
        print("")
        print("######################################################")

        # getting choice input from user
        while True:
            try:
                choice = int(
                    input("\033[1m Enter your choice (Ex. 1,2,3,4,...) : \033[0m"))
                break
            except:
                print("######################################################")
                print("\033[1m That's not a valid option! \033[0m")
                print("######################################################")

        # filtering data as per user choice
        if choice == 1:
            # for every video in the playlist
            for vids in playlist.videos:
                # getting playlist first video url
                vid_url = vids.watch_url
                print("")
                print("\033[1m Fetching data !! Please wait... \033[0m")
                print("")
                # getting stream data
                yt = YouTube(url=vid_url, on_progress_callback=on_progress,
                             on_complete_callback=on_complete)
                audio = yt.streams.get_audio_only()
                print(audio)
                if audio:
                    print("################################################")
                    print(f"\033[1m Video title: {yt.title} \033[0m")
                    file_size = round((audio.filesize / 1000000), 2)
                    print(f"\033[1m File Size: {file_size} MB \033[0m \n")
                    print("\033[1m Please wait... \033[0m")
                    output_path = download_directory()
                    audio.download(output_path)
                    print("")
                else:
                    print("################################################")
                    print("\033[1m Audio not found \033[0m")
                    print("################################################")
        elif choice == 2:
            # for every video in the playlist
            for vids in playlist.videos:
                # getting playlist first video url
                vid_url = vids.watch_url
                print("")
                print("\033[1m Fetching data !! Please wait... \033[0m")
                print("")
                # getting stream data
                yt = YouTube(url=vid_url, on_progress_callback=on_progress,
                             on_complete_callback=on_complete)
                video = yt.streams.filter(
                    type="video", res="240p", mime_type="video/webm")
                audio = yt.streams.get_audio_only()
                checking_audio_and_video(audio, video, yt.title, True)
        elif choice == 3:
            # for every video in the playlist
            for vids in playlist.videos:
                # getting playlist first video url
                vid_url = vids.watch_url
                print("")
                print("\033[1m Fetching data !! Please wait... \033[0m")
                print("")
                # getting stream data
                yt = YouTube(url=vid_url, on_progress_callback=on_progress,
                             on_complete_callback=on_complete)
                # download video
                video = yt.streams.filter(
                    type="video", res="360p", mime_type="video/webm")
                audio = yt.streams.get_audio_only()
                checking_audio_and_video(audio, video, yt.title, True)
        elif choice == 4:
            # for every video in the playlist
            for vids in playlist.videos:
                # getting playlist first video url
                vid_url = vids.watch_url
                print("")
                print("\033[1m Fetching data !! Please wait... \033[0m")
                print("")
                # getting stream data
                yt = YouTube(url=vid_url, on_progress_callback=on_progress,
                             on_complete_callback=on_complete)
                # download video
                video = yt.streams.filter(
                    type="video", res="480p", mime_type="video/webm")
                audio = yt.streams.get_audio_only()
                checking_audio_and_video(audio, video, yt.title, True)
        elif choice == 5:
            # for every video in the playlist
            for vids in playlist.videos:
                # getting playlist first video url
                vid_url = vids.watch_url
                print("")
                print("\033[1m Fetching data !! Please wait... \033[0m")
                print("")
                # getting stream data
                yt = YouTube(url=vid_url, on_progress_callback=on_progress,
                             on_complete_callback=on_complete)
                # download video
                video = yt.streams.filter(
                    type="video", res="720p", mime_type="video/webm")
                audio = yt.streams.get_audio_only()
                checking_audio_and_video(audio, video, yt.title, True)
        elif choice == 6:
            # for every video in the playlist
            for vids in playlist.videos:
                # getting playlist first video url
                vid_url = vids.watch_url
                print("")
                print("\033[1m Fetching data !! Please wait... \033[0m")
                print("")
                # getting stream data
                yt = YouTube(url=vid_url, on_progress_callback=on_progress,
                             on_complete_callback=on_complete)
                # download video
                video = yt.streams.filter(
                    type="video", res="1080p", mime_type="video/webm")
                audio = yt.streams.get_audio_only()
                checking_audio_and_video(audio, video, yt.title, True)
        elif choice == 7:
            # for every video in the playlist
            for vids in playlist.videos:
                # getting playlist first video url
                vid_url = vids.watch_url
                print("")
                print("\033[1m Fetching data !! Please wait... \033[0m")
                print("")
                # getting stream data
                yt = YouTube(url=vid_url, on_progress_callback=on_progress,
                             on_complete_callback=on_complete)
                # download video
                video = yt.streams.filter(
                    type="video", res="1440p", mime_type="video/webm")
                audio = yt.streams.get_audio_only()
                checking_audio_and_video(audio, video, yt.title, True)
        elif choice == 8:
            # for every video in the playlist
            for vids in playlist.videos:
                # getting playlist first video url
                vid_url = vids.watch_url
                print("")
                print("\033[1m Fetching data !! Please wait... \033[0m")
                print("")
                # getting stream data
                yt = YouTube(url=vid_url, on_progress_callback=on_progress,
                             on_complete_callback=on_complete)
                # download video
                video = yt.streams.filter(
                    type="video", res="2160p", mime_type="video/webm")
                audio = yt.streams.get_audio_only()
                checking_audio_and_video(audio, video, yt.title, True)
        elif choice == 9:
            print("################################################")
            print("\033[1m Program closed !! \033[0m")
            print("################################################")
        else:
            print("################################################")
            print("\033[1m Invalid input !! \033[0m")
            print("################################################")
            on_init()

    except Exception as e:
        print("################################################")
        print("\033[1m Invalid input !! \033[0m")
        print("################################################")
        on_init()


def on_init():
    print()
    print("################################################")
    print("\033[1m Welcome to Youtube Video Downloader \033[0m")
    print("################################################")
    print("")
    print("################################################")
    print("\033[1m What do you want to download? \033[0m")
    print("################################################")
    print("\033[1m 1. Video \033[0m")
    print("\033[1m 2. Playlist \033[0m")
    print("\033[1m 3. Exit \033[0m")
    print("################################################")
    print("")
    chos = int(input("\033[1m Enter your choice (1,2 or 3) : \033[0m"))
    if chos == 1:
        download_video()
    elif chos == 2:
        download_playlist()
    else:
        print("################################################")
        print("\033[1m Program closed !! \033[0m")
        print("################################################")


# calling first function
on_init()
