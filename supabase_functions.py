#from dotenv import load_dotenv
#load_dotenv()
import os
import requests

#apikey = os.environ.get("apikey")
#Authorization = os.environ.get("Authorization")
def get_all_new_reviews_restaurant_1():
    import requests

    url = 'https://dvumniwfduptvyuudtis.supabase.co/rest/v1/restaurant_1_new_reviews?select=*'
    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2dW1uaXdmZHVwdHZ5dXVkdGlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MzEwODEyNSwiZXhwIjoxOTk4Njg0MTI1fQ.dszsSlmzF7QM9K3aksoMA7TkOntQdJqS0GvQGOjBnX0',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2dW1uaXdmZHVwdHZ5dXVkdGlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MzEwODEyNSwiZXhwIjoxOTk4Njg0MTI1fQ.dszsSlmzF7QM9K3aksoMA7TkOntQdJqS0GvQGOjBnX0'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)  # Do something with the data
    else:
        print(f'Request failed with status code {response.status_code}')
    return data

    
def get_all_reviews_restaurant_1():
    import requests

    url = 'https://dvumniwfduptvyuudtis.supabase.co/rest/v1/restaurant_1?select=*'
    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2dW1uaXdmZHVwdHZ5dXVkdGlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MzEwODEyNSwiZXhwIjoxOTk4Njg0MTI1fQ.dszsSlmzF7QM9K3aksoMA7TkOntQdJqS0GvQGOjBnX0',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2dW1uaXdmZHVwdHZ5dXVkdGlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MzEwODEyNSwiZXhwIjoxOTk4Njg0MTI1fQ.dszsSlmzF7QM9K3aksoMA7TkOntQdJqS0GvQGOjBnX0'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)  # Do something with the data
    else:
        print(f'Request failed with status code {response.status_code}')
    return data


# marche pas 
def get_all_reviews(table):
    url = 'https://dvumniwfduptvyuudtis.supabase.co/rest/v1/{table}?select=*'

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2dW1uaXdmZHVwdHZ5dXVkdGlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MzEwODEyNSwiZXhwIjoxOTk4Njg0MTI1fQ.dszsSlmzF7QM9K3aksoMA7TkOntQdJqS0GvQGOjBnX0',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2dW1uaXdmZHVwdHZ5dXVkdGlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MzEwODEyNSwiZXhwIjoxOTk4Njg0MTI1fQ.dszsSlmzF7QM9K3aksoMA7TkOntQdJqS0GvQGOjBnX0'}

    response = requests.get(url, headers=headers)
    return response.json() 

#get_all_reviews("restaurant_1")

# example #update_review('id',1, 'restaurant', 'lenotre') 
def update_review(some_column,some_column_value, other_column, other_column_value):
    
    url = f'https://dvumniwfduptvyuudtis.supabase.co/rest/v1/restaurant_1_new_reviews?{some_column}=eq.{some_column_value}'

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2dW1uaXdmZHVwdHZ5dXVkdGlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MzEwODEyNSwiZXhwIjoxOTk4Njg0MTI1fQ.dszsSlmzF7QM9K3aksoMA7TkOntQdJqS0GvQGOjBnX0',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2dW1uaXdmZHVwdHZ5dXVkdGlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MzEwODEyNSwiZXhwIjoxOTk4Njg0MTI1fQ.dszsSlmzF7QM9K3aksoMA7TkOntQdJqS0GvQGOjBnX0',
        'Content-Type': 'application/json',
        'Prefer': 'return=minimal'
    }

    data = {
        other_column : other_column_value
    }

    response = requests.patch(url, headers=headers, json=data)

    if response.status_code == 204:
        print('Review updated successfully!')
    else:
        print(f'Failed to update review. Status code: {response.status_code}')

#update_review('id',1, 'restaurant', 'bob')

def get_review(review_id):
    url = f'https://dvumniwfduptvyuudtis.supabase.co/rest/v1/reviews?id=eq.{review_id}'

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2dW1uaXdmZHVwdHZ5dXVkdGlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MzEwODEyNSwiZXhwIjoxOTk4Njg0MTI1fQ.dszsSlmzF7QM9K3aksoMA7TkOntQdJqS0GvQGOjBnX0',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2dW1uaXdmZHVwdHZ5dXVkdGlzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MzEwODEyNSwiZXhwIjoxOTk4Njg0MTI1fQ.dszsSlmzF7QM9K3aksoMA7TkOntQdJqS0GvQGOjBnX0'}

    response = requests.get(url, headers=headers)
    return response.json()

