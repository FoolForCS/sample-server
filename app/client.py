#!/usr/bin/python

import http.client, json
import google.protobuf.json_format as json_format
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32

from sample_pb2 import Sample, Location, Acceleration, Activity
from common import parse_objects

def read_from_file(filename):
    data_set = []
    with open(filename) as f:
        for line in f:
            message = json_format.Parse(line, Sample())
            data_set.append(message)
    return data_set

# Enter the file name here
l = read_from_file("../activity.json")
f = b''
# Construct a stream of protobuf messages from the input
for act in l:
    size = act.ByteSize()
    f = f + (_VarintBytes(size))
    f = f + (act.SerializeToString())
params = f
headers = {"Content-type": "application/octet-stream"}
conn = http.client.HTTPConnection("127.0.0.1:5000")
conn.request("POST", "/samples/", params, headers)
response = conn.getresponse()
data = response.read()
print("The server responded with", data)
conn.close()
