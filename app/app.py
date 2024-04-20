import fire

def aloha(name="Damon"):
  return "Aloha %s!" % name

if __name__ == '__main__':
  fire.Fire(aloha)
