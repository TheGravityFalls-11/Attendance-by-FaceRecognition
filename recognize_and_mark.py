import cv2
from deepface import DeepFace
import pickle
import numpy as np
import pandas as pd
import datetime

# Load known encodings
with open("encodings.pkl", "rb") as f:
    known_encodings = pickle.load(f)

# Attendance file
attendance_file = "attendance.csv"

# Create CSV if it doesn't exist
try:
    df = pd.read_csv(attendance_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Name", "Time"])
    df.to_csv(attendance_file, index=False)

# Function to calculate Euclidean distance
def is_match(known_vec, candidate_vec, threshold=0.4):
    dist = np.linalg.norm(np.array(known_vec) - np.array(candidate_vec))
    return dist < threshold

# Function to mark attendance
def mark_attendance(name):
    df = pd.read_csv(attendance_file)
    if name not in df["Name"].values:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df = df.append({"Name": name, "Time": now}, ignore_index=True)
        df.to_csv(attendance_file, index=False)
        print(f"✅ Attendance marked for {name}")

# Start camera
cam = cv2.VideoCapture(0)
print("🎥 Camera started. Press 'q' to quit.")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    try:
        faces = DeepFace.extract_faces(frame, detector_backend='opencv', enforce_detection=False)
    except Exception as e:
        print(f"Face detection error: {e}")
        faces = []

    for face in faces:
        cropped_face = face["face"]
        x, y, w, h = (face["facial_area"]["x"], face["facial_area"]["y"],
                      face["facial_area"]["w"], face["facial_area"]["h"])

        try:
            # Generate embedding for detected face
            embedding = DeepFace.represent(cropped_face, model_name="Facenet")[0]["embedding"]

            name_found = "Unknown"
            for name, embeddings in known_encodings.items():
                if any(is_match(e, embedding) for e in embeddings):
                    name_found = name
                    mark_attendance(name)
                    break

            # Draw bounding box and name
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, name_found, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        except Exception as e:
            print(f"Embedding error: {e}")

    cv2.imshow("Face Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
