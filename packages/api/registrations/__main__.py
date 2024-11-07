from util import add
from dynamodb import DynamoDBManager

def main(args):
    #name = args.get("name", "stranger")
    #sum = add(2, 2)
    #greeting = "Hello " + name + "! 2 + 2 = " + str(sum)
    #print(greeting)
    #return {"body": greeting}
    regs = "initial"
    try:
        db = DynamoDBManager()
        regs = 'calling'
        regs = db.get_registration_by_id('gLqZ3CKErWL')
        if regs is None:
            regs = 'no registrations found'
    except Exception as e:
        regs = f'exception: {str(e)}'
    return {"body": {"registrations": regs}}