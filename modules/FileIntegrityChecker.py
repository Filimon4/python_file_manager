import hashlib
from modules.security.HashAlgo import Hash

class FileIntegrityChecker:
    def __init__(self):
        self.hash_dict = {}

    def addFile(self, file_path):

        source_hash = self.calculate_file_hash(file_path)
        self.hash_dict[file_path] = source_hash

    def calculate_file_hash(self, file_path):
        hash_object = Hash()
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                hash_object.update(chunk)
        return hash_object.hexdigest()

    def compare_two(self, source1, source2):
        source1_hash = self.calculate_file_hash(source1)
        source2_hash = self.calculate_file_hash(source2)

        if source1_hash == source2_hash:
            return True
        else:
            return False

    def compare_all(self):
        pass


    def compare_with(self, source, index):
        current_hash = self.calculate_file_hash(index)
        stored_hash = self.hash_dict.get(source)

        if stored_hash and current_hash == stored_hash:
            print(f"Integrity check passed for file: {index}")
            return True
        else:
            print(f"Integrity check failed for file: {index}")
            return False
        