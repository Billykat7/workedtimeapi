from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.reverse import reverse

import holidays, time, re, datetime, calendar
from datetime import datetime, date

@api_view()
def homePage(request):
	"""
	Welcome to the home page of our worked-time calculating API. Acceptable requests are during Weekdays, between 08:00:00 & 17:00:00. No ZA public holidays.
	"""
	return Response({
	'timeworked': reverse('timeworked', request=request),
	})

saHolidays = holidays.ZA()
dateToday = datetime.now()
dateTodayISO = datetime.now().isoformat()
holidayCheck = dateToday in saHolidays
weekdayCheck = calendar.day_name[dateToday.weekday()]

@api_view()
def timeworked(request):
	"""
	Time Worked calculation function. 
			timeworked(
				start_time=08:00:00,
				end_time=17:00:00,
			)
	example call: **host**/timeworked/?start_time=08:00:00&end_time=17:00:00, and should return a JSON like:
	{'business_seconds': 32400}
	"""

	if weekdayCheck == 'Saturday':
		return Response({"Please note, No calculations allowed on Weekends."})
	elif weekdayCheck == 'Sunday': 
		return Response({"Please note, No calculations allowed on Weekends."})
	elif holidayCheck == True:
		return Response({"Today is a public holiday in RSA. Please note, no calculations allowed on SA public holidays."})
	elif holidayCheck == False:
		try:
			inTimeStart = request.GET.get('start_time')
			if inTimeStart == None:
				return Response({"Waiting for time values to be entered...."})
			timeStartSTR = re.findall('[0-9]+', inTimeStart)
			numberSPulled = [ int(timeCutS) for timeCutS in timeStartSTR ]
			if numberSPulled[0] > 24 or numberSPulled[1] > 60 or numberSPulled[2] > 60:
				return Response({"Please make sure that hours are less than 24, minutes less than 60 and Seconds less than 60."})

			start_time = (numberSPulled[0])*3600 + (numberSPulled[1])*60 + numberSPulled[2]
			if start_time < 28800:
				return Response({"Please note: No public holidays. Weekdays only, from 08:00 - 17:00."})
			elif 61200 < start_time:
				return Response({"Please note: No public holidays. Weekdays only, from 08:00 - 17:00."
				})

			inTimeEnd = request.GET.get('end_time')
			if inTimeEnd == None:
				return Response({"Waiting for time values to be entered...."})
			timeEndSTR = re.findall('[0-9]+', inTimeEnd)
			numberEPulled = [ int(timeCutE) for timeCutE in timeEndSTR ]
			if numberEPulled[0] > 24 or numberEPulled[1] > 60 or numberEPulled[2] > 60:
				return Response({"Please make sure that hours are less than 24, minutes less than 60 and Seconds less than 60."})
			end_time = (numberEPulled[0])*3600 + (numberEPulled[1])*60 + numberEPulled[2]

			if end_time < 28800:
				return Response({"Please note: No public holidays. Weekdays only, from 08:00 - 17:00."})
			elif 61200 < end_time:
				return Response({"Please note: No public holidays. Weekdays only, from 08:00 - 17:00."})

			if end_time > start_time:
				timeDiff = int(end_time - start_time)
			else:
				return Response({"The End time cannot be less than the Start time. Please review and try again."})
			
			return Response({"business_seconds": timeDiff })
		except Exception as e:
			return Response({'Bad Results response': 'there was an error ' + str(e)})