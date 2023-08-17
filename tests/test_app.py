



# When I add one name Route: /add_names?name=Eddie
# Parameters: Julia, Alice, Karim
# Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie
"""
def test_get_one_name_added(web_client):
    response = web_client.get('/names', query_string={'names': 'Julia,Alice,Karim'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia,Alice,Karim,Eddie'

# When I add an empty string Route: /add_names
# Parameters: ' '
# Expected response (404 NOT FOUND):
"""
'Please add names to the list'
"""
def test_get_empty_string_added(web_client):
    response = web_client.get('/names', query_string={'names': ''})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Please add a name'

# When I add nothing to the  Route: /add_names
# Parameters: None
# Expected response (200 OK):
"""
Julia, Alice, Karim
"""
def test_get_nothing_added(web_client):
    response = web_client.get('/names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Please add a name'

# When I add two names Route: /add_names
# Parameters: Eddie, Leo
# Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie, Leo
"""
def test_get_multiple_names_added(web_client):
    response = web_client.get('/add_multiple_names', query_string={'names': 'Julia,Alice,Karim'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia,Alice,Karim,Eddie,Leo'

# When I alphabetise the names Route: /sort_names
# Parameters: Julia,Alice,Karim,Eddie,Leo
# Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie, Leo
"""
def test_get_alphabetise_names(web_client):
    response = web_client.get('/alphabetise_names', query_string={'names': 'Julia,Alice,Karim,Eddie,Leo'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Eddie,Julia,Karim,Leo'


