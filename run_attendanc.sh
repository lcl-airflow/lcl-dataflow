source airflow-dataflow/bin/activate
PROJECT=$(gcloud config list project --format "value(core.project)")
IN_FILENAME=dept-data.txt	
OUT_FILENAME=part
TEMP=gs://$PROJECT-demo/tmp
INPUT=gs://$PROJECT-demo/$IN_FILENAME
OUTPUT=gs://$PROJECT-demo/outputs/$OUT_FILENAME
RUNNER=DataflowRunner
REGION=us-east1
MACHINE_TYPE=n2-highmem-32
NUM_WORKERS=4
MAX_NUM_WORKERS=16

####################################################
#NOTES: https://cloud.google.com/dataflow/docs/guides/specifying-exec-params (full text)
#
#service_account_email:
#  - https://cloud.google.com/dataflow/docs/concepts/security-and-permissions#controller_service_account
#
#WORK_DISK_TYPE
#autoscaling_algorithm
#dataflow_kms_key
#
#####################
python attendance.py --input $INPUT \
                     --output $OUTPUT \
                     --runner $RUNNER \
                     --project $PROJECT \
                     --temp_location $TEMP \
                     --region $REGION \
                     --machine_type $MACHINE_TYPE
echo $?
