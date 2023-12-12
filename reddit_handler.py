import praw
import os
from dotenv import load_dotenv

load_dotenv()

def config_reddit():
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_USER_AGENT'),
        username=os.getenv('REDDIT_USERNAME'),
        password=os.getenv('REDDIT_PASSWORD')
)
    
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT'),
    username=os.getenv('REDDIT_USERNAME'),
    password=os.getenv('REDDIT_PASSWORD')
)

def set_selling_flair(submission, subreddit_name):
    """
    Set the flair of the submission to 'Selling' for 'appleswap' and 'hardwareswap' subreddits found from get_subreddit_flair.py
    """
    if subreddit_name == 'appleswap':
        submission.flair.select('e52255b8-d38d-11e6-aa39-0e1677116306')
    elif subreddit_name == 'hardwareswap':
        submission.flair.select('b00f081c-3426-11e3-8b34-12313b079641')



