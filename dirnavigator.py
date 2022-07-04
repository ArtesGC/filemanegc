from os import listdir, path


class DirNav:
    def __init__(self, _dir: str):
        self.directory = _dir
        self.content = listdir(directory)

        self.files = []
        self.folders = []

        for item in content:
            if path.isdir(f'{self.directory}/{item}'):
                self.folders.append(item)
            elif path.isfile(f'{self.directory}/{item}'):
                self.files.append(item)

    def quant_files(self):
        return len(self.files)

    def quant_folders(self):
        return len(self.folders)

    def name_files(self):
        return self.files

    def name_folders(self):
        return self.folders
