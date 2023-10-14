from solutionChecker import *

# There is a secret message hidden in the file. 
# The secret message is encoded by having each character 
# occur at every X index. 
# X is a random prime number between 0 and 200
# Use the "SolutionChecker" class to check answer!


def read_file(file_path):
  # implement this function
  # takes in a file_path variable and returns the data of that file
  data = ""
  return data

def is_prime(n):
  # implement this function (helper for parse_and_check_data)
  # returns true or false if number n is prime
  pass

def parse_and_check_data(data, checker):
  # implement this function
  # parse possible secret messages from the data
  # check each secret message with the SolutionChecker class (checker.check_answer())
  # return the secret message if it is correct, return "Wrong Answer" otherwise
  pass


checker = SolutionChecker()
data = read_file("the_file_path.txt")
print(parse_and_check_data(data, checker))


