from azure.storage.blob import BlobServiceClient

import os
import glob
connect_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]

container_name = "blob-container-01"

def upload_file(source, dest):
    print(f'Uploading {source} to {dest}')
    with open(source, 'rb') as data:
      container_client.upload_blob(name=dest, data=data)


def upload_dir(source, dest):
    '''
    Upload the whole directory into the storage account
    '''
    prefix = '' if dest == '' else dest + '/'
    prefix += os.path.basename(source) + '/'

    for root, dirs, files in os.walk(source):
        for name in files:
            dir_part = os.path.relpath(root, source)
            dir_part = '' if dir_part == '.' else dir_part + '/'
            file_path = os.path.join(root, name)
            blob_path = prefix + dir_part + name
            upload_file(file_path, blob_path)

def download(source, dest):
    '''
    Download the directory to a path on the local filesystem
    '''
    print("\nListing blobs...")
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)

    download_file_paths = []
    download_files = []
    upload_file_paths = []
    for root, dirs, files in os.walk(source):
        for name in files:
            download_file_path = os.path.join(source, str.replace(name ,'.txt', 'DOWNLOAD.txt'))
            download_file_paths.append(download_file_path)
            upload_file_paths.append(os.path.join(root, name))
            print("\nDownloading blob to \n\t" + download_file_path)
            with open(file=download_file_path, mode="wb") as download_file:
                download_file.write(container_client.download_blob(blob.name).readall())
    return download_file_paths, download_files, upload_file_paths

def clean_up(source, paths, down_files, upload_files):
    for path in paths:
        print(f'Cleaning up {path}')
        os.remove(path)
        
    for file in upload_files:
            print(f'Cleaning up {file}')
            os.remove(file)

    for file in down_files:
            print(f'Cleaning up {file}')
            os.remove(file)
            #os.rmdir(source)

    print("Deleting blob container...")
    container_client.delete_container()
    print("Deleting the local source and downloaded files...")
    print("Done")   

try:
    dest = '' 
    source='data'
    service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = service_client.get_container_client(container_name)
    upload_dir("data", dest)
    paths, down_files, upload_files = download('data','')
    clean_up(source, paths, down_files, upload_files)
    print(glob.glob('downloads/**', recursive=True))


except Exception as ex:
    print('Exception:', ex)

    