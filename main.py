from modules.live_listening import LiveListening as Listen

def trigger(trigger=False):
    if trigger == True:
      print("Triggered")

l = Listen(model_path="MODEL_PATH")
l.start("hello world", trigger)
