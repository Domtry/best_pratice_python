import os
from autoload import ModuleLoader

ModuleLoader.set_setting(
    base_path=os.getcwd(), 
    strict=False,
    singleton=True
)

loader_repo = ModuleLoader()
sql_memory = "in_memory"
Memory = loader_repo.load_class(f"repositories/{sql_memory}")


repo = Memory()
user = repo.find_user({"username":"domtry", "password": "123456"})

print(user)