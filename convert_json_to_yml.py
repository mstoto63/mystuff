import sys
import json
import yaml


inputfile = sys.argv[1]
outputfile = inputfile.replace(".json",".yml")

f = open(outputfile,"w")

f.write(yaml.dump(yaml.load(json.dumps(json.loads(open(inputfile).read()))), default_flow_style=False))
