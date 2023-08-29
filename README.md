# Django Channels Websocket Project

In this project there are 2 different app. 

* <strong>A chat application.</strong> Here is the tutorial that I implemented: [Channels Tutorial](https://channels.readthedocs.io/en/stable/tutorial/part_1.html)

![ezgif com-video-to-gif](https://github.com/koglak/django_channels_websocket_example/assets/24697147/ebe7270d-fa3f-4952-8901-6560193c5ea6)

* <strong>Momentary Commnucation Between Front&Back </strong>

When a method is completed, the informative message directly sent to frontend even though task has not been completed.

![ezgif com-video-to-gif (1)](https://github.com/koglak/django_channels_websocket_example/assets/24697147/0a10b447-1649-457f-a882-d9f364439569)


Establish Project to Your Local Env
-----


1. Create environment

         python -m venv myvenv
   
2. Activate enviroment

         env\Scripts\activate
        
3. Download requirements

         pip install -r requirements.txt
   
5. Migrate migrations

         python manage.py migrate

6. Run redis

        docker run -p 6379:6379 -d redis:5
   
7. Run app

        daphne mysite.asgi:application

8. Go to your local host: [http://localhost:8000](http://localhost:8000/)

Dockerize App
-----

Dockerfile is ready for usage. Please follow steps below:

1. Route Project Directory & Create Docker image

       docker build -t my-django-app .
   
2. Push to Registry

       docker push my-django-app
   
3. Run container
   
       docker run -p 8000:8000 my-django-app
   
4. Go to your local host: [http://localhost:8000](http://localhost:8000/)
