# workedtimeapi
FULL BUSINESS DAY SECONDS CALCULATING - API

END POINTS

- Calculate the total number of business seconds between two given times. A business second is defined as any whole second that elapses after 08:00 and before 17:00 during a weekday (Monday - Friday) that is not a public holiday in the Republic of South Africa. 

- The end point must support only list GET requests and must take two parameters: start_time and end_time. Parameter values will be in ISO-8601 format. You are guaranteed that start_time will be before end_time. 

- The end point must respond with only a single integer value for successful requests or a suitable error message string for failed requests.


Notes:

Please use requirements.txt to install packages in order to avoid error and malfunctioning due to versions conflicts and incompatibility.

python -m pip install -r requirements.txt

django-toolbelt==0.0.1
Django==1.9.1
djangorestframework==3.3.2
holidays==0.9.10
python-dateutil==2.8.0
PyYAML==3.11
six==1.12.0


I used Postman to test. But tests can be done with other tools you can use to push a 'GET' command.
