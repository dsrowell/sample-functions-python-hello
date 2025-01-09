from dynamodb import DynamoDBManager

def main(event, context):
    # event
    #   http
    #     headers
    #       <header>: <val>
    #     method: GET
    #     path: /
    #   <name>: <val>
    #http = event['http']
    #method = http['method']
    #path = http['path']

    print(f'event: {event}')
    year = event['year'] if 'year' in event else None
    print(f'year: {year}')

    #return {"body": {"event": event}}

    if year:
        print('creating manager')
        db = DynamoDBManager()
        items = db.get_all_events(year)
        return {"body": {"event": event, "items": items}}
    else:
        return {"body": {"error": "specify year"}}