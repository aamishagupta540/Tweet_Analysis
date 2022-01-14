from twython import TwythonStreamer
import json
import uuid

with open("C:\\python\\samples\\Twitter\\twitter_connection_config.json",'r') as cfile:
    creds = json.load(cfile)


class DEIStreamer(TwythonStreamer):
    tweets = []
    no_of_tweets = 0
    tweets_per_file = 1000

    def process_tweets(self,tweet):
        try:
            self.tweets.append(tweet)
            self.no_of_tweets += 1
            if self.no_of_tweets > self.tweets_per_file:
                path = "C:\\python\\samples\\Twitter\\tweet_data\\"
                filename = "tweet_"+str(uuid.uuid4())+".json"
                filepath = path+filename
                self.save_to_disk(self.tweets,filepath)
                self.no_of_tweets = 0
                self.tweets = []
        except:
            self.disconnect()
    
    def init_variables(self,tweets):
        self.tweets_per_file = tweets

    def on_success(self,data):
        try:
            if data['lang'] == 'en':
                self.process_tweets(data)
        except:
            self.disconnect()
    
    def on_error(self,status_code,data):
        print(status_code,data)
        self.disconnect()

    def disconnect(self):
        self.disconnect()

    def on_timeout(self,data):
        pass
    
    def save_to_disk(self,tweets,filepath):
        with open(filepath,'w') as outfile:
            json.dump(tweets,outfile)



