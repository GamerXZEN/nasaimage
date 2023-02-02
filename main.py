import requests
import streamlit as sl

url = "https://api.nasa.gov/planetary/apod?api_key=B2zzDLYTXsuxcshu79HVxAfTdqUOs2BeRHwUvs5r"

request = requests.get(url)
data = request.json()

title = data["title"]
date = data["date"]
description = data["explanation"]
image = requests.get(data["hdurl"])

with open("image.png", "wb") as file:
	file.write(image.content)

sl.set_page_config(layout="wide")

sl.image("image.png")
sl.title(f"{title}")
sl.write(f"Date: {date}")
sl.info(f"{description}")
