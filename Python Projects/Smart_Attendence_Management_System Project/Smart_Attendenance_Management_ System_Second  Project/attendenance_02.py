import face_recognition
import cv2

#  replace these with your own data or more student details
KNOWN_FACES = {
    "Angad kumar": "angad.jpg",
    "Akshay": "Akshay.jpeg",
    "jacki shroff": "jacki shroff.jpg",
    "Akshay": "Akshay.jpeg",
    # Add more faces with their corresponding image paths
}

def load_known_faces():
    known_encodings = {}
    for name, image_path in KNOWN_FACES.items():
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        known_encodings[name] = encoding
    return known_encodings

def mark_attendance(name):
    with open("attendance.txt", "a") as file:
        file.write(f"{name}, present\n")

def recognize_faces(frame, face_locations, face_encodings, known_encodings, tolerance=0.6):
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(list(known_encodings.values()), face_encoding, tolerance=tolerance)
        name = "Unknown"

        if True in matches:
            matched_index = matches.index(True)
            name = list(known_encodings.keys())[matched_index]

        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

        if name != "Unknown":
            mark_attendance(name)

def main():
    video_capture = cv2.VideoCapture(0)
    known_encodings = load_known_faces()

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        recognize_faces(frame, face_locations, face_encodings, known_encodings)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
