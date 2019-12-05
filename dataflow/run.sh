PROJECT=$(gcloud config list project --format "value(core.project)")
BUCKET=gs://$PROJECT-dataflow
python ../dataflow/run.py \
    --runner DataflowRunner \
    --project $PROJECT \
    --staging_location $BUCKET/staging \
    --temp_location $BUCKET/temp \
    --job_name $PROJECT-prediction-cs \
    --model $BUCKET/model \
    --input $BUCKET/input/images.txt \
    --output $BUCKET/output/predict
    