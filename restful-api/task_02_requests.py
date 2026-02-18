#!/usr/bin/python3
import requests
import json


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


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        reponses = requests.get(url)
        reponses.raise_for_status()
        posts = reponses.json()
        with open("posts.csv", "w") as file:
            json.dump(posts, file, indent=4)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
