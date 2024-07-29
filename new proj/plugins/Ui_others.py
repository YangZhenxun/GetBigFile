import pickle
from pathlib import Path

plug_path = Path(__file__).resolve().parent/"plugins"
usr_path = plug_path.parent/"usr.pkl"

def true(usrname, passwd):
    with open(usr_path, "wb") as f:
        pickle.dump({"username": usrname, "password": passwd}, f)
