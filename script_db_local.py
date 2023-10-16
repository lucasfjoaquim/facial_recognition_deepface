from deepface import DeepFace

img_path = 'imagens_teste/obama2.png'

def verify_if_img_in_db(img):
    try:
        dfs = DeepFace.find(img_path=img, db_path="image_DB/")
        if dfs[0].empty:
            return "Pessoa não indentificada"
        else:
            identitidade = dfs[0]['identity'][0]
            identitidade = process_string_data(identitidade)
            return identitidade
    except Exception as e:
        print(f"Erro ao escanar foto: {e}")

def process_string_data(string_path):
    string_path = str(string_path)
    processed_string = string_path.split("//")[1].split(".")[0]
    processed_string = f"Pessoa na foto: {processed_string}"
    return processed_string


print(verify_if_img_in_db(img_path))
