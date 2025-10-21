import os
import shutil

def delete_pycache(root_dir: str = '.') -> None:
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '__pycache__' in dirnames:
            pycache_path = os.path.join(dirpath, '__pycache__')
            print(f'Deleting: {pycache_path}')
            shutil.rmtree(pycache_path, ignore_errors=True)

if __name__ == '__main__':
    delete_pycache('.')
