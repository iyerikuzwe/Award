# author
    Iyerikuzwe Regine
# project-name
    ikuzweprojects
# Project-description

    This is a website where users get to post previously done projects for review purposes. One posts a screenshot of the landing page, a brief description of the site, a title and a link to the site. The project is the rated based on three criteria, i.e Design, Usability and Content
# user stories
    As a user, I would like to:

    View posted projects and their details
    Post a project to be rated/reviewed
    Rate/ review other users' projects
    Search for projects 
    View projects overall score
    View my profile page

### Prerequisites

    Python 3.6 required and the django=1.11 framework.

### Set-Up

    To access this app on your local machine:

    1) Clone the repo
    2) Create a virtual environment then pip install requirements.txt
    3) On your terminal route to the root folder then run: python manage.py runserver
    4) Create database - on terminal, run `psql`
    5) Create a .env file and add the following:
        i) SECRET_KEY = `<Secret_Key>`
        ii) DB_NAME = `<your_db_name`
        iii) DB_PASSWORD = `your_password`
        iv) DEBUG = `True`
   
    6) Run Migrations `python3.6 manage.py makemigrations <name of the app>` then `python3.6 manage.py migrate`
    7) On terminal run `python3.6 manage.py runserver`

## Features
    1) Users can upload projects they've done
    2) Users can view their profiles
    3) User can rate/review each other's projects
    4) Authenticated users can view profile and project details using API


### Known bugs

There are no known bugs.

### Technologies used

This application was made with Python version 3.6 using the django framework. The templates were made using html and was styled using css and bootstrap 3. The database used was postgresql, it was edited using visual studio code and deployed to heroku.

## Support and Contact details
Incase of additions or if you run into any issues, my email address is: .iyerikuzweregine19@gmail.com
or call 0789140216

## License

Copyright (c) 2019 Iyerikuzwe Regine

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgement
    1. I would like to express my deepest appreciation to moringa school who provided me the possibility to complete this project.
    2.  A special gratitude I give to my mentors,  whose contribution in stimulating suggestions and encouragement,  helped me to coordinate my project.

    3. Furthermore I would also like to acknowledge with much appreciation the crucial role of my classmates who  help me to assemble the codes and gave suggestion about the task.
    4.  Last but not least, many thanks go to the mentor of the project, [Mr Saphani,Mr Aristote] whose have invested his full effort in guiding our team in achieving the goal.
    5. I have to appreciate the guidance given by other facilitators that has improved our projects skills,thanks to their comments and advices.