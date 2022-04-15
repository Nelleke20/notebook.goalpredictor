# notebook.goalpredictor

An API is a set of definitions and protocols for building and integrating application software. It’s sometimes referred to as a contract between an information provider and an information user—establishing the content required from the consumer (the call) and the content required by the producer (the response). 
REST is a set of architectural constraints, not a protocol or a standard. API developers can implement REST in a variety of ways. When a client request is made via a RESTful API, it transfers a representation of the state of the resource to the requester or endpoint. This information, or representation, is delivered in one of several formats via HTTP: JSON (Javascript Object Notation), HTML, XLT, Python, PHP, or plain text.
https://www.redhat.com/en/topics/api/what-is-a-rest-api#:~:text=A%20REST%20API%20(also%20known,by%20computer%20scientist%20Roy%20Fielding.


# first step is to create a model that predicts scores
- check worldcup input data: DONE
- check imbalanced dataset: DONE
- create predictor: DONE

# second step is to create an api in a docker container
- fast api(faster than flask): DONE running in app folder - uvicorn main:app --reload
- check swagger: DONE

- docker container(docker build -t dockerfile)) : DONE
docker build -t predictor .


# next steps: my goal is to create an api on my local machine. 
create an app where you can run a button and get the score for the nxt minute on my raspberry pi
- create front-end button:
https://towardsdatascience.com/how-to-easily-build-your-first-machine-learning-web-app-in-python-c3d6c0f0a01c#e14b
- input data frmo random_int

# next steps for production:
a cloud/data engineer could then focus on deploying the api and the flow in the cloud by:
creating a kubernetes cluster and deploying the api via the docker container.