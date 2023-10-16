from deepface import DeepFace

def verify_if_img_in_db_cloud(img):
    try:
        dfs = DeepFace.find(img_path=img, db_path="image_DB/")
        if dfs[0].empty:
            return None
        else:
            identitidade = dfs[0]['identity'][0]
            return identitidade
    except Exception as e:
        print(f"Erro ao escanar foto: {e}")
        return None