# NoteForge
AI-powered lecture understanding system that converts YouTube lectures into structured revision notes using Whisper and LLMs.

## Overview
NoteForge is an AI study assistant that converts long educational YouTube lectures into structured revision notes automatically.

The system:

* downloads lecture videos
* extracts audio
* transcribes speech using Whisper AI
* generates structured notes using LLMs
* creates reusable study material for revision

This project was built to solve a real student problem:

> Watching lectures while making detailed notes takes too much time, but watching without notes makes revision difficult later.

NoteForge automates the note-making process while preserving concepts, explanations, formulas, and examples.

---

# Current Features

## Implemented MVP

### YouTube Lecture Processing

* Download lecture videos from YouTube
* Cache downloaded videos

### Audio Extraction

* Extract audio using FFmpeg
* Cache extracted audio

### AI Speech Recognition

* Transcribe lectures using OpenAI Whisper
* Save transcript locally
* Reuse transcript without retranscribing

### AI Notes Generation

* Generate structured study notes using LLMs
* Uses OpenRouter API
* Supports free models like DeepSeek/Qwen

### Pipeline Caching

Avoids reprocessing already completed stages:

* video cache
* audio cache
* transcript cache

---

# Architecture

```text
YouTube URL
    ↓
Video Download (yt-dlp)
    ↓
Audio Extraction (FFmpeg)
    ↓
Whisper Speech Recognition
    ↓
Transcript Generation
    ↓
LLM Notes Generation
    ↓
Structured Study Notes
```

---

# Tech Stack

## Backend

* Python

## AI Models

* Whisper
* DeepSeek/Qwen via OpenRouter

## Video Processing

* yt-dlp
* FFmpeg

## APIs

* OpenRouter API

## Libraries

* openai
* python-dotenv
* ffmpeg-python
* openai-whisper

---

# Project Structure

```text
study-ai/
│
├── downloads/
├── audio/
├── transcripts/
├── notes/
├── venv/
├── .env
├── main.py
└── requirements.txt
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your_repo_url>
cd study-ai
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```bash
pip install yt-dlp openai-whisper ffmpeg-python openai python-dotenv
```

---

## 4. Install FFmpeg

Download FFmpeg:

[https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

Add FFmpeg `bin` folder to system PATH.

Test installation:

```bash
ffmpeg -version
```

---

## 5. Setup OpenRouter API

Create `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

# Running the Project

```bash
python main.py
```

Paste a YouTube lecture URL when prompted.

---

# Example Workflow

```text
Input:
YouTube lecture URL

Output:
- video.mp4
- audio.mp3
- transcript.txt
- notes.md
```

---

# Current Limitations

* Long lectures are truncated temporarily using transcript slicing
* No diagram understanding yet
* No OCR yet
* No timestamps in notes
* Single-file pipeline architecture

---

# Planned Features

## Short-Term

* Transcript chunking
* Better markdown formatting
* Timestamp linking
* Retry/fallback models
* Flashcards generation
* Revision mode

## Advanced Features

* OCR for slides
* Formula extraction
* Diagram understanding
* Multimodal note generation
* Searchable lecture memory
* Quiz generation
* RAG-based lecture chat

---

# Future Architecture

```text
Transcript
    ↓
Chunking
    ↓
Chunk Summaries
    ↓
Merged Notes
    ↓
Revision Notes
```

---

# Why This Project Matters

Most AI note tools only summarize transcripts.

NoteForge aims to become a complete lecture understanding system capable of:

* preserving explanations
* understanding diagrams
* extracting formulas
* generating revision-ready notes
* reducing manual note-making time for students

---

# Learning Outcomes

This project demonstrates:

* AI pipeline engineering
* speech recognition
* API integration
* prompt engineering
* caching systems
* long-context handling
* video/audio processing
* LLM orchestration

---

# Author

Built by Lakshya Kewlani.

---

# License

MIT License
