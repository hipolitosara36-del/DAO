import os
import pandas as pd
from dao.user_dao_base import UserDAOBase
from models.user import User

class UserDAOExcel(UserDAOBase):
    def __init__(self, filepath: str):
        self.filepath = filepath
        if not os.path.exists(filepath):
            # Crear archivo Excel con encabezados si no existe
            df = pd.DataFrame(columns=["id", "name", "email"])
            df.to_excel(filepath, index=False)

    def add_user(self, user: User):
        users = self.get_all_users()
        user_id = len(users) + 1
        new_user = {"id": user_id, "name": user.name, "email": user.email}
        df = pd.read_excel(self.filepath)
        df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
        df.to_excel(self.filepath, index=False)

    def get_all_users(self) -> list[User]:
        users = []
        df = pd.read_excel(self.filepath)
        for _, row in df.iterrows():
            users.append(User(int(row["id"]), row["name"], row["email"]))
        return users