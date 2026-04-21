import requests as probe
victim = input()
while True:
  stats=probe.get(victim)
  print(stats.status_code)  
