def myFunc():
  print("Hello world")
  

# if this code is directly executed by running the file its present in
if __name__ == __main__:
  print("We're directly running this code")
  myFunc()
  print(__name__)