from util import add
from dynamodb import DynamoDBManager

def main(args):
    http = args['http']
    method = http['method']
    path = http['path'].strip('/')
    parts = path.split('/')

    db = DynamoDBManager()

    eventid = args['eventid'] if 'eventid' in args else None

    if method == 'GET':
        if len(parts) == 0:
            if eventid is not None:
                eventid = args['eventid']
                #return {'body': {'registrations': db.get_all_registrations(eventid)}}
                return {'body': {'registrations': f'get registrations for {eventid}'}}
            else:
                return {'body': {'error': 'you need to supply eventid'}}
        elif len(parts) == 1:
            #return {'body': {'parts': parts}}
            regs = db.get_registration_by_id(parts[0])
            return {'body': {'registrations': regs}}

    return {'body': {'message': 'end of main'}}