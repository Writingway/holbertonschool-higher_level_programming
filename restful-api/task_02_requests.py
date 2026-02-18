#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        reponses = requests.get(url)
        reponses.raise_for_status()  # Check if the request was successful
        posts = reponses.json()  # Parse the JSON response
        print("Status Code: {}".format(reponses.status_code))
        for post in posts:
            print("{}".format(post['title']))
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# if the request was sucessfull, instead of printing titles,
# structure the data into a list of dictionaries, where each dictionary
# represents a post with keys and values for id, title, and body.
# Using Python's csv module, write this data into a CSV file called posts.csv
# with columns corresponding to the dictionary keys.
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        reponses = requests.get(url)
        reponses.raise_for_status()  # Check if the request was successful
        posts = reponses.json()  # Parse the JSON response
        structured_posts = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        with open('posts.csv', mode='w') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerows(structured_posts)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
