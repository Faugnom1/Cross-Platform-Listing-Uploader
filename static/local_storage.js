function saveToLocalStorage() {
    const combinedContent = document.getElementById("combinedContent").value;
    const subreddit = document.getElementById("subredditSelect").value;
    const postTitle = document.getElementById("postTitle").value;
    const redditContent = document.getElementById("redditPostContent").value;
    const facebookContent = document.getElementById("facebookContent").value;
    const cloudinaryContent = document.getElementById("cloudinaryImage").value;

    const postData = {
        cloudinaryContent,
        combinedContent,
        subreddit,
        postTitle,
        redditContent,
        facebookContent,
    };

    localStorage.setItem("uploadedData", JSON.stringify(postData));
}

document.addEventListener('DOMContentLoaded', function () {
    const savedData = localStorage.getItem("uploadedData");

    if (savedData) {
        const postData = JSON.parse(savedData);
    }
});