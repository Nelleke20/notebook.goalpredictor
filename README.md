# notebook.goalpredictor

# first step is to create a model that predicts scores
- check worldcup input data: DONE
- check imbalanced dataset: DONE
- create predictor: DONE

# second step is to create a working-api in a docker 
- fast api(faster than flask): DONE running in app folder - uvicorn main:app --reload
- check and test swagger: DONE
- docker container(docker build -t dockerfile)): DONE 

# possible next steps: create a working front-end for other users 
create an app where you can run a button and get the score for the nxt minute on my raspberry pi
- create front-end input var DOING (example: see repo webserver.sensor)

# next steps for production:
a cloud/data engineer could then focus on deploying the api and the flow in the cloud by:
creating a kubernetes cluster and deploying the api via the docker container.




---------------

flask-app:
python flask_app.py