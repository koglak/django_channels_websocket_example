# Django Channels Websocket Project

Here is the tutorial that I implemented: [Channels Tutorial](https://channels.readthedocs.io/en/stable/tutorial/part_1.html)

![ezgif com-video-to-gif](https://github.com/koglak/django_channels_websocket_example/assets/24697147/ebe7270d-fa3f-4952-8901-6560193c5ea6)


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
