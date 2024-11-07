from util import add
from dynamodb import DynamoDBManager
def main(args):
    #name = args.get("name", "stranger")
    #sum = add(2, 2)
    #greeting = "Hello " + name + "! 2 + 2 = " + str(sum)
    #print(greeting)
    #return {"body": greeting}
    try:
        db = DynamoDBManager()
        regs = db.get_all_registrations()
    except Exception as e:
        regs = e
    return {"body": {"registrations": regs}}