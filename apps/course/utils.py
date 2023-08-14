import cv2


def get_video_length(video_path):
    try:
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        total_seconds = frame_count / fps
        hours = int(total_seconds // 3600)
        total_seconds %= 3600
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        if hours == 0:
            return f"{minutes}:{seconds}"
        return f"{hours}:{minutes}:{seconds}"
    except Exception as e:
        print(f"Error: {e}")
        return None

