from deepface import DeepFace
def verify_if_there_are_faces(image_path):
    try:
        result = DeepFace.extract_faces(image_path)
        return True
    except Exception as e:
        return False

image_path = '../imagens_teste/obama2.png'

print(verify_if_there_are_faces(image_path))