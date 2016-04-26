from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from collections import OrderedDict
from models import *
import json

import names
import random

import string

import geocoder

# Create your views here.

data = ''

def MSC_Clear_Codes(request):

    return render_to_response('index.html', locals())


@csrf_exempt
def login(request):
    data = json.loads(request.body)
    res = dict()
    if data['username'] == "alexey" and data["password"] == "123":
        res['login'] = "success"
    else:
        res['login'] = "failed"

    res = json.dumps(res)

    return HttpResponse(res)


def users(request):
    data = getRandomData()

    res = json.dumps(data)

    return HttpResponse(res)



def reports(request):
    data = getRandomData()
    res = dict()

    # get lead score info for pie chart
    lead_score = {'1-10': 0, '11-20': 0, '21-30': 0, '31-40': 0, '41-50': 0, '51-60': 0, '61-70': 0, '71-80': 0, '81-90': 0, '91-100': 0, }
    for element in data:
        if element['lead_score'] > 0 and element['lead_score'] <= 10:
            lead_score['1-10'] += 1
        elif element['lead_score'] <= 20:
            lead_score['11-20'] += 1
        elif element['lead_score'] <= 30:
            lead_score['21-30'] += 1
        elif element['lead_score'] <= 40:
            lead_score['31-40'] += 1
        elif element['lead_score'] <= 50:
            lead_score['41-50'] += 1
        elif element['lead_score'] <= 60:
            lead_score['51-60'] += 1
        elif element['lead_score'] <= 70:
            lead_score['61-70'] += 1
        elif element['lead_score'] <= 80:
            lead_score['71-80'] += 1
        elif element['lead_score'] <= 90:
            lead_score['81-90'] += 1
        elif element['lead_score'] <= 100:
            lead_score['91-100'] += 1


    res['lead_score'] = lead_score

    # get aggregated data by geo city
    temp = dict()
    for element in data:
        if element['found_postal']['city'] in temp.keys():
            temp[element['found_postal']['city']] +=1
        else:
            temp[element['found_postal']['city']] = 0

    res['geo_city'] = OrderedDict(sorted(temp.items(), key=lambda t: t[1], reverse=True))
    print res['geo_city']
    # get aggregated data by salary
    temp = dict()
    for element in data:
        if element['salary'] in temp.keys():
            temp[element['salary']] +=1
        else:
            temp[element['salary']] = 0

    res['salary'] = OrderedDict(sorted(temp.items(), key=lambda t: t[1], reverse=True))


    # get aggregated data by interest
    temp = dict()
    for element in data:
        if element['interests'] in temp.keys():
            temp[element['interests']] +=1
        else:
            temp[element['interests']] = 0
    res['interests'] = OrderedDict(sorted(temp.items(), key=lambda t: t[1], reverse=True))

    # get aggregated data by home_owner_status
    temp = dict()
    for element in data:
        if element['demographics']['home_owner_status'] in temp.keys():
            temp[element['demographics']['home_owner_status']] +=1
        else:
            temp[element['demographics']['home_owner_status']] = 0
    res['home_owner_status'] = OrderedDict(sorted(temp.items(), key=lambda t: t[1], reverse=True))

    # get aggregated data by education
    temp = dict()
    for element in data:
        if element['education'] in temp.keys():
            temp[element['education']] +=1
        else:
            temp[element['education']] = 0
    res['education'] = OrderedDict(sorted(temp.items(), key=lambda t: t[1], reverse=True))

    # get aggregated data by occupation
    temp = dict()
    for element in data:
        if element['demographics']['occupation'] in temp.keys():
            temp[element['demographics']['occupation']] +=1
        else:
            temp[element['demographics']['occupation']] = 0
    res['occupation'] = OrderedDict(sorted(temp.items(), key=lambda t: t[1], reverse=True))

     # get aggregated data by date
    temp = dict()
    for element in data:
        if element['time_subscribed'] in temp.keys():
            temp[element['time_subscribed']] +=1
        else:
            temp[element['time_subscribed']] = 0
    res['time_subscribed'] = temp

    res = json.dumps(res)
    return HttpResponse(res)

def getRandomStr(size):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))



def getRandomData():
    res = []
    gender = ['Male', 'Female']
    location = ['USA', 'Canada', 'Austria', 'France', 'Italy']
    state = ['AL', 'AK', 'CA', 'CO', 'GA', 'HI', 'IL']
    city = ['Montgomery', '	Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover']
    interests = ['Sports', 'Music', 'Art', 'Study', 'Teach']
    home_owner_status = ['Owner', 'Rent']
    education = ['University', 'College', 'Middle School']
    occupation = ['Professional', 'Architect', 'Auditor', 'Cabinet Maker', 'Care Taker', 'Composer', 'Electrician', 'Historian']
    salary = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    date = ['2016-1-2 00:00:00', '2016-1-3 00:00:00', '2016-1-4 00:00:00', '2016-1-12 00:00:00', '2016-1-10 00:00:00', '2016-1-15 00:00:00']
    for i in range(0, 100):
        data = {
            'full_name': names.get_full_name(),
            'phone_number': str(random.randrange(11111111111, 99999999999)),
            'email': "%s@%s.com" % (getRandomStr(5), getRandomStr(3)),
            'location': random.choice(location),
            'time_subscribed': random.choice(date),
            'link_to_google_maps_location': 'https://maps.google.com/',
            'lead_score': random.randint(1, 100),
            'interests': random.choice(interests),
            'education': random.choice(education),
            'salary': '$%d' % random.choice(salary),
            "demographics":{
                "age": random.randint(10, 80),
                "gender": random.choice(gender),
                "occupation": random.choice(occupation),
                "children": "No",
                "household_income": "75k-100k",
                "marital_status": "Single",
                "home_owner_status":  random.choice(home_owner_status),
                "velocity": "7",
            },
            "found_postal": {
                "address1": "100 MAIN ST APT 3",
                "address2": '',
                "city": random.choice(city),
                "state": random.choice(state),
                "zip": "%d" % random.randint(11111, 99999),
            },
        }

        res.append(data)
    return res

