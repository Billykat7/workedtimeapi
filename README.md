# workedtimeapi
API to calculate seconds in a working day with two given ISO format times.

This project provides an API end point that will calculate the total number of business seconds between two given times. 
A business second is defined as any whole second that elapses after 08:00 and before 17:00 during a 
weekday (Monday - Friday) that is not a public holiday in the Republic of South Africa. The end point 
must support only list GET requests and must take two parameters: start_time and end_time. 
Parameter values will be in ISO-8601 format. You are guaranteed that start_time will be before end_time, or otherwise 
provide a suitable response. The end point must respond with only a single integer value for successful requests or 
a suitable error message string for failed requests.
