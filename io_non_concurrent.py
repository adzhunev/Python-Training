import requests
import time


def read_site_content(url, session):
    print('Send request...')
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def read_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            read_site_content(url, session)


if __name__ == "__main__":

    # variable to set how many requests to be send
    n = 1000

    # JSON Placeholder website to serve as dummy API
    URLs = ['https://jsonplaceholder.typicode.com/posts'] * n

    start_time = time.time()
    read_all_sites(URLs)
    print(f"Downloaded {n} times in {round(time.time() - start_time, 2)} seconds")