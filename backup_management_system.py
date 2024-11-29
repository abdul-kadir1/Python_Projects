import os
import time
import shutil
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate_google_drive():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('drive', 'v3', credentials=creds)

def backup_files(source_dir, backup_dir):
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist!")
        return
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    for filename in os.listdir(source_dir):
        src_file = os.path.join(source_dir, filename)
        dst_file = os.path.join(backup_dir, filename)
        if os.path.isdir(src_file):
            shutil.copytree(src_file, dst_file)
        else:
            shutil.copy2(src_file, dst_file)
    print(f"Backup complete from '{source_dir}' to '{backup_dir}'.")

def upload_to_drive(service, folder_id, file_path):
    file_metadata = {'name': os.path.basename(file_path), 'parents': [folder_id]}
    media = MediaFileUpload(file_path, mimetype='application/octet-stream')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File '{file_path}' uploaded to Google Drive with ID: {file['id']}")

def automate_backup(source_dir, backup_dir, cloud_folder_id, interval_minutes=30):
    service = authenticate_google_drive()
    while True:
        backup_files(source_dir, backup_dir)
        for filename in os.listdir(backup_dir):
            file_path = os.path.join(backup_dir, filename)
            upload_to_drive(service, cloud_folder_id, file_path)
        print(f"Next backup will run in {interval_minutes} minutes...")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    source_directory = 'D:/Users/Lenovo/Documents'
    backup_directory = 'C:/Users/ProgramFiles/Documents'
    cloud_folder_id = '1ugCEi1zKQHsuqNnvtbIlNuRefC14E0IK'
    automate_backup(source_directory, backup_directory, cloud_folder_id, interval_minutes=30)
