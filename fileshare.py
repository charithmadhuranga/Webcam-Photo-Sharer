from pyuploadcare import Uploadcare


class FileSharer:
    def __init__(self,filepath,public_key,secret_key):
        self.filepath = filepath
        self.public_key = public_key
        self.secret_key = secret_key

    def share(self):
        uploadcare = Uploadcare(public_key=self.public_key, secret_key=self.secret_key)
        filelink = uploadcare.file(self.filepath).store()
        return filelink
