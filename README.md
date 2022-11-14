# TP1_Datalake_integration

# Lab1: Data lakes and data integration in Azure

### Create a virtual environment

python -m venv .venv
source .venv/bin/activate

### Install the azure dependencies

pip install -r requirements.text

### Upload our unstructured data files

I used the BlobServiceClient to upload local data in the Azure Storage Account blob container

![results.png](Lab1%20Data%20lakes%20and%20data%20integration%20in%20Azure%20423a233a4ace440492d27896639040c1/results.png)

Data is well stored as a data lake inside our â€œblob-container-01â€.

![Untitled](Lab1%20Data%20lakes%20and%20data%20integration%20in%20Azure%20423a233a4ace440492d27896639040c1/Untitled.png)

### Download blobs in the local directory

I download the blobs to retrieve data locally.

### Remove the data lake and data locally

I remove the upload and download paths and the local filesystem downloaded. 

![Untitled](Lab1%20Data%20lakes%20and%20data%20integration%20in%20Azure%20423a233a4ace440492d27896639040c1/Untitled%201.png)

![Untitled](Lab1%20Data%20lakes%20and%20data%20integration%20in%20Azure%20423a233a4ace440492d27896639040c1/Untitled%202.png)
