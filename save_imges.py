import cv2, os

name = input("Enter person's name: ")
path = f"dataset/{name}"
os.makedirs(path, exist_ok=True)

cam = cv2.VideoCapture(0)
i = 0

while i < 30:
    ret, frame = cam.read()
    if not ret:
        break
    cv2.imshow("Capturing Face", frame)
    cv2.imwrite(f"{path}/img{i}.jpg", frame)
    i += 1
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
