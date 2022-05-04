# api.py module
"""A program to read realy time weather data from internet and to provide this data to local clients
"""

from fastapi import FastAPI, Path, HTTPException, status, Request
from typing import Optional
from pydantic import BaseModel
from weather_api import get_weather
from datetime import datetime
import os

cities = []


class City(BaseModel):
    """City class to create city object."""
    name: str
    state: Optional[str] = None
    temperature: Optional[float] = None
    date_time = datetime.utcnow()

class CityUpdate(BaseModel):
    """Not in use rigth now."""
    name: str
    state: Optional[str] = None
    temperature: Optional[float] = None

def init():
    pass

cities = []
app = FastAPI()
init()
key = os.urandom(24)


@app.get("/")
def home_page():
    """Return all cities in database"""
    if cities:
        return cities
    return {"message": "Please add cities first"}

@app.post("/add-city")
def add_city(city: City):
    """Record a city and last data to database"""
    for c in cities: 
        if c.name == city.name.capitalize():
            return {"message": "City already in database!"}
    weather = get_weather(city.name)
    if not weather:
        return {"message": "No city found with that name!"}
    city.name = city.name.capitalize()
    city.state = weather["state"]
    city.temperature = weather["temp"]
    city.date_time = datetime.utcnow()
    cities.append(city)
    return city

@app.delete("/delete-city/{name}")
def delete_city(name: str):
    """Delete a city from database"""
    for c in cities: 
        if c.name == name.capitalize():
            cities.remove(c)
            return {"message": f"{name.capitalize()} deleted from database!"}
    return {"message": "No city found with that name!"}

@app.put("/update-city/{name}")
def update_city(name: str):
    """Update a city data and record to database"""
    for c in cities: 
        if c.name == name.capitalize():
            weather = get_weather(name.capitalize())
            if not weather:
                return {"message": "An unknown error occured!"}
            c.state = weather["state"]
            c.temperature = weather["temp"]
            c.date_time = datetime.utcnow()
    return {"message": "No city found with that name!"}
