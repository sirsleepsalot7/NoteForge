from yt_dlp import YoutubeDL
import ffmpeg
import whisper
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Download video
if not os.path.exists("downloads/video.mp4"):

    print("Downloading video...")

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': 'downloads/video.%(ext)s'
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Video downloaded successfully!")

else:
    print("Video already exists. Skipping download...")

# Extract audio
if not os.path.exists("audio/audio.mp3"):

    print("Extracting audio...")

    (
        ffmpeg
        .input("downloads/video.mp4")
        .output("audio/audio.mp3")
        .run()
    )

    print("Audio extracted successfully!")

else:
    print("Audio already exists. Skipping extraction...")


# Check if transcript already exists
if os.path.exists("transcripts/transcript.txt"):

    print("Transcript already exists. Loading transcript...")

    with open("transcripts/transcript.txt", "r", encoding="utf-8") as f:
        transcript = f.read()

else:
    print("Loading Whisper model...")
    model = whisper.load_model("base")

    print("Transcribing audio...")
    result = model.transcribe("audio/audio.mp3")

    transcript = result["text"]
    

    with open("transcripts/transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript)

    print("Transcript saved successfully!")

# Prompt for notes generation
prompt = f"""
You are an expert academic note-taking assistant.

Generate COMPLETE and DETAILED study notes.

IMPORTANT:
- Do NOT skip concepts
- Preserve definitions
- Preserve formulas
- Preserve examples
- Use headings and bullet points
- Make notes revision-friendly

Lecture Transcript:
{transcript[:12000]}
"""

print("Generating notes using AI...")

response = client.chat.completions.create(
    model="deepseek/deepseek-v4-flash:free",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    timeout=300
)

notes = response.choices[0].message.content


# Save notes
with open("notes/notes.md", "w", encoding="utf-8") as f:
    f.write(notes)

print("Notes generated successfully!")