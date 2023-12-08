import os


class FileManager:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def check_and_create_directory(self):
        if not os.path.exists(self.directory_path):
            try:
                os.makedirs(self.directory_path)
                print(f"Directory '{self.directory_path}' created successfully.")
            except OSError as e:
                print(f"Error creating directory '{self.directory_path}': {e}")
        else:
            print(f"Directory '{self.directory_path}' already exists.")

