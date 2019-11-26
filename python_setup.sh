PROJECT=$(gcloud config list project --format "value(core.project)")
BUCKET=gs://$PROJECT-dataflow
gsutil mkdir $BUCKET
gsutil cp data/export* $BUCKET/model/
gzip -kdf data/images.txt.gz
gsutil cp data/images.txt $BUCKET/input/

git clone https://github.com/GoogleCloudPlatform/dataflow-prediction-example
python -m virtualenv airflow-dataflow
source airflow-dataflow/bin/activate
pip install apache-beam[gcp]

