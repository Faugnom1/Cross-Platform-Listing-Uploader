from flask import Flask, request, render_template, redirect, url_for
import cloudinary.uploader
import logging
from cloudinary_handler import config_cloudinary 
from reddit_handler import config_reddit, reddit, set_selling_flair
from facebook_handler import post_to_facebook, page_id, my_store, post_with_image

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def upload_data():
    reddit_post_url = None
    facebook_post_url = None
    image_urls = None

    if request.method == 'POST':
        # Cloudinary image uploads
        cloudinary_files = request.files.getlist('cloudinaryImage')
        image_urls = [cloudinary.uploader.upload(file)['url'] for file in cloudinary_files if file]
        image_urls = [url.replace("%5B'", '').replace("'%5D", '') for url in image_urls]
    
    
        # Get post data
        combined_content = request.form.get('combinedContent')
        subreddit_name = request.form.get('subreddit')
        reddit_title = request.form.get('postTitle')
        reddit_content = request.form.get('redditPostContent')
        facebook_content = request.form.get('facebookContent')

        cloudinary_uploaded = bool(image_urls)
        reddit_uploaded = subreddit_name and reddit_title and reddit_content
        facebook_uploaded = facebook_content
        combined_uploaded = combined_content

        # Reddit posting
        if reddit_uploaded:
            if image_urls:
                reddit_content += "\n\n" + "\n".join(image_urls)

            subreddit = reddit.subreddit(subreddit_name)
            submission = subreddit.submit(title=reddit_title, selftext=reddit_content)
            reddit_post_url = submission.url
            set_selling_flair(submission, subreddit_name)

        # Facebook posting
        if facebook_content:
            facebook_post_url = my_store
            if cloudinary_uploaded:
                post_with_image(page_id, image_urls[0], facebook_content)
                # if len(image_urls)>1:
                #     create_album_and_upload_images(page_id, "New Album", image_urls, facebook_content)
                # else:
                #     post_with_image(page_id, image_urls[0], facebook_content)
            else:
                post_to_facebook(page_id, facebook_content)

        # Reddit and Facebook Posting
        if combined_uploaded:
            facebook_content = combined_content
            facebook_post_url = my_store
            if cloudinary_uploaded:
                combined_content += "\n\n" + "\n".join(image_urls)
                
                post_with_image(page_id, image_urls[0], facebook_content)
                subreddit = reddit.subreddit(subreddit_name)
                submission = subreddit.submit(title=reddit_title, selftext=combined_content)
                reddit_post_url = submission.url
                set_selling_flair(submission, subreddit_name)
            else:
                subreddit = reddit.subreddit(subreddit_name)
                submission = subreddit.submit(title=reddit_title, selftext=combined_content)
                reddit_post_url = submission.url
                set_selling_flair(submission, subreddit_name)
                post_to_facebook(page_id, facebook_content)

        # # Redirect logic
        if cloudinary_uploaded and not reddit_uploaded and not facebook_uploaded and not combined_uploaded:
            return redirect(url_for('show_combined_posts', image_urls=image_urls))

        elif reddit_uploaded and not cloudinary_uploaded and not facebook_uploaded:
            return redirect(reddit_post_url)
        
        elif facebook_uploaded and not reddit_uploaded and not cloudinary_uploaded:
            return redirect(my_store)

        elif cloudinary_uploaded and facebook_uploaded and not reddit_uploaded:
            return redirect(my_store)
        
        elif cloudinary_uploaded and reddit_uploaded and not facebook_uploaded:
            return redirect(reddit_post_url)

        elif combined_uploaded and not cloudinary_uploaded:
            return redirect(url_for('show_combined_posts', reddit_url=reddit_post_url, facebook_url=facebook_post_url))
        
        elif combined_uploaded and cloudinary_uploaded:
            return redirect(url_for('show_combined_posts', image_urls=image_urls, reddit_url=reddit_post_url, facebook_url=facebook_post_url))

    return render_template('home.html')

@app.route('/previous-posts', methods=['GET'])
def show_previous_posts():
    return render_template('previous_posts.html')

@app.route('/combined-posts', methods=['GET'])
def show_combined_posts():
    reddit_url = request.args.get('reddit_url')
    facebook_url = request.args.get('facebook_url')
    image_urls = request.args.getlist('image_urls')
    return render_template('show_combined_posts.html', reddit_url=reddit_url, facebook_url=facebook_url, image_urls=image_urls)


if __name__ == '__main__':
    config_cloudinary()
    config_reddit() 
    app.run(debug=True)
