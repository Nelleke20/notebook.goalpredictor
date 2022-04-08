# notebook.goalpredictor

An API is a set of definitions and protocols for building and integrating application software. It’s sometimes referred to as a contract between an information provider and an information user—establishing the content required from the consumer (the call) and the content required by the producer (the response). 
REST is a set of architectural constraints, not a protocol or a standard. API developers can implement REST in a variety of ways. When a client request is made via a RESTful API, it transfers a representation of the state of the resource to the requester or endpoint. This information, or representation, is delivered in one of several formats via HTTP: JSON (Javascript Object Notation), HTML, XLT, Python, PHP, or plain text.
https://www.redhat.com/en/topics/api/what-is-a-rest-api#:~:text=A%20REST%20API%20(also%20known,by%20computer%20scientist%20Roy%20Fielding.


# first step is to create a model that predicts scores
- check worldcup input data: DONE
- check imbalanced dataset: DONE
- create predictor: DONE

# next steps: my goal is to create an api on my local machine. 
check fast and flask api
check swagger
create an app where you can run a button and get the score for the nxt minute

# next steps for production:
a cloud/data engineer could then focus on deploying the api and the flow in the cloud by:
creating a kubernetes cluster and deploying the api via a docker container with seldon.