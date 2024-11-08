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

    return {"body": {"event": event}}