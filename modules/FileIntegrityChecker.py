import hashlib
from modules.security.HashAlgo import Hash

class FileIntegrityChecker:
    def __init__(self):
        self.hash_dict = {}

    def calculate_file_hash(self, file_path):
        hash_object = Hash()
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                hash_object.update(chunk)
        return hash_object.hexdigest()

    def update_hashes(self, model, source, destination):
        source_path = model.filePath(source)
        destination_path = model.filePath(destination)

        source_hash = self.calculate_file_hash(source_path)
        destination_hash = self.calculate_file_hash(destination_path)

        self.hash_dict[source_path] = source_hash
        self.hash_dict[destination_path] = destination_hash

    def check_integrity(self, model, index):
        file_path = model.filePath(index)
        current_hash = self.calculate_file_hash(file_path)
        stored_hash = self.hash_dict.get(file_path)

        if stored_hash and current_hash != stored_hash:
            print(f"Integrity check failed for file: {file_path}")
        else:
            print(f"Integrity check passed for file: {file_path}")
