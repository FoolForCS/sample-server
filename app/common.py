from sample_pb2 import Sample, Location, Acceleration, Activity

# Takes an array of data objects and constructs them into their right objects
def parse_objects(data_array):
    location, activity, acceleration = ([], [], [])
    for data_with_timestamp in data_array:
        (id, data, timestamp) = data_with_timestamp
        if data.Is(Location.DESCRIPTOR):
            loc = Location()
            data.Unpack(loc)
            location.append((id, loc, timestamp))
        elif data.Is(Activity.DESCRIPTOR):
            act = Activity()
            data.Unpack(act)
            activity.append((id, act, timestamp))
        elif data.Is(Accelaration.DESCRIPTOR):
            acc = Accelaration()
            data.Unpack(acc)
            acceleration.append((id, acc, timestamp))
    return (location, activity, acceleration)