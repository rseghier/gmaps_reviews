# rajouter get status pour initialiser le choix du radio button
# for login  "pip install streamlit-authenticator==0.1.5"
import pickle #new
from pathlib import Path #new
import streamlit_authenticator as stauth #new

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from supabase_functions import get_all_reviews, update_review, get_review

## USER AUTHENTICATION
names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)
    
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Incorrect username or password!")
if authentication_status == None:
    st.warning("Please login to access the dashboard!")

if authentication_status:
    
    authenticator.logout("Logout","sidebar")
    st.sidebar.title(f"Welcome {name}!")

    # create a sidebar with links to page 1 and page 2
    st.sidebar.title('📊  🍽️  🍔  🍕  🍣  👨‍🍳  📈')
    st.sidebar.title('RESTAURANT REVIEW APP')

    page = st.sidebar.radio('Navigation', ['Latests Reviews and Statistics', 'New Review Confirmation'])

    if page == 'Latests Reviews and Statistics':
        
        # GRAPHIQUE
        
        # calculation is wrong 
        import streamlit as st
        import pandas as pd
        import plotly.express as px
        
        st.header("Latests Reviews and Statistics")
        #st.write('')
        
        st.metric(label="# Reviews of the week", value="9", delta="12%")

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


        reviews = get_all_reviews_restaurant_1()
        df = pd.DataFrame(reviews)

        # add a column numberReviews that counts the number of rows starting from botton to top
        df = df.assign(numberReviews = df.shape[0] - df.index.values)

        df['review_date'] = pd.to_datetime(df['review_date'])
        df_weekly = df.groupby(pd.Grouper(key='review_date', freq='W-MON'))['numberReviews'].sum().reset_index()

        fig = px.bar(df_weekly, x='review_date', y='numberReviews') #title='Number of Reviews per Week'

        st.plotly_chart(fig)
    
    if page == 'New Review Confirmation':
        
        # CREATION OF NEW REVIEW TEXT BOXES
        
        from supabase_functions import get_all_new_reviews_restaurant_1
    
        st.header("New Review Confirmation")
        st.write('Please confirm these reviews before publication')
        
        reviews = get_all_new_reviews_restaurant_1()
        
        for i in range(len(reviews)):
            review_text = reviews[i]['review_text']
            text_area = st.text_area("Review Text", value=review_text, height=200, max_chars=100*10)

            if "visibility" not in st.session_state: # Store the initial value of widgets in session state
                st.session_state.visibility = "Pending"

            visibility_radio = st.radio(
                "Set review status 👉",
                key=f"visibility_{i}",
                options=["Pending", "Update", "Cancel"])

            # Call the appropriate function based on the selected option
            if visibility_radio == "Pending":
                update_review('id',i+1, 'review_status', "Pending") 
                st.write("Pending")
            elif visibility_radio == "Update":
                update_review('id',i+1, 'review_text', text_area) 
                update_review('id',i+1, 'review_status', "Updated") 
                st.write("Updated")
            else:
                update_review('id',i+1, 'review_status', "Cancelled") 
                st.write("Cancelled")

            