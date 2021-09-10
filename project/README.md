# anymindtest

Steps to run:
1. Clone the repository: `git clone https://github.com/mrpeem/anymindtest.git`
2. Go into the cloned directory and the project directory: `cd anymindtest/project/`
3. Run the server: `python manage.py runserver` <br>
  --if encounter any issues with packages, install with pip: `pip install -r requirements.txt`
4. Getting the data
  Can either use CURL, Postman, or run it in the browser
5. Server name: **localhost:8000**

API endpoints:
1. Get tweets by a hashtag: **/hashtags/{hashtag}** <br>
   --Optional parameter: limits: **/hashtag/{hashtag}?limit=10** <br><br>
  Example: http://localhost:8000/hashtags/python?limit=10<br>
  --To run with CURL: `curl http://localhost:8000/hashtags/python/?limit=10`<br><br>
2. Get user tweets: **/users/{user_handle}** <br>
    --Optional parameter: limit: **/users/{user_handle}?limit=10**<br><br>
  Example: http://localhost:8000/users/mkbhd/ <br>
  --To run with CURL:  `curl http://localhost:8000/users/mkbhd/`



