# YouTube Video Uploader
This repository contains a Python-based application that automates the uploading of videos to YouTube using the YouTube Data API. The application is designed to streamline the process of uploading videos, managing metadata, and interacting with your YouTube account programmatically.

## Features

- **OAuth 2.0 Authentication:** Securely authenticate with your Google account using OAuth 2.0. The application manages tokens locally for repeated use without requiring re-authentication.
- - **Automated Video Uploading:** Upload videos to your YouTube channel with customizable titles, descriptions, tags, and privacy settings.
- - **Channel Management:** Retrieve and display channel information, including statistics like view counts, subscriber counts, and uploaded video details.
- - **Extensible:** The modular design allows easy integration into larger workflows or automation systems.
## Getting Started

### Prerequisites

- Python 3.6 or higher
- - A Google Cloud Console project with the YouTube Data API enabled
- - `client_secrets.json` file obtained from the Google Cloud Console for OAuth 2.0 authentication
### Installation

1. **Clone the repository:**
    ```bash
        git clone https://github.com/your-username/youtube-video-uploader.git
            cd youtube-video-uploader
                ```
                
                1. **Install the required Python packages:**
              1.     ```bash
              2.     pip install -r requirements.txt
              3.     ```
            1. 3. **Set up Google API credentials:**
          1.     - Go to the [Google Cloud Console](https://console.cloud.google.com/).
          2.     - Create a new project and enable the YouTube Data API.
          3.     - Generate OAuth 2.0 credentials and download the `client_secrets.json` file.
          4.     - Place the `client_secrets.json` file in the root directory of your project.
        1. ### Usage
      1. #### 1. Authenticate with Google
    1. Run the authentication script to authenticate with your Google account and generate a token for future requests.
  1. ```bash
  2. python authenticate.py

This will open a browser window prompting you to sign in with your Google account and authorize the application.

1. Upload a Video
2. After successfully authenticating, you can upload a video by running the upload_video.py script:
3. ```bash
4. python upload_video.py --file "path_to_your_video.mp4" --title "My Video Title" --description "This is a description of my video." --tags "tag1,tag2" --category "22" --privacyStatus "public"

--file: Path to the video file you want to upload.
--title: Title of the video.
--description: Description of the video.
--tags: Comma-separated list of tags for the video.
--category: Category ID for the video (e.g., 22 for "People & Blogs").
--privacyStatus: Privacy status of the video (public, private, unlisted).

## License
This project is licensed under the MIT License - see the LICENSE file for details.
