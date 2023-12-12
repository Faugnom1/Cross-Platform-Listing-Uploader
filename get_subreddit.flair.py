import praw
import os
from dotenv import load_dotenv

load_dotenv()

def get_subreddit_flairs(reddit_instance, subreddit_name):
    subreddit = reddit_instance.subreddit(subreddit_name)
    flairs = list(subreddit.flair.link_templates.user_selectable())
    return flairs

reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT'),
    username=os.getenv('REDDIT_USERNAME'),
    password=os.getenv('REDDIT_PASSWORD')
)

appleswap_flairs = get_subreddit_flairs(reddit, 'appleswap')
hardwareswap_flairs = get_subreddit_flairs(reddit, 'hardwareswap')

print("Appleswap Flairs:", appleswap_flairs)
print("Hardwareswap Flairs:", hardwareswap_flairs)