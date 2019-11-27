source airflow-dataflow/bin/activate
PROJECT=$(gcloud config list project --format "value(core.project)")
IN_FILENAME=dept-data.txt	
OUT_FILENAME=part
TEMP=gs://$PROJECT-demo/tmp
INPUT=gs://$PROJECT-demo/$IN_FILENAME
OUTPUT=gs://$PROJECT-demo/outputs/$OUT_FILENAME
RUNNER=DataflowRunner
REGION=us-east1
MACHINE_TYPE=n1-standard-16
echo $PROJECT
echo $INPUT
echo $OUTPUT

python attendance.py --input $INPUT \
                     --output $OUTPUT \
                     --runner $RUNNER \
                     --project $PROJECT \
                     --temp_location $TEMP \
                     --region $REGION \
                     --machine_type $MACHINE_TYPE