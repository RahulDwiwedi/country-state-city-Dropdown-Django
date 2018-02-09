# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector



# Create your views here.


#index page where the form and result is populated.
def index(request):
    cnx = mysql.connector.connect(user='root', password="rahul", host="localhost", database='location')
    cursor = cnx.cursor()
    query="Select name,id from countries"
    cursor.execute(query)
    country=cursor.fetchall()
    context={"country":country
        }
    cnx.close()
    return render(request,"index.html",context)

#  to populate state dropdown when country is selected. 
def state_view(request,id):
    cnx = mysql.connector.connect(user='root', password="rahul", host="localhost", database='location')
    cursor = cnx.cursor()
    query="select name,id from states where country_id="+str(id)
    cursor.execute(query)
    states=cursor.fetchall()
    context={"states":states
        }
    cnx.close()
    return render(request,"state.html",context)

#  to populate city dropdown when state is selected.
def city_view(request,id):
    cnx = mysql.connector.connect(user='root', password="rahul", host="localhost", database='location')
    cursor = cnx.cursor()
    query="select name,id from cities where state_id="+str(id)
    cursor.execute(query)
    cities=cursor.fetchall()
    if cities:
        context={"cities":cities
            }
        
    else:
        context={"cities":["",0]
        }
    cnx.close()
    return render(request,"city.html",context)
        
#  populate the Country,State,City on the Index page.
def location_view(request,conid,sid,cid):
    cnx = mysql.connector.connect(user='root', password="rahul", host="localhost", database='location')
    cursorCon = cnx.cursor()
    cursorS = cnx.cursor()
    cursorC = cnx.cursor()
    query=["select name from countries where id="+str(conid),"select name from states where id="+str(sid),"select name from cities where id="+str(cid)]
    cursorCon.execute(query[0])
    country=cursorCon.fetchone()
    cursorS.execute(query[1])
    state=cursorS.fetchone()
        
    cursorC.execute(query[2])
    city=cursorC.fetchone()
    html="Country : "+str(country[0])+"</br>State : "+str(state[0])+"</br>City : "+str(city[0])
    cnx.close()
    return HttpResponse(html)


def location_view2(request,conid,sid):
    cnx = mysql.connector.connect(user='root', password="rahul", host="localhost", database='location')
    cursorCon = cnx.cursor()
    cursorS = cnx.cursor()
    query=["select name from countries where id="+str(conid),"select name from states where id="+str(sid)]
    cursorCon.execute(query[0])
    country=cursorCon.fetchone()
    cursorS.execute(query[1])
    state=cursorS.fetchone()
    html="Country : "+str(country[0])+"</br>State : "+str(state[0])
    cnx.close()
    return HttpResponse(html) 

    
