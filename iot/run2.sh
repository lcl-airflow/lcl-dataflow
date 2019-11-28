 echo "Create IOT Service Account"
 gcloud iam service-accounts create $SERVICE_ACCT \
    --description $SERVICE_ACCT \
    --display-name $SERVICE_ACCT

echo "Adding ROles to Service Account"

gcloud projects add-iam-policy-binding $PROJECT \
  --member serviceAccount:$SERVICE_ACCT@$PROJECT.iam.gserviceaccount.com \
  --role roles/owner


 

 
 node cloudiot_mqtt_example_nodejs.js \
    mqttDeviceDemo \
    --projectId=$PROJECT \
    --cloudRegion=us-central1 \
    --registryId=my_registery \
    --deviceId=my-registry \
    --privateKeyFile=rsa_private.pem \
    --numMessages=25 \
    --mqttBridgePort=443 \
    --algorithm=RS256


gcloud iam service-accounts create $SERVICE_ACCT \
    --description "iot-test" \
    --display-name "iot test user"