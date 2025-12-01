# TranscribeIt

TranscribeIt is a free software video transcription service for videos and live streams.

# Why?

Hard of hearing and speech population, people with visual impairments and sensory processing disorders have difficulty navigating video content. With online platforms providing little to no transcriptions or inaccurate transcriptions, especially for live streams, it hinders acccessibility. TransribeIt aims to provide customized and diarized transcriptions for making video content accessible.

# Features

1. Transcribe videos and livestreams from YouTube and other online sources supported by [yt-dlp](https://pypi.org/project/yt-dlp).
2. Get transcriptions with timestamps in an intuitive UI.

# Roadmap

- Download transcripts in different formats (STT, JSON, etc.)
- Include speaker diarization
- Background processing
- Transcription from local audio file uploads

# Get Started

1. Clone the project
```sh
git clone https://github.com/fossiaorg/transcribeit
cd transcribeit
```

2. Set up frontend
```sh
cd frontend
yarn install
```

3. Configure environment variables for frontend
```sh
cp .env.sample .env
# Edit the values as per needed for .env
```

4. Set up backend
```sh
cd backend
poetry install
$(poetry env activate)
```

5. Configure environment variables for backend
```sh
cp .env.sample .env
# Edit the values as per needed for .env
```

6. Run the frontend and backend
    - For frontend
    ```sh
    yarn dev
    ```
    - For backend
    ```sh
    fastapi dev src/transcribeit/server.py
    ```

# License

TranscribeIt is licensed under GNU Affero General Public License version 3. For more information, check out our [LICENSE](./LICENSE) file.