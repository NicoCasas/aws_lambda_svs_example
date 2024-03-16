import json
import re
from scrapper import get_top_n_majors_three_pointers_nba

InvalidBodyError = {
    'statusCode': 400,
    'body': json.dumps({
        'error': 'Invalid body'
    })
}

def get_welcome_msg(event):
    # Extract the string from the request body
    if not event.get('body'):
        return  InvalidBodyError
    
    try:
        body = json.loads(event['body'])
    except:
        return InvalidBodyError
    
    if not body.get('name'):
        return InvalidBodyError
    name = body['name']
    
    # Verify if the name contains only alphabetical values
    if re.match(r'^[a-zA-Z]+$', name) is None:
        return InvalidBodyError

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
    if not event['httpMethod']:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': 'Bad Request'
            })
        }
    
    http_method = event['httpMethod']
    # Check if the request method is POST
    if http_method not in ['GET', 'POST']:
        return {
            'statusCode': 405,
            'body': json.dumps({
                'error': 'Method Not Allowed'
            })
        }
    
    if http_method == 'GET':
        return get_scorers()        
    
    if http_method == 'POST':
        return get_welcome_msg(event)
    

