import shutil
import datetime
import os

def backeup_files(source,destination):
    today = datetime.date.today()
    backeup_file_name = os.path.join(destination,f"backeup_{today}")
    shutil.make_archive(backeup_file_name,'gztar',source)

source = "/Users/vinod/OneDrive/Desktop/python-devops"
destination = "/Users/vinod/OneDrive/Desktop/python-devops/backups"
backeup_files(source,destination)