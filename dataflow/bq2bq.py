import argparse
import json
import logging
import os

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam.io.gcp.pubsub as pubsub


def run(argv=None):
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', dest='input', required=True,
                      help='Input file to process.')
  parser.add_argument('--output', dest='output', required=True,
                      help='Output file to write results to.')
  parser.add_argument('--model', dest='model', required=True,
                      help='Checkpoint file of the model.')
  parser.add_argument('--runner', dest='runner', required=True)
  parser.add_argument('--project', dest='project', required=True) 
  known_args, pipeline_args = parser.parse_known_args(argv)
  print ( known_args )
  p3 = beam.Pipeline()
  lines1 = (p3
           | 'QueryTable' >> beam.io.Read(beam.io.BigQuerySource(
            query='SELECT max_temperature FROM '\
              '[clouddataflow-readonly:samples.weather_stations]'))
           )
  p3.run()


    
       