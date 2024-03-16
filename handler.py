import json
import re
from scrapper import get_top_n_majors_three_pointers_nba

def get_welcome_msg(event):
    # Extract the string from the request body
    if not event['body'] or not event['body']['name']:
        return {
            'statusCode': 400,
            'body':{
                'error': 'Invalid body'
            }
        }
    name = event['body']['name']
    
    # Verify if the name contains only alphabetical values
    if not re.match(r'^[a-zA-Z]+$', name):
        return {
            'statusCode': 400,
            'body': {
                'error': 'Invalid name. Only alphabetical values are allowed.'
            }
        }

    welcome_message = 'hola ' + name
    
    # Return the processed string as a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps({'message': welcome_message})
    }


def get_scorers():
    top_scorers = get_top_n_majors_three_pointers_nba(5)
    return {
        'statusCode': 200,
        'body': json.dumps(top_scorers)
    }


def lambda_handler(event, context):
    print(f'event -> {event}')
    
    if not event['httpMethod']:
        return {
            'statusCode': 400,
            'error': 'Bad Request'
        }
    
    http_method = event['httpMethod']
    # Check if the request method is POST
    if http_method not in ['GET', 'POST']:
        return {
            'statusCode': 405,
            'body': 'Method Not Allowed'
        }
    
    if http_method == 'GET':
        return get_scorers()        
    
    if http_method == 'POST':
        return get_welcome_msg(event)
    

