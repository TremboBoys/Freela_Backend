import requests
import cloudinary, cloudinary.api
from django.shortcuts import redirect

cloudinary.config(
    cloud_name="dm2odcrnf",
    api_key="392291948516824",
    api_secret="8L8ApfYnDq6_YiXSd4lAgDmZGnI"   
)

resources = cloudinary.api.resource(public_id="db3a0fae-0ee7-4e93-b7ed-c1b3684e4495")
print(resources)
