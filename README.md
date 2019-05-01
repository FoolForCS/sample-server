# Backend/DevOps Engineer @ xbird challenge

Thank you for applying at xbird! We think you are a very promising candidate and would like to move on with the following challenge. Build a system that accepts sample uploads and writes each sample to a database. Deploy the system to a container solution.

## Specification

- Write a REST API server that accepts HTTP POST requests containing valid `Sample`[ protocol buffer messages](https://developers.google.com/protocol-buffers/). It must write the samples to a database of your choice. When choosing a database and defining your schema (or none), keep in mind that you might want to filter samples using attributes of their data.
    - If the upload body is invalid or writing to the database fails, the endpoint should respond with an error.
    - If the upload succeeds, the endpoint's response should indicate that along with a number of processed objects on the current request.
- Write a client script that reads the json source files, creates the equivalent `Sample` protocol buffer objects and sends them to the server. Think about how to represent a collection of samples in the upload body.
- Ensure your system can be deployed as multi-container application, preferably using [Kubernetes](https://kubernetes.io), alternatively using[ Docker Compose](https://docs.docker.com/compose/overview/). You might actually deploy it, for example, to [Google Cloud Platform](https://cloud.google.com) using the [Free Trial](https://cloud.google.com/free-trial/).

We think there is enough time to complete the all the tasks, in case there is not, they are sorted according to our preferences.

Please document your results along with the answers to the *Questions* section. Then email us back either a zip file or a GitHub link.

## Attachments

- `sample.proto` contains the relevant protocol buffer definitions.
- `activity.json` contains four weeks of activity data, one per line.
- `location.json` contains four weeks of location data, one per line.
- Acceleration samples are intentionally not provided.

## Questions

- Explain your database choice
- How would you modify the system if the number of samples becomes really big?
- How would you monitor the running services?


## Bonus questions

If you would like a chance to play around with the data you can also give these questions a go:

- Location data represents significant location changes:
    > The significant-change location service delivers updates only when there has been a significant change in the device’s location, such as 500 meters or more.
    Based on the location samples supplied, what are the three places where the user spends most of their time?
    
- Given the most common places for the user, identify what kind of location they represent for the user. You can use any additional data sources (provided or not) to find the answer.
>>>>>>> initial commit
