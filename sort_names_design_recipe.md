# sort_names Route Design Recipe


## 1. Design the Route Signature

```
# EXAMPLE

# Request:
GET /names?add=Eddie

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie

'''
curl http://localhost:5000/add_names?names=Julia&names=Alice&names=Karim&names=Eddie
'''
-------------------------------------
Extra Challenge

# Request:
GET /names?add=Eddie,Leo

# Expected response (2OO OK):
Alice, Eddie, Julia, Karim, Leo

# Sort names in alphabetical order

'''
curl http://localhost:5000/sort_names?names=Julia&names=Alice&names=Karim&names=KieranEddie&names=Leo
'''

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# Route: /add_names
# Parameters: Julia, Alice, Karim
# Expected response (200 OK):
"""
Julia, Alice, Karim
"""

# Route: /add_names
# Parameters: Eddie
# Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie
"""

# Route: /add_names
# Parameters: ' '
# Expected response (400 BAD REQUEST):
"""
'Please add names to the list'
"""

# Route: /sort_names
# Parameters: Eddie, Leo
# Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie, Leo
"""

# Route: /sort_names
# Parameters: Julia, Alice, Karim, Eddie, Leo
# Alphabetise the names
# Expected response (200 OK):
"""
Alice,Eddie,Julia,Karim,Leo
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```

