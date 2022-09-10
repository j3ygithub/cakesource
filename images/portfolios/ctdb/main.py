import pathlib


base_dir = pathlib.Path(__file__).resolve().parent
for file in base_dir.iterdir():
    fullname = file.name
    if fullname.startswith("ctdb-"):
        name = fullname.split("ctdb-")[-1]
    file.rename(file.with_name(name))
