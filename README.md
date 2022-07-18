# notebook.goalpredictor
I aim to have some fun with an imbalanced dataset. I expect it to be very hard to predict goals (if it were easy; wouldn't everybody have done it by now?) But my goal is not to create a high scoring model. My goal is to check what strategy works best for this imbalanced dataset, have some fun with soccer data, and see if i can deploy it as an API that can be used by other people.

# first step is to create a model that predicts scores
- check worldcup input data: DONE
- check imbalanced dataset: DONE
- create predictor: DONE

# second step is to create a working-api in a docker 
- fast api(faster than flask): DONE running in app folder - uvicorn main:app --reload
- check and test swagger: DONE
- built a docker container(docker build -t dockerfile)): DONE 

# possible next steps: create a working front-end for other users 
create an app where you can run a button and get the score for the nxt minute on my raspberry pi
- create front-end input webpage PARTLY DONE (extra example: see repo webserver.sensor)
