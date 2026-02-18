#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    reponses = requests.get(url)
    print("Status Code: {}".format(reponses.status_code))

    if reponses.status_code == 200:
        posts = reponses.json()
        for post in posts:
            print("{}".format(post.get('title')))


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    reponses = requests.get(url)

    if reponses.status_code == 200:
        posts = reponses.json()
        structured_posts = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            } for post in posts
        ]

        with open('posts.csv', mode='w', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_posts)
