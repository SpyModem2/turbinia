# -*- coding: utf-8 -*-
#!/usr/bin/env python

import subprocess
import sys

from turbinia import config

index_file = './index.yaml'

if len(sys.argv) > 1:
  function_names = [sys.argv[1]]
else:
  function_names = ['gettasks', 'getrecenttasks']

config.LoadConfig()

for function in function_names:
  print 'Deploying function {0:s}'.format(function)
  cmd = ('gcloud --project {0:s} beta functions deploy {1:s} --stage-bucket '
         '{2:s} --region {3:s} --trigger-http'.format(config.PROJECT, function,
                                       config.BUCKET_NAME, config.TURBINIA_REGION))
  print subprocess.check_call(cmd, shell=True)

print '/nCreating Datastore index from {0:s}'.format(index_file)
cmd = 'gcloud --quiet --project {0:s} datastore create-indexes {1:s}'.format(
    config.PROJECT, index_file)
subprocess.check_call(cmd, shell=True)
