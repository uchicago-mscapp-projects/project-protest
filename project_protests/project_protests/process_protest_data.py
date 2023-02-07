import os
import pandas as pd
import glob

def load_data():
    folder_dir = "/home/monican/capp30122/30122-project-project-protest/project_protests/count_data"
    csv_files = glob.glob(os.path.join(folder_dir, "*.csv"))
    print("is this working")
    for f in csv_files:
        df = pd.read_csv(f)
        print('Location:', f)
        print('File Name:', f.split("\\")[-1])
    return None

load_data()