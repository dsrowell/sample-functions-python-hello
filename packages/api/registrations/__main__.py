from util import add
def main(args):
      name = args.get("name", "stranger")
      sum = add(2, 2)
      greeting = "Hello " + name + "! 2 + 2 = " + str(sum)
      print(greeting)
      return {"body": greeting}