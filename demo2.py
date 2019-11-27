import apache_beam as beam
def SplitRow(element):
    return element.split(',')

def filtering(record):
    return record[3] == 'Accounts'

def listing(record):
    return (record[1],1)

p1 = beam.Pipeline()

attendance_count = (
    
    p1 
     |"Read" >> beam.io.ReadFromText('dept-data.txt')
     |"Split" >> beam.Map(lambda element: element.split(','))
     |"Filter" >> beam.Filter(lambda record: record[3] == 'Accounts')
     |"Map Name" >> beam.Map(lambda record: (record[1],1))
     |"Combin name" >> beam.CombinePerKey(sum)
     |"Write to beam" >> beam.io.WriteToText('data/output_new2')
)

p1.run()