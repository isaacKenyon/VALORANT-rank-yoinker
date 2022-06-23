import sys
from cx_Freeze import setup, Executable

build_exe_options = {"path": sys.path}

setup(
    name = "VALORANT rank yoinker",
    version = "1.262",
    description='vRY - Live Match Rank Viewer',
    executables = [Executable("main.py", icon="./assets/Logo.ico")],
    options={"build_exe": build_exe_options}
)