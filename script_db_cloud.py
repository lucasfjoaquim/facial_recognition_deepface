import psycopg2
import os
from dotenv import load_dotenv
from app.facial_recognition import verify_if_img_in_db_cloud
from app.remove_path import process_string_data

load_dotenv()

class BancoDeDados:

    @staticmethod
    def conexao(self):
        try:
            connection = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
        except Exception as e:
            print(e)
        return connection

    def execute(self,SQL):
        connection = self.conexao(self)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SQL)

    def querry(self,SQL):
        connection = self.conexao(self)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SQL)
                results = cursor.fetchall()
        return results

    def get_workers(self, worker_img=None):
        if worker_img is None:
            SQL = "SELECT * FROM workers"
        else:
            SQL = f"SELECT * FROM workers WHERE image = '{worker_img}'"
        response = self.querry(SQL)
        return response

    def verify_image(self,img):

        result = verify_if_img_in_db_cloud(img)
        if result is None:
            return False
        else:
            result = process_string_data(result)
            worker = self.get_workers(result)
            self.print_workers(worker)
            return True

    def print_workers(self,worker_query):
        for worker in worker_query:
            print(f"Id : {worker[0]}\n"
                  f"Name : {worker[1]}\n"
                  f"Image : {worker[2]}\n"
                  f"Record Creation : {worker[3]}")


DB = BancoDeDados()
print(DB.verify_image('imagens_teste/eu.jpg'))