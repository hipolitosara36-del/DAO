import json
from dao.user_dao_mysql import UserDAOMySQL
from dao.user_dao_txt import UserDAOTxt
from dao.user_dao_xml import UserDAOXML
from dao.user_dao_sqlserver import UserDAOSQLServer  
from dao.user_dao_excel import UserDAOExcel

def get_dao_from_config(config_path="config.json"):
    with open(config_path, "r") as f:
        config = json.load(f)

    dao_type = config["dao_type"].lower()

    if dao_type == "mysql":
        mysql_conf = config["mysql"]
        return UserDAOMySQL(
            host=mysql_conf["host"],
            user=mysql_conf["user"],
            password=mysql_conf["password"],
            database=mysql_conf["database"]
        )

    elif dao_type == "txt":
        return UserDAOTxt(config["txt"]["filepath"])

    elif dao_type == "xml":
        return UserDAOXML(config["xml"]["filepath"])
    
    elif dao_type == "excel":
        return UserDAOExcel(config["excel"]["filepath"])
    
    elif dao_type == "sqlserver": 
        mssql_conf = config["sqlserver"]
        return UserDAOSQLServer(
            host=mssql_conf["host"],
            user=mssql_conf["user"],
            password=mssql_conf["password"],
            database=mssql_conf["database"]
        )
    else:
        raise ValueError(f"Tipo de DAO desconocido: {dao_type}")

