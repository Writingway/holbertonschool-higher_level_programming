#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    reponses = requests.get(url)
    reponses.raise_for_status()  # Check if the request was successful
    posts = reponses.json()  # Parse the JSON response
    print("Status Code: {}".format(reponses.status_code))
    for post in posts:
        print("{}".format(post['title']))


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    reponses = requests.get(url)
    reponses.raise_for_status()
    posts = reponses.json()
    structured_posts = [
        {
            'id': post.get('id'),
            'title': post.get('title'),
            'body': post.get('body')
        } for post in posts
    ]

    with open('posts.csv', mode='w') as csvfile:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(structured_posts)
