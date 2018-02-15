require('dotenv').config()

const Twitter   = require('twitter'),
	  Sentiment = require('sentiment'),
	  JSONfile  = require('jsonfile')

let file = 'data.json'

let client = new Twitter({
	consumer_key: process.env.TWITTER_CONSUMER_KEY,
	consumer_secret: process.env.TWITTER_CONSUMER_SECRET,
	access_token_key: process.env.TWITTER_ACCESS_TOKEN_KEY,
	access_token_secret: process.env.TWITTER_ACCESS_TOKEN_SECRET
})

let t = [];

function getTweets (params) {
	client.get('statuses/user_timeline', params, (error, tweets, response) => {
		if (!error) {
			for (i=0; i<tweets.length; i++) {
				tweets[i].sentiment = Sentiment(tweets[i].text)
				JSONfile.writeFile(file, tweets[i], {flag: 'a'}, function (err) {
					console.error(err)
				})
			}
			getTweets({ count: 200, screen_name: 'potus', max_id: tweets[tweets.length-1].id })
		}
		// console.log(error)
	});
}

let params = {
	count: 200,
	screen_name: 'potus'
};
getTweets(params)