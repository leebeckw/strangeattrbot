import matplotlib.pyplot as plt
import tweepy
import os
import attractor
from dotenv import load_dotenv

# load constants from .env file
load_dotenv()

# twitter api keys
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
KEY = os.getenv("KEY")
SECRET = os.getenv("SECRET")

# absolute path for cron
PATH = os.getenv("ABS_PATH")

# create and save a plot
def plot(points, s, ms = 0.05):
    metadata = {"Title": s}
    x,y = [p[0] for p in points], [p[1] for p in points]
    fig, ax = plt.subplots()
    ax.plot(x,y,'k+', markersize = ms)
    ax.set_axis_off()
    fig.savefig(PATH, dpi=300, metadata=metadata)

# if string is given, save plot of that string
# otherwise find a chaotic string and save plot
def go(s = None):
    while s == None:
        s = attractor.generateAttractor()
        
    out = attractor.generatePoints(s)
    
    plot(out, s)

    return s

# tweeting infrastructure
def main():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(KEY, SECRET)

    api = tweepy.API(auth)
    
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    try:
        tweet = go()
        media = api.media_upload(PATH)
        api.update_status(status=tweet, media_ids=[media.media_id])
        print("tweeted", tweet)
    except:
        pass

# main()

# cool attractors ;)
# VGDJVHLHQKDP
# GAUVHRWSVXEO
# PLQFERMYONKM
# NEKBSTRRCHPP
# FPOUVQXOITLA
# AGVTEVQRUITD