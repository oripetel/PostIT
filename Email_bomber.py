from instagrapi import Client

# Log in to Instagram
client = Client()
client.login("idaanlevi", "Ninja555@@@")

# Path to the video you want to upload
video_path = r"C:\Users\kork\Desktop\Email-Bomber-master\videotest.mp4"

# Upload video to Reels
client.clip_upload(
    video_path,
    caption="Check out this reel!",
    thumbnail="path_to_thumbnail_image.jpg"  # Optional thumbnail image
)
