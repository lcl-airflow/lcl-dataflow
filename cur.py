def SplitRow(element):
    return element.split(',')

def filtering(record):
    return record[3] == 'Accounts'

def listing(record):
    return (record[1],1)

p1 = beam.Pipeline()

input_collection = (
                  p1
                  |"Read" >> beam.io.ReadFromText('dept-data.txt')
                  | "Split" >> beam.Map(lambda element: element.split(','))
                  )

account_count = (
                  input_collection
                  |"Filter" >> beam.Filter(lambda record: record[3] == 'Accounts')
                  |"Map Name" >> beam.Map(lambda record: (record[1],1))
                  |"Combin name" >> beam.CombinePerKey(sum)
                  |"Write to beam" >> beam.io.WriteToText('data/account')
)
hr_count = (
                  input_collection
                  |"Filter" >> beam.Filter(lambda record: record[3] == 'HR')
                  |"Map Name" >> beam.Map(lambda record: (record[1],1))
                  |"Combin name" >> beam.CombinePerKey(sum)
                  |"Write to beam" >> beam.io.WriteToText('data/hr')
)

p1.run()
