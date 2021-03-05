import concurrent.futures
import requests
import threading
import time


thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def read_site_content(url):
    session = get_session()
    print('Send request...')
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def read_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(read_site_content, sites)


if __name__ == "__main__":

    # variable to set how many requests to be send
    n = 1000

    # JSON Placeholder website to serve as dummy API
    URLs = ['https://jsonplaceholder.typicode.com/posts'] * n

    start_time = time.time()
    read_all_sites(URLs)
    print(f"Downloaded {n} times in {round(time.time() - start_time, 2)} seconds")