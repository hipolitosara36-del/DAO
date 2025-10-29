# main.py

from models.user import User
from dao.factory import get_dao_from_config

def main():
    # El dao_type en config.json determinará si es SQLServer, MySQL, etc.
    dao = get_dao_from_config("config.json")
    
    # Llama a los métodos que el DAO de SQL Server ya implementó
    dao.add_user(User(None, "Sarahi H", "saracruz@example.com"))
    dao.add_user(User(None, "Armando M", "armando99@example.com"))
    dao.add_user(User(None, "Noemi S", "noemi23@example.com"))
    dao.add_user(User(None, "Evelyn A", "aide55@example.com"))
    

    print("Usuarios almacenados:")
    for u in dao.get_all_users():
        print(u) # Asumo que tu clase User tiene un buen método __str__ o __repr__

if __name__ == "__main__":
    main()