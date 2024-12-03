import magic
import os
import platform

CONTENT_TYPE_ICO = "image/x-icon"
CONTENT_TYPE_JPG = "image/jpeg"
CONTENT_TYPE_PNG = "image/png"
CONTENT_TYPE_PDF = "application/pdf"

def get_content_type(file):
    system = platform.system()

    if system == "Windows":
        file_magic = magic.Magic(mime=True)
    else:
        file_magic = magic.Magic(mime=True)

    if hasattr(file, "temporary_file_path"):
        content_type = file_magic.from_file(file.temporary_file_path())
    else:
        content_type = file_magic.from_buffer(file.read())

    if hasattr(file, "seek") and callable(file.seek):
        file.seek(0)

    return content_type
