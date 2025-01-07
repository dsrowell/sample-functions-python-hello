import dynamodb

def main(event, context):
    # event
    #   http
    #     headers
    #       <header>: <val>
    #     method: GET
    #     path: /
    #   <name>: <val>
    http = event['http']
    method = http['method']
    path = http['path']

    year = event['year'] if 'year' in event else None

    if year:
        db = DynamoDBManager()
        items = db.get_all_events(year)
        return {"body": {"event": event, "items": items}}
    else:
        {"body": {"error": "specify year"}}