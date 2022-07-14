from pyrogram import Client
import time

api_id = int(input("API ID : "))
api_hash = str(input("API HASH : "))

app = Client("_DaMaR_", api_id, api_hash)
Nb = list(input("Name : "))
L2 = []
app.start()
print("Start")
while True:
  for name in Nb:
    try:
      L2.append(name)
      app.update_profile(first_name=''.join(L2))
      time.sleep(5)
    except Exception as e:
        print(e)
  L2 = []
app.stop()