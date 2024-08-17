
# YouTube Video Uploader

This project contains two Python scripts that allow you to authenticate with the YouTube Data API and upload videos directly to YouTube.

## Files

- `authenticate.py`: Handles the authentication process with the YouTube Data API.
- `upload_video.py`: Contains the logic to upload a video to YouTube.

## Prerequisites

Before running the scripts, make sure you have the following:

1. Python 3.x installed.
2. The `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, and `google-api-python-client` libraries installed. You can install them using pip:

    ```bash
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
    ```

3. A `client_secrets.json` file downloaded from your Google Developer Console with YouTube Data API enabled.

## How to Use

### Step 1: Authentication

1. Place your `client_secrets.json` file in the same directory as `authenticate.py`.
2. Run the `upload_video.py` script. The authentication process will be initiated automatically if no valid credentials are found.

### Step 2: Upload a Video

1. Edit the `upload_video.py` script to modify the parameters such as `video_file`, `title`, `description`, `tags`, `category_id`, and `privacy_status` according to your needs.
2. Run the `upload_video.py` script:

    ```bash
    python upload_video.py
    ```

3. Upon successful upload, the script will print the ID of the uploaded video.

## Notes

- The script saves the OAuth tokens in a `token.pickle` file for future use.
- Make sure your video file is in the correct format supported by YouTube.

## License

This project is licensed under the MIT License.
