import os
from flask import Flask, request
#import sys

# Create a new Flask app
app = Flask(__name__)


# Route 1:
# /add_names
# Route 2:
# /sort_names

# Parameters:
# names = list of names in string format


@app.route('/names', methods=['GET'])
def get_add_name():
    static_name = 'Eddie'
    if request.args.get('names') in [None, '']:
        return 'Please add a name'
    else:
        names = request.args.get('names')
        names += ',' + static_name
        return names


@app.route('/add_multiple_names', methods=['GET'])
def get_multiple_names_added():
    static_name = 'Eddie,Leo'
    if request.args.get('names') in [None, '']:
        return 'Please add a name'
    else:
        names = request.args.get('names')
        names += ',' + static_name
        return names

@app.route('/alphabetise_names', methods=['GET'])
def get_alphabetise_names():
    names_from_request = request.args.get('names') 
    list_of_names = names_from_request.split(',')
    list_of_names.sort()
    # another way to sort where a new list is formed
    # sorted_list = sorted(list_of_names)
    joined_list_of_names = ','.join(list_of_names)
    return joined_list_of_names










    # name = 'Eddie'
    # name_added = names + ',' + name
    # print('added_name', file=sys.stderr)
    # print(name_added, file=sys.stderr)
    # return added_name








# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
