# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: datalake_samples_upload_download.py
DESCRIPTION:
    This sample demonstrates:
    * Set up a file system
    * Create file
    * Append data to the file
    * Flush data to the file
    * Get file properties
    * Download the uploaded data
    * Delete file system
USAGE:
    python datalake_samples_upload_download.py
    Set the environment variables with your own values before running the sample:
    1) STORAGE_ACCOUNT_NAME - the storage account name
    2) STORAGE_ACCOUNT_KEY - the storage account key
"""

import os
import random
connect_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]

from azure.storage.filedatalake import (
    DataLakeServiceClient, DataLakeFileClient, DataLakeDirectoryClient
)
SOURCE_FILE = 'SampleSource.txt'
container_name = "blob-container-01"


def upload_download_sample(file_path, dl_path, file_client, filesystem_client='', file_content='', file_name=''):
    print(f'Uploading {file_path} to {dl_path}')
    #with open(file_path, 'rb') as datas:
     ##   file_client.append(datas)    
    file_client.flush_data(len(file_client))

    # Get file properties
    # [START get_file_properties]
    #properties = file_client.get_file_properties()
    # [END get_file_properties]

    # read the data back
    #print("Downloading data from '{}'.".format(file_name))
    # [START read_file]
    #download = file_client.download_file()
    #downloaded_bytes = download.readall()
    # [END read_file]

    # verify the downloaded content
    #if file_content == downloaded_bytes:
    #    print("The downloaded data is equal to the data uploaded.")
    #else:
     #   print("Something went wrong.")

    # Rename the file
    # [START rename_file]
    #new_client = file_client.rename_file(file_client.file_system_name + '/' + 'newname')
    # [END rename_file]

    # download the renamed file in to local file
    """with open(SOURCE_FILE, 'wb') as stream:
        download = new_client.download_file()
        download.readinto(stream)
"""
    # [START delete_file]
    #new_client.delete_file()
    # [END delete_file]


def run(source, dest):
    account_name = os.getenv('STORAGE_ACCOUNT_NAME', "")
    account_key = os.getenv('STORAGE_ACCOUNT_KEY', "")

    # set up the service client with the credentials from the environment variables
    service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
        "https",
        account_name
    ), credential=account_key)

    #client = service_client.get_directory_client(container_name)

    '''
    Upload the whole directory into the storage account
    '''
    
    for root, dirs, files in os.walk(source):

        for name in files:    
            dir_part = os.path.relpath(root, source)

            dir_part = '' if dir_part == '.' else dir_part + '/'

            file_path = os.path.join(root, name)

            dl_path = dir_part + name
        
            filesystem_client = service_client.get_file_system_client(file_system =container_name)

            file_client = filesystem_client.get_file_client(name)
            
           # file_client.create_file()

            upload_download_sample(file_path, dl_path,file_client)

            
    # create the filesystem
    #filesystem_client = service_client.create_file_system(file_system=fs_name)

    # invoke the sample code
    #try:
        
        #upload_download_sample(filesystem_client)
    #finally:
        # clean up the demo filesystem
        #filesystem_client.delete_file_system()


if __name__ == '__main__':
    run("data", '')
