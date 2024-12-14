from pyuploadcare import Uploadcare


class FileSharer:
    def __init__(self, filepath, public_key, secret_key):
        self.filepath = filepath
        self.public_key = public_key
        self.secret_key = secret_key

    def share(self):
        uploadcare = Uploadcare(public_key=self.public_key, secret_key=self.secret_key)
        with open(self.filepath, 'rb') as file_object:
            ucare_file = uploadcare.upload(file_object)
        filelink = ucare_file.cdn_url
        return filelink
