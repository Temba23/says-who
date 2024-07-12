                                        SAYS WHO?
In this project, I have created a game project where the user have to answer the mcq questions where the quote of any star is a question
and player have to give the answer. Player has 3 lifelines and with each incorrect answer it decreases whereas with correct answers 
increases points.

![alt text](image.png)

To play this game :

1. git clone https://github.com/Temba23/says-who.git

2. create env and install requirements :
    - python -m venv env
    - pip install -r requirements.txt

3. run migrations :
    - python manage.py makemigrations
    - python manage.py migrate

4. add questions/ Quote/ Star or for default :
    - python manage.py runserver
    - visit localhost/question/

5. enjoy 

Temba - Says Who?