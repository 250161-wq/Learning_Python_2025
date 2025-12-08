"""
Module: Working with APIs in Python
Description: Comprehensive guide to making API requests with Python

This module covers:
- HTTP basics (GET, POST, PUT, DELETE)
- Using the requests library
- Handling responses
- Query parameters and headers
- Authentication
- Error handling
- Best practices

Note: This module uses public APIs that don't require authentication.
Some examples may fail if the API is down or rate-limited.
"""

import requests
import json
from datetime import datetime


def demonstrate_get_request():
    """
    Demonstrates making GET requests to retrieve data from APIs.
    
    GET is used to retrieve data from a server.
    """
    print("=== GET Requests ===")
    
    # Simple GET request
    print("Fetching a joke from API:")
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        
        # Check if request was successful
        if response.status_code == 200:
            joke = response.json()
            print(f"  Setup: {joke['setup']}")
            print(f"  Punchline: {joke['punchline']}")
        else:
            print(f"  Error: Status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"  Request failed: {e}")
    
    print()


def demonstrate_response_handling():
    """
    Demonstrates different ways to handle API responses.
    """
    print("=== Response Handling ===")
    
    try:
        url = "https://jsonplaceholder.typicode.com/posts/1"
        response = requests.get(url)
        
        # Status code
        print(f"Status Code: {response.status_code}")
        print(f"OK: {response.ok}")
        
        # Headers
        print(f"\nContent-Type: {response.headers.get('Content-Type')}")
        
        # Response body in different formats
        print("\nResponse as text (first 100 chars):")
        print(f"  {response.text[:100]}...")
        
        print("\nResponse as JSON:")
        data = response.json()
        print(f"  Title: {data['title']}")
        print(f"  Body: {data['body'][:50]}...")
        
        # Raw bytes
        print(f"\nResponse as bytes (length): {len(response.content)}")
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    
    print()


def demonstrate_query_parameters():
    """
    Demonstrates using query parameters in requests.
    
    Query parameters are used to filter or customize API responses.
    """
    print("=== Query Parameters ===")
    
    try:
        # Using params parameter
        base_url = "https://jsonplaceholder.typicode.com/comments"
        params = {
            "postId": 1,
            "_limit": 3
        }
        
        response = requests.get(base_url, params=params)
        
        if response.ok:
            comments = response.json()
            print(f"Fetched {len(comments)} comments:")
            for comment in comments:
                print(f"  - {comment['email']}: {comment['body'][:40]}...")
        
        # URL with query params
        print(f"\nFull URL: {response.url}")
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    
    print()


def demonstrate_headers():
    """
    Demonstrates using custom headers in requests.
    
    Headers provide metadata about the request.
    """
    print("=== Custom Headers ===")
    
    try:
        url = "https://jsonplaceholder.typicode.com/posts/1"
        
        # Custom headers
        headers = {
            "User-Agent": "Python Learning App 1.0",
            "Accept": "application/json"
        }
        
        response = requests.get(url, headers=headers)
        
        if response.ok:
            print("Request successful with custom headers")
            print(f"  User-Agent sent: {headers['User-Agent']}")
            data = response.json()
            print(f"  Received post: {data['title']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    
    print()


def demonstrate_post_request():
    """
    Demonstrates making POST requests to send data to APIs.
    
    POST is used to create new resources on the server.
    """
    print("=== POST Requests ===")
    
    try:
        url = "https://jsonplaceholder.typicode.com/posts"
        
        # Data to send
        new_post = {
            "title": "Learning Python APIs",
            "body": "This is a test post about API interactions",
            "userId": 1
        }
        
        # Send POST request
        response = requests.post(url, json=new_post)
        
        if response.status_code == 201:  # 201 = Created
            created = response.json()
            print("Post created successfully!")
            print(f"  ID: {created['id']}")
            print(f"  Title: {created['title']}")
        else:
            print(f"  Error: Status code {response.status_code}")
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    
    print()


def demonstrate_put_request():
    """
    Demonstrates making PUT requests to update data.
    
    PUT is used to update existing resources.
    """
    print("=== PUT Requests ===")
    
    try:
        url = "https://jsonplaceholder.typicode.com/posts/1"
        
        # Updated data
        updated_post = {
            "id": 1,
            "title": "Updated Title",
            "body": "Updated body content",
            "userId": 1
        }
        
        # Send PUT request
        response = requests.put(url, json=updated_post)
        
        if response.ok:
            updated = response.json()
            print("Post updated successfully!")
            print(f"  Title: {updated['title']}")
            print(f"  Body: {updated['body']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    
    print()


def demonstrate_delete_request():
    """
    Demonstrates making DELETE requests.
    
    DELETE is used to remove resources.
    """
    print("=== DELETE Requests ===")
    
    try:
        url = "https://jsonplaceholder.typicode.com/posts/1"
        
        # Send DELETE request
        response = requests.delete(url)
        
        if response.ok:
            print("Post deleted successfully!")
            print(f"  Status code: {response.status_code}")
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    
    print()


def demonstrate_error_handling():
    """
    Demonstrates proper error handling for API requests.
    """
    print("=== Error Handling ===")
    
    # Timeout error
    print("Handling timeout:")
    try:
        response = requests.get("https://httpbin.org/delay/10", timeout=2)
    except requests.exceptions.Timeout:
        print("  Request timed out!")
    
    # Connection error
    print("\nHandling connection error:")
    try:
        response = requests.get("https://this-site-does-not-exist-12345.com")
    except requests.exceptions.ConnectionError:
        print("  Connection failed!")
    
    # HTTP error (4xx, 5xx)
    print("\nHandling HTTP errors:")
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/999999")
        response.raise_for_status()  # Raises HTTPError for bad status codes
        print("  Request successful")
    except requests.exceptions.HTTPError as e:
        print(f"  HTTP error occurred: {e}")
    
    # Generic exception
    print("\nGeneric exception handling:")
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        response.raise_for_status()
        data = response.json()
        print(f"  Success: {data['title']}")
    except requests.exceptions.RequestException as e:
        print(f"  Request failed: {e}")
    
    print()


def demonstrate_session():
    """
    Demonstrates using sessions for persistent connections.
    
    Sessions maintain cookies and connection pooling across requests.
    """
    print("=== Using Sessions ===")
    
    try:
        # Create a session
        with requests.Session() as session:
            # Set default headers for all requests
            session.headers.update({"User-Agent": "Python Learning App"})
            
            # Make multiple requests
            urls = [
                "https://jsonplaceholder.typicode.com/posts/1",
                "https://jsonplaceholder.typicode.com/posts/2",
                "https://jsonplaceholder.typicode.com/posts/3"
            ]
            
            for url in urls:
                response = session.get(url)
                if response.ok:
                    data = response.json()
                    print(f"  Post {data['id']}: {data['title'][:40]}...")
        
        print("Session closed automatically")
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    
    print()


def demonstrate_rate_limiting():
    """
    Demonstrates implementing rate limiting for API requests.
    """
    print("=== Rate Limiting ===")
    
    import time
    
    print("Making 5 requests with 1-second delay:")
    for i in range(1, 6):
        try:
            response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{i}")
            if response.ok:
                data = response.json()
                print(f"  {i}. {data['title'][:40]}...")
            time.sleep(1)  # Wait 1 second between requests
        except requests.exceptions.RequestException as e:
            print(f"  Request {i} failed: {e}")
    
    print()


# EXERCISES
def exercise_1():
    """
    Exercise 1: Weather Data Fetcher (Simulated)
    
    TODO: Create a function that fetches data from an API and:
    - Extracts specific information
    - Handles errors gracefully
    - Returns structured data
    """
    print("=== Exercise 1: API Data Fetcher ===")
    
    def fetch_user_data(user_id):
        """Fetches user data from JSONPlaceholder API."""
        try:
            url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            
            user = response.json()
            return {
                "name": user["name"],
                "email": user["email"],
                "city": user["address"]["city"],
                "company": user["company"]["name"]
            }
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    # Test the function
    for user_id in [1, 2, 3]:
        result = fetch_user_data(user_id)
        if "error" in result:
            print(f"  User {user_id}: Error - {result['error']}")
        else:
            print(f"  User {user_id}: {result['name']} ({result['email']})")
            print(f"    City: {result['city']}, Company: {result['company']}")
    
    print()


def exercise_2():
    """
    Exercise 2: Bulk Data Fetcher
    
    TODO: Fetch multiple posts and:
    - Get posts from multiple pages
    - Combine results
    - Count total words in all posts
    """
    print("=== Exercise 2: Bulk Data Fetcher ===")
    
    def fetch_posts(limit=5):
        """Fetches multiple posts from API."""
        try:
            url = "https://jsonplaceholder.typicode.com/posts"
            params = {"_limit": limit}
            
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            
            posts = response.json()
            
            # Calculate statistics
            total_posts = len(posts)
            total_words = sum(len(post["body"].split()) for post in posts)
            
            return {
                "total_posts": total_posts,
                "total_words": total_words,
                "posts": posts
            }
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    result = fetch_posts(10)
    if "error" in result:
        print(f"  Error: {result['error']}")
    else:
        print(f"  Fetched {result['total_posts']} posts")
        print(f"  Total words: {result['total_words']}")
        print(f"  Average words per post: {result['total_words'] / result['total_posts']:.1f}")
    
    print()


def exercise_3():
    """
    Exercise 3: API Client Class
    
    TODO: Create a class that wraps API interactions:
    - Initialize with base URL
    - Methods for GET, POST
    - Automatic error handling
    - Logging
    """
    print("=== Exercise 3: API Client Class ===")
    
    class APIClient:
        """Simple API client wrapper."""
        
        def __init__(self, base_url):
            self.base_url = base_url
            self.session = requests.Session()
        
        def get(self, endpoint, **kwargs):
            """Makes a GET request."""
            url = f"{self.base_url}/{endpoint}"
            try:
                response = self.session.get(url, timeout=5, **kwargs)
                response.raise_for_status()
                print(f"  GET {endpoint}: Success")
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"  GET {endpoint}: Error - {e}")
                return None
        
        def post(self, endpoint, data=None, **kwargs):
            """Makes a POST request."""
            url = f"{self.base_url}/{endpoint}"
            try:
                response = self.session.post(url, json=data, timeout=5, **kwargs)
                response.raise_for_status()
                print(f"  POST {endpoint}: Success")
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"  POST {endpoint}: Error - {e}")
                return None
    
    # Test the client
    client = APIClient("https://jsonplaceholder.typicode.com")
    
    # GET request
    post = client.get("posts/1")
    if post:
        print(f"    Title: {post['title']}")
    
    # POST request
    new_post = {"title": "Test", "body": "Content", "userId": 1}
    created = client.post("posts", data=new_post)
    if created:
        print(f"    Created post ID: {created['id']}")
    
    print()


def exercise_4():
    """
    Exercise 4: Data Aggregator
    
    TODO: Fetch data from multiple endpoints and aggregate:
    - Get all posts by a user
    - Get all comments on those posts
    - Create summary statistics
    """
    print("=== Exercise 4: Data Aggregator ===")
    
    def get_user_activity(user_id):
        """Gets all activity for a user."""
        try:
            # Get user's posts
            posts_url = f"https://jsonplaceholder.typicode.com/posts"
            posts_response = requests.get(posts_url, params={"userId": user_id}, timeout=5)
            posts_response.raise_for_status()
            posts = posts_response.json()
            
            # Get comments for first post
            if posts:
                comments_url = f"https://jsonplaceholder.typicode.com/comments"
                comments_response = requests.get(
                    comments_url, 
                    params={"postId": posts[0]["id"]}, 
                    timeout=5
                )
                comments_response.raise_for_status()
                comments = comments_response.json()
            else:
                comments = []
            
            return {
                "user_id": user_id,
                "posts_count": len(posts),
                "first_post_title": posts[0]["title"] if posts else "N/A",
                "first_post_comments": len(comments)
            }
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    result = get_user_activity(1)
    if "error" in result:
        print(f"  Error: {result['error']}")
    else:
        print(f"  User ID: {result['user_id']}")
        print(f"  Total posts: {result['posts_count']}")
        print(f"  First post: {result['first_post_title']}")
        print(f"  Comments on first post: {result['first_post_comments']}")
    
    print()


def exercise_5():
    """
    Exercise 5: Response Caching
    
    TODO: Implement simple caching to avoid repeated API calls:
    - Cache responses for a certain time
    - Check cache before making requests
    - Save bandwidth and improve speed
    """
    print("=== Exercise 5: Response Caching ===")
    
    class CachedAPI:
        """API client with simple caching."""
        
        def __init__(self):
            self.cache = {}
            self.cache_duration = 60  # seconds
        
        def get(self, url):
            """Gets data with caching."""
            current_time = datetime.now().timestamp()
            
            # Check cache
            if url in self.cache:
                cached_data, cached_time = self.cache[url]
                if current_time - cached_time < self.cache_duration:
                    print(f"  Cache HIT: {url}")
                    return cached_data
            
            # Make request
            print(f"  Cache MISS: {url}")
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                data = response.json()
                
                # Store in cache
                self.cache[url] = (data, current_time)
                return data
            except requests.exceptions.RequestException as e:
                print(f"  Error: {e}")
                return None
    
    # Test caching
    api = CachedAPI()
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    # First call - cache miss
    data1 = api.get(url)
    if data1:
        print(f"    Title: {data1['title'][:30]}...")
    
    # Second call - cache hit
    data2 = api.get(url)
    if data2:
        print(f"    Title: {data2['title'][:30]}...")
    
    print()


if __name__ == "__main__":
    """
    Main execution block - runs all demonstrations and exercises.
    """
    print("=" * 60)
    print("WORKING WITH APIs IN PYTHON - COMPLETE GUIDE")
    print("=" * 60)
    print()
    
    print("Note: Some examples use public APIs and may fail if")
    print("the API is down, rate-limited, or network is unavailable.")
    print()
    
    # Run all demonstrations
    demonstrate_get_request()
    demonstrate_response_handling()
    demonstrate_query_parameters()
    demonstrate_headers()
    demonstrate_post_request()
    demonstrate_put_request()
    demonstrate_delete_request()
    demonstrate_error_handling()
    demonstrate_session()
    demonstrate_rate_limiting()
    
    # Run all exercises
    print("=" * 60)
    print("EXERCISES")
    print("=" * 60)
    print()
    
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    
    print("=" * 60)
    print("END OF WORKING WITH APIs MODULE")
    print("=" * 60)
