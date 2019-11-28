from google.cloud import bigquery
client = bigquery.Client()

def createDataset(DataSetName):
    dataset_id = "{}.{}".format(client.project, DataSetName)
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"
    dataset = client.create_dataset(dataset)  # API request
    print("Created dataset {}.{}".format(client.project, dataset.dataset_id))

def createTable(DataSetName, TableName):

    createDataset(DataSetName)

    #schema = [
    #bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
    #bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
    #]


    table_id = "{}.{}.{}".format(DataSetName,TableName)

    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  # API request
    print("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))

def loadtoTable(DataSetName, TableName, GCSpath):

    dataset_ref = client.dataset(DataSetName)
    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = True
    job_config.source_format = bigquery.SourceFormat.CSV
    uri = GCSpath
    load_job = client.load_table_from_uri(
    uri, dataset_ref.table(TableName), job_config=job_config
    )  # API request
    print("Starting job {}".format(load_job.job_id))

    load_job.result()  # Waits for table load to complete.
    print("Job finished.")

    destination_table = client.get_table(dataset_ref.table(TableName))
    print("Loaded {} rows.".format(destination_table.num_rows))

if __name__ == "__main__":
    #createDataset("SAP")
    loadtoTable("SAP", "MARA", "gs://playground-s-11-7e0ddc-dataflow/MARA_20191007190003_0001.txt")
