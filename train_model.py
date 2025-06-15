from deepface import DeepFace
import os
import pickle

dataset_path = "dataset"
encodings = {}

print("Encoding faces from dataset...")

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)
    embeddings = []
    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)
        try:
            # Get embedding vector for the image using Facenet model
            embedding = DeepFace.represent(img_path, model_name="Facenet")[0]["embedding"]
            embeddings.append(embedding)
            print(f"Encoded {img_name} of {person}")
        except Exception as e:
            print(f"Could not encode {img_path}: {e}")
    encodings[person] = embeddings

with open("encodings.pkl", "wb") as f:
    pickle.dump(encodings, f)

print("Encoding complete and saved to encodings.pkl")
