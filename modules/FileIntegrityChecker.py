import hashlib
import os
from modules.security.HashAlgo import Hash

class FileIntegrityChecker:
    def __init__(self):
        self.hash_dict = {}

    def addFile(self, file_path):
        source_hash = self.calculate_file_hash(file_path)
        self.hash_dict[file_path] = source_hash

    def calculate_file_hash(self, file_path):
        hash_object = Hash()
        try:
            with open(file_path, 'rb') as file:
                for chunk in iter(lambda: file.read(4096), b''):
                    hash_object.update(chunk)
        except PermissionError:
            return 'denied'
        return hash_object.hexdigest()  

    def compare_two(self, source1, source2):
        source1_hash = self.calculate_file_hash(source1)
        source2_hash = self.calculate_file_hash(source2)

        if source1_hash == 'denied' or source2_hash == 'denied':
            return True

        if source1_hash == source2_hash:
            return True
        else:
            return False

    def compare_with(self, source, index):
        current_hash = self.calculate_file_hash(index)
        stored_hash = self.hash_dict.get(source)

        if stored_hash and current_hash == stored_hash:
            return True
        else:
            return False
        
class FolderIntegrityChecker(FileIntegrityChecker):

    def __init__(self):
        super().__init__()
        self.folder_dict = {}

    def addFolder(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            self.folder_dict[root] = {}
            for f in files:
                fPath = os.path.join(root, f)
                fHex = super().calculate_file_hash(fPath)
                self.folder_dict[root][fPath] = fHex

    def calculate_folder_hash(self, file_path):
        pass

    def compare_two(self, source1, source2):
        self.addFolder(source1)
        self.addFolder(source2)
        hashFolder1 = self.folder_dict[source1]
        hashFolder2 = self.folder_dict[source2]
        equal = True
        for i in hashFolder1.values():
            if not equal: break
            for j in hashFolder2.values():
                if i != j:
                    equal = False
                    break
        return equal
