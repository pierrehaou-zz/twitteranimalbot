import config
import unsplashapirequest
import time

#setting variable for sleep function
downtime = 60 * 60 * 6

while True:
	# creates twitter api object
	api = config.create_api()

	# downloads random animal photo from Unsplash API, returns source link
	source_text = unsplashapirequest.download_photo()

	# Posts tweet to twitter with both the photo and photo source
	api.update_with_media(
	    "uphoto.jpg", status=f"This photo can be found at {source_text}")
	
	print("deployed to Heroku!")

	# Sets function to run four times a day
	time.sleep(downtime)
