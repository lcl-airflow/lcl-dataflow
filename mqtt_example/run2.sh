 gcloud auth activate-service-account \
  test1-299@playground-s-11-a067f9.iam.gserviceaccount.com \
          --key-file=./playground-s-11-a067f9-01aad473b30d.json --project=playground-s-11-a067f9
 
 node cloudiot_mqtt_example_nodejs.js \
    mqttDeviceDemo \
    --projectId=playground-s-11-a067f9 \
    --cloudRegion=us-central1 \
    --registryId=my_registery \
    --deviceId=my-registry \
    --privateKeyFile=rsa_private.pem \
    --numMessages=25 \
    --mqttBridgePort=443 \
    --algorithm=RS256


