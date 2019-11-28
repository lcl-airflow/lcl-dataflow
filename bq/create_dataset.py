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

    schema = [
    bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]


    table_id = "{}.{}.{}".format(DataSetName,TableName)

    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  # API request
    print("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))


if __name__ == "__main__":
    createDataset("SAP")
