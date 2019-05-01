from quart import abort, Blueprint, current_app, jsonify, request
import sample_pb2 
from common import parse_objects
import psycopg2
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32
import io
import logging

blueprint = Blueprint('sample', __name__)

"""
This takes in a bunch of protobuf data and then expects the encoding to be of the form
[length of message ++ actual message]. It gets the length and then proceeds to the actual message.
It does this repeatedly until it is out of bytes to read.
It returns the objects parsed into their respective location, activity or acceleration types.
"""
def unmarshal_message(data):
    data_set = []
    f = io.BytesIO(data)
    buf = f.read()
    n = 0
    while n < len(buf):
        msg_len, new_pos = _DecodeVarint32(buf, n)
        n = new_pos
        msg_buf = buf[n:n+msg_len]
        n += msg_len
        sample_data = sample_pb2.Sample()
        sample_data.ParseFromString(msg_buf)
        data_set.append((sample_data.id, sample_data.data, sample_data.timestamp))
    return parse_objects(data_set)

"""
The next three functions are used for inserting the information into the database.
This could be made async to improve performance.
"""
#TODO: Make the writes to the database async.
def insert_location_data(locations):
    data = []
    for location_with_time in locations:
        (id, location, timestamp) = location_with_time
        data.append((id, location.longitude, location.latitude, timestamp.ToJsonString()))
    cursor = current_app.conn.cursor()
    data_str = ','.join(cursor.mogrify("(%s,%s,%s,%s)", x).decode("utf-8") for x in data)
    cursor.execute("INSERT INTO location VALUES " + data_str)
    cursor.close()
    current_app.conn.commit()

def insert_acceleration_data(accelerations):
    data = []
    for acceleration_with_time in accelerations:
        (id, acc, timestamp) = acceleration_with_time
        data.append((id, acc.x, acc.y, acc.z, timestamp.ToJsonString()))
    cursor = current_app.conn.cursor()
    data_str = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s)", x).decode("utf-8") for x in data)
    cursor.execute("INSERT INTO acceleration VALUES " + data_str)
    cursor.close()
    current_app.conn.commit()

def insert_activity_data(activity):
    data = []
    for activity_with_time in activity:
        (id, act, timestamp) = activity_with_time
        print(id, act.unknown, act.stationary, act.walking, act.running, timestamp.ToJsonString())
        data.append((id, act.unknown, act.stationary, act.walking, act.running, timestamp.ToJsonString()))
    cursor = current_app.conn.cursor()
    data_str = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s)", x).decode("utf-8") for x in data)
    cursor.execute("INSERT INTO activity VALUES " + data_str)
    cursor.close()
    current_app.conn.commit()
    
# This is the path taken by our endpoint
@blueprint.route('/samples/', methods=['POST'])
async def add_samples():
    data = await request.get_data()
    try:
        (l, a, acc) = unmarshal_message(data)
        # insert each set into the database
        if len(l):
            insert_location_data(l)
        if len(a):
            insert_activity_data(a)
        if len(acc):
            insert_acceleration_data(acc)
        return jsonify({
            'status': "Success",
            'processed': len(l) + len(acc) + len(a),
        })
    except:
        #TODO: This can be improved to point to the specific error. It could be a parsing error or a database write failure.
        logging.exception("Something went wrong")
        return jsonify({
            'status': "Failed",
            'reason': "Unknown"
        })