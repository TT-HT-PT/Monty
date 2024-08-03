from twitter import (
    tweet,
    MessageTooLongError,
    CommunicationError,
)

message = input("What would you like to tweet?  ")
message = input("What would you like to tweet?  ")
# Your code here
try:
    tweet(message)
except CommunicationError:
        print("An error occurred attempting to connect to Twitter. Please try again!")
except MessageTooLongError as err:
	print("Oh no! Your message was too long ({})".format(err))