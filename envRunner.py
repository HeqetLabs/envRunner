"""envRunner

Usage:
  envRunner (-h | --help)
  envRunner <config> exec [COMMAND ...]

Options:
  -h --help   Shows this screen.
  --version
"""
from docopt import docopt
from urlparse import urlparse
import json
import os
import requests
import subprocess
import yaml

def read_local_file(filename):
  _,ext = os.path.splitext(filename)
  ext = ext.lower()

  if ext == ".yaml" or ext == ".yml":
    return _read_yaml_file(filename)
  elif ext == ".js" or ext == ".json":
    return _read_json_file(filename)
  else:
    raise Exception("Could not read" + filename)

def _read_yaml_file(filename):
  return yaml.load(open(filename, "r"))

def _read_json_file(filename):
  return json.load(open(filename, "r"))

def read_remote_file(url):
  r = requests.get(url)

  try:
    return json.loads(r.text)
  except (ValueError):
    return yaml.load(r.text)

if __name__ == '__main__':
  arguments = docopt(__doc__, version='envRunner v0.1')
  parsed_uri = urlparse(arguments["<config>"])

  environment = {}
  if "http" in parsed_uri.scheme:
    #read from web
    environment = read_remote_file(parsed_uri.geturl())
    print environment
  elif "file" in parsed_uri.scheme or parsed_uri.scheme == "":
    environment = read_local_file(parsed_uri.path) 

  env = dict(os.environ, **{ k: str(environment[k]) for k in environment})
  if arguments["exec"]:
    process = subprocess.Popen(arguments["COMMAND"], env=env)
