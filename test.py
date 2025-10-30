import cv2
from ultralytics import YOLO

# Load your trained model
model = YOLO("C:\\Users\\kumar\\Desktop\\NASA Spaceapp\\NASA_fnf_model\\detect_best.pt")   # path to your trained weights

# Function for video detection
def detect_from_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLO inference
        results = model(frame)

        # Visualize results on frame
        annotated_frame = results[0].plot()

        # Display
        cv2.imshow("Trash Detection - Video", annotated_frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Function for webcam detection 
def detect_from_webcam():
    cap = cv2.VideoCapture(0)   # 0 = default webcam

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLO inference
        results = model(frame)

        # Visualize results
        annotated_frame = results[0].plot()

        # Show
        cv2.imshow("Trash Detection - Webcam", annotated_frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    mode = input("Enter 'v' for video or 'w' for webcam: ").strip().lower()
    if mode == 'v':
        detect_from_video("C:\\Users\\kumar\\Desktop\\NASA Spaceapp\\NASA_fnf_model\\Video2.mp4")
    elif mode == 'w':
        detect_from_webcam()
    else:
        print("Invalid option.")