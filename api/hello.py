def handler(request):
    """Simple test handler to verify Vercel Functions work"""
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': '{"message": "Hello from Vercel Python Function!"}'
    }
