import json
import re
from scrapper import get_top_n_majors_three_pointers_nba

def get_welcome_msg(event):
    # Extract the string from the request body
    name = event['body']
    
    # Verify if the name contains only alphabetical values
    if not re.match(r'^[a-zA-Z]+$', name):
        return {
            'statusCode': 400,
            'body': 'Invalid name. Only alphabetical values are allowed.'
        }

    welcome_message = 'hola ' + name
    
    # Return the processed string as a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps({'message': welcome_message})
    }


def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    # Check if the request method is POST
    if http_method not in ['GET', 'POST']:
        return {
            'statusCode': 405,
            'body': 'Method Not Allowed'
        }
    
    if http_method == 'GET':
        return get_top_n_majors_three_pointers_nba(5)
    
    if http_method == 'POST':
        return get_welcome_msg(event)
    

