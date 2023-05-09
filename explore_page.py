import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import instaloader


L = instaloader.Instaloader()

@st.cache_data
def load_data():
    # Define the list of accounts to scrape
    accounts = [
        {"category": "food", "username": "f_delhite"},
        {"category": "food", "username": "thecoachmarlow"},
        {"category": "food", "username": "londonbylora"},
        {"category": "food", "username": "non_veg_lovers"},
        {"category": "food", "username": "lekhas_feast"},
        {"category": "photography", "username": "natural_photography123_"},
        {"category": "photography", "username": "phot.ographyislife1"},
        {"category": "photography", "username": "mimimandira_clicks"},
        {"category": "photography", "username": "ija_photography"},
        {"category": "photography", "username": "colours.of.india"},
        {"category": "dance", "username": "dance_n_addiction"},
        {"category": "dance", "username": "ishpreet_dang"},
        {"category": "dance", "username": "manoletyet"},
        {"category": "dance", "username": "yashpandyachoreography"},
        {"category": "dance", "username": "sneadesai"},
        {"category": "sports", "username": "stn.daily"},
        {"category": "sports", "username": "judo.olymp_"},
        {"category": "sports", "username": "thesizeup"},
        {"category": "sports", "username": "ball__star"},
        {"category": "sports", "username": "thebsblr"}
    ]

    # Initialize an empty list to store the scraped data
    all_data = []

    # Loop through each account in the list
    for account in accounts:

        # Get the profile of the Instagram account
        profile = instaloader.Profile.from_username(L.context, account['username'])

        # Get the number of followers of the account
        num_followers = profile.followers

        # Get the number of posts of the account
        num_posts = profile.mediacount

        # Get the last 10 posts of the account and store the data in a list of dictionaries
        posts = profile.get_posts()
        posts_data = []
        for post in posts:
            if len(posts_data) >= 10:
                break
            else:
                post_data = {"Category": account['category'],
                            "Username": account['username'],
                            "Time of Posting": post.date.hour, 
                            "Number of Followers": num_followers, 
                            "Number of Posts": num_posts, 
                            "Likes": post.likes}
                posts_data.append(post_data)

        # Add the post data to the list of all data
        all_data.extend(posts_data)

    # Convert the list of data into a pandas DataFrame
    df = pd.DataFrame(all_data)
    return df

df = load_data()

def show_explore_page():
    st.title("Visualize your data")
    # Create a scatter plot of likes vs. time posted
    plt.scatter(df['Time of Posting'], df['Likes'])
    plt.xlabel('Time Posted')
    plt.ylabel('Likes')
    plt.show()
