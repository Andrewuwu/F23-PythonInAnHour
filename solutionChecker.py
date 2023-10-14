import hashlib
import os

class SolutionChecker:
  def __init__(self):
    self.secret1 = os.environ['ANSWER']

  def check_answer(self, answer):
    sha1 = hashlib.sha1()
    sha1.update(answer.encode())
    hash_val = sha1.hexdigest()
    return hash_val == self.secret1

  def give_hint(self):
    print("No")