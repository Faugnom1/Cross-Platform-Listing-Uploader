function toggleFields() {
    let cloudinaryChecked = document.getElementById("cloudinaryCheck").checked;
    let facebookChecked = document.getElementById("facebookCheck").checked;
    let redditChecked = document.getElementById("redditCheck").checked;
    let etsyChecked = document.getElementById("etsyCheck").checked;
    let combinedContent = document.getElementById("combinedFields");
    let redditContentLabel = document.getElementById("redditContentLabel");
    let redditPostContent = document.getElementById("redditPostContent");

    if (redditChecked && facebookChecked) {

        redditContentLabel.style.display = "none";
        redditPostContent.style.display = "none";
        combinedContent.style.display = "block";
        document.getElementById("redditFields").style.display = "block";
        document.getElementById("facebookFields").style.display = "none";
    } else {

        combinedContent.style.display = "none";
        redditPostContent.style.display = "block";
        document.getElementById("redditFields").style.display = redditChecked ? "block" : "none";
        document.getElementById("redditContentLabel").style.display = redditChecked ? "block" : "none";
        document.getElementById("facebookFields").style.display = facebookChecked ? "block" : "none";

        if (!redditChecked) {
            redditContentLabel.style.display = "block";
        }
    }

    document.getElementById("cloudinaryFields").style.display = cloudinaryChecked ? "block" : "none";
    document.getElementById("etsyFields").style.display = etsyChecked ? "block" : "none";
}

document.addEventListener('DOMContentLoaded', function () {
    let subredditDropdown = document.getElementById('subredditSelect'); 
    let postTitleInput = document.getElementById('postTitle');

    subredditDropdown.addEventListener('change', function () {
        let subreddit = subredditDropdown.value;
        if (subreddit === 'appleswap' || subreddit === 'hardwareswap') {
            postTitleInput.value = '[USA-NJ][H] [W]';
        } else {
            postTitleInput.value = '';
        }
    });
});

