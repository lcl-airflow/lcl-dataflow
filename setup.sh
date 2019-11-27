PROJECT=$(gcloud config list project --format "value(core.project)")
BUCKET=gs://$PROJECT-dataflow
gsutil mkdir $BUCKET
gsutil cp data/export* $BUCKET/model/
gzip -kdf data/images.txt.gz
gsutil cp data/images.txt $BUCKET/input/

python3 -m virtualenv airflow-dataflow
source airflow-dataflow/bin/activate
pip install apache-beam[gcp]
git config --global user.email $1
git config --global user.name "lcl-airflow"
ssh-keygen -t rsa -f ~/.ssh/id_rsa -C $1  -q -P ""
