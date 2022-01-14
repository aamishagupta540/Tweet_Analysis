import json
from twitter_stream import DEIStreamer

class Twitter_Stream_Wrapper:
	APP_KEY = ""
	APP_SECRET = ""
	OAUTH_TOKEN = ""
	OAUTH_TOKEN_SECRET = ""
	
	config_file_path = ""
	search_file_path = ""
	
	tweets_per_file = 0

	key_words = []
	

	def init_Stream(self,config_file_path,search_file_path,tweets_per_file):
		with open(config_file_path,'r') as config:
			creds = json.load(config)
			
			self.APP_KEY = creds['api_key']
			self.APP_SECRET = creds['api_secret_key']
			self.OAUTH_TOKEN = creds['oauth_token']
			self.OAUTH_TOKEN_SECRET = creds['oauth_token_secret']

		with open(search_file_path) as search_file:		
			lines = json.load(search_file)
			self.key_words = [word["keyword"] for word in lines]
		
		self.tweets_per_file = tweets_per_file
	
	def stream(self):
		streams = DEIStreamer(self.APP_KEY, self.APP_SECRET, self.OAUTH_TOKEN, self.OAUTH_TOKEN_SECRET)
		streams.init_variables(self.tweets_per_file)
		streams.statuses.filter(track = self.key_words)



if __name__ == "__main__":
	tsw = Twitter_Stream_Wrapper()
	tsw.init_Stream("C:\\python\\samples\\Twitter\\twitter_connection_config.json",
	"C:\\python\\samples\\Twitter\\search_terms.json",1000)
	tsw.stream()