PROJECT=$(gcloud config list project --format "value(core.project)")
gsutil mb gs://$PROJECT-demo/
gsutil cp sample_data/dept-data.txt gs://$PROJECT-demo/