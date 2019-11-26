# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import argparse
import json
import logging
import os

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class MyOptions(PipelineOptions):

  @classmethod
  def _add_argparse_args(cls, parser):
    parser.add_argument('--input', dest='input', required=True,
                      help='Input file to process.')
    parser.add_argument('--output', dest='output', required=True,
                      help='Output file to write results to.')
    parser.add_argument('--model', dest='model', required=True,
                      help='Checkpoint file of the model.')
    parser.add_argument('--source', dest='source', required=True,
                      help='Data source location (cs|bq).')


def run(argv=None):
  parser = argparse.ArgumentParser()
  


p = beam.Pipeline(options=MyOptions())

print (p.options.input)
print (p.options.output)
print (p.options.model)
print (p.options.source)


