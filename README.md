# Monoloves
## Not Your Ordinary Love Games.


[![My Tech Stack](https://github-readme-tech-stack.vercel.app/api/cards?title=Monoloves%20Tech%20Stack&lineCount=3&line1=django,django,0c7e3d;mongodb,mongodb,04810c;python,python,04810c;&line2=html5,html5,04810c;javascript,javascript,04810c;flask,flask,04810c;&line3=css3,css3,04810c;tensorflow,tensorflow,04810c;)](https://github-readme-tech-stack.vercel.app/api/cards?title=Monoloves%20Tech%20Stack&lineCount=1&line1=django,django,0c7e3d;mongodb,mongodb,04810c;python,python,04810c;&line2=html5,html5,04810c;javascript,javascript,04810c;flask,flask,04810c;&line3=css3,css3,04810c;tensorflow,tensorflow,04810c;)


> The project is built as a hobby project - With **no affiliation** to any organization


Current web app only can predict if you probably match or no using [speed dating data](https://www.kaggle.com/datasets/annavictoria/speed-dating-experiment) this web app on v1 version.

## Put Any Other feature that You Want

> Feel free to contribute here.

1. you can add more feature by creating another models since this web has been built using django framework.
2. this web still on a long journey, more feature will be available in the next version.

## Features

- predict if you were match or no with your partner by filling the form


## How to install locally

- Install python interpreter
- create two virtual env using venv package
```
pip -m venv <virtual env name> 
```
- install the requirements_django for web serving
- install the requirements_model_api for serving the machine learning
- after all of the requirements are installed then run the flask server in the model_api dir using the prompt below
```
flask run
```
- after the flask api running, run the django web serving by get into the dating_web directory then run using the prompt below
```
python manage.py runserver
```
- you would not get any error if the installations are work slimly

