# Backend/DevOps Engineer @ xbird challenge
The app/ contains all the source code.
To run the code you need a postgres server to be setup first. This postgres server should contain the tables 'location', 'activity' and 'sample'. It should have write privelages to a user 'newuser' who will use 'password' to authenticate. These things are currently hard-coded in the system. I'm working on making it generic and deployable but I wanted to update on the progress about the completion of the business logic in the code.

'source app/activate' to activate the virtual area.
python3 run.py to run the server.

Note that this is not how it'll be deployed in production. We will probably need to layer it on top of gunicorn as well.
## Design considerations
- I've used quart for the backend server. It uses asyncio over flask and is easy to prototype. It needs to be used with a gunicorn like solution in production.
- I've encoded protobufs as a stream of messages whose size is detailed by an integer prefixing each message. This allows me to represent a long sequence of protcol buffer messages easily. The reason I had to do this on my own was because protocol buffers do not provide any out of the box method for streaming.
- I've not implemented error handling very well due to a time crunch - I've noted that this could be improved to point to the specific error. Given time, I can make this better as well.

## Database choice
- I've used Postgresql for storing the data. The reason for this choice is because we wish to do some aggregations/filtering on the data. These kind of operations are usually faster on a relational database. It also has good support for python.
- I've aggregated the request and made bulk inserts into tables. If the size of the request would get really large, I'd need to split up the request data and then do bulk inserts. We can potentially do some error handling as well on the data to avoid failures in bulk inserts. Those things have not been considered yet.
- There are three tables in the postgres db - one for each type of data: (activity, location, acceleration). I set these up before hand with 'newuser' and 'password' as password.

## If the number of samples become really big
- I'd probably partition the system and have multiple instances of the servers.
- In addition, I'll try to parallelize as much of the code as possible. For instance, while I'm still reading protobuf messages, I could start writing a chunk of protobufs that I've already got onto the database. Given the amount of time, I've not optimized the code to support these kind of things just yet, but they could surely be added.

## Monitoring
- I believe setting up lots of metrics and telemetries to allow for easy monitoring of the system. Example metrics would be: response times of the server, size of the protobuf messages being sent to the server, number of database transactions being made, time taken for each transaction, number of pending requests at a time, etc.
- In addition to these metrics, one could then set up thresholds on sane values and setup alerting whenever those thresholds are violated.

## Bonus questions
| longitude | latitude | count |
| :---:   | :-: | :-: |
 | 13.4034529455246 | 52.5476395228265 | 9 |
 | 13.3987157382968 | 52.5462835873742 | 8 |
 | 13.4032220930736 | 52.5476969210846 | 7 |
 This was using the query - postgres=> select longitude, latitude, count(*) as c from location group by latitude, longitude order by c desc;
