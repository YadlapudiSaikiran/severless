def lambda_handler(event, context):
    try:
        num1 = float(event['num1'])
        num2 = float(event['num2'])
        result = num1 + num2
        return {
            'statusCode': 200,
            'body': f'The sum of {num1} and {num2} is {result}.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
