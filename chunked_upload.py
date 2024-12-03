import dropbox
import os

# Dropbox access token
ACCESS_TOKEN = os.getenv('DROPBOX_ACCESS_TOKEN')

# File to be uploaded
file_path = 'mysql.tar'
dropbox_path = '/mysql.tar'

# Chunk size (in bytes)
CHUNK_SIZE = 4 * 1024 * 1024  # 4MB

def upload_large_file(file_path, dropbox_path):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    
    with open(file_path, 'rb') as f:
        file_size = os.path.getsize(file_path)
        
        if file_size <= CHUNK_SIZE:
            dbx.files_upload(f.read(), dropbox_path)
        else:
            upload_session_start_result = dbx.files_upload_session_start(f.read(CHUNK_SIZE))
            cursor = dropbox.files.UploadSessionCursor(session_id=upload_session_start_result.session_id, offset=f.tell())
            commit = dropbox.files.CommitInfo(path=dropbox_path)

            while f.tell() < file_size:
                if (file_size - f.tell()) <= CHUNK_SIZE:
                    dbx.files_upload_session_finish(f.read(CHUNK_SIZE), cursor, commit)
                else:
                    dbx.files_upload_session_append_v2(f.read(CHUNK_SIZE), cursor)
                    cursor.offset = f.tell()

if __name__ == "__main__":
    upload_large_file(file_path, dropbox_path)
