import os

def assure_path_exists(raw_path):
        dir = os.path.dirname(raw_path)
        if not os.path.exists(dir):
                os.makedirs(dir)
