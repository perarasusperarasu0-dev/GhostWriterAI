import json
from datetime import datetime
from pathlib import Path

import requests
import streamlit as st


# -----------------------------
# Project configuration
# -----------------------------

APP_TITLE = "GhostWriter AI"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:0.5b"

DATA_DIR = Path(__file__).parent / "data"
STORIES_FILE = DATA_DIR / "stories.json"


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="👻",
    layout="wide"
)


# -----------------------------
# Story storage functions
# -----------------------------

def load_stories():
    DATA_DIR.mkdir(exist_ok=True)

    if not STORIES_FILE.exists():
        return []

    try:
        with STORIES_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_story(title, theme, story):
    stories = load_stories()

    new_story = {
        "title": title,
        "theme": theme,
        "story": story,
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    stories.insert(0, new_story)

    with STORIES_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            stories,
            file,
            ensure_ascii=False,
            indent=4
        )


# -----------------------------
# AI story generation
# -----------------------------

def generate_story(topic, theme, length):
    prompt = f"""
You are GhostWriter AI, a creative horror story writer.

Write an original fictional story using these details:

Topic: {topic}
Theme: {theme}
Length: {length}

Requirements:
- Write in simple, engaging English.
- Give the story a suitable title.
- Create suspense and atmosphere.
- Keep the story original.
- Do not claim that fictional events are real.
- Return only the title and story.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    response.raise_for_status()

    result = response.json()
    story = result.get("response", "").strip()

    if not story:
        raise ValueError("The AI returned an empty story.")

    return story


# -----------------------------
# Main user interface
# -----------------------------

st.title("👻 GhostWriter AI")
st.subheader("Unleash your imagination with local AI!")

st.write(
    "Create spooky stories with an AI model running "
    "on your own computer."
)

st.info(
    f"Local model: {MODEL_NAME} | "
    "AI service: Ollama"
)

st.divider()

st.header("✍️ Create Your Story")

topic = st.text_input(
    "Enter your story topic",
    placeholder="Example: A mysterious school at midnight"
)

theme = st.selectbox(
    "Choose a theme",
    [
        "Ghost Story",
        "Haunted House",
        "Abandoned School",
        "Dark Mystery",
        "Supernatural Adventure",
        "Halloween Night"
    ]
)

length = st.selectbox(
    "Choose story length",
    [
        "Short (around 150 words)",
        "Medium (around 300 words)",
        "Long (around 500 words)"
    ]
)

if st.button("👻 Generate Story", type="primary"):
    if not topic.strip():
        st.warning("Please enter a story topic.")
    else:
        try:
            with st.spinner(
                "The ghost writer is creating your story..."
            ):
                generated_story = generate_story(
                    topic.strip(),
                    theme,
                    length
                )

            st.session_state["generated_story"] = (
                generated_story
            )
            st.session_state["generated_title"] = (
                topic.strip()
            )
            st.session_state["generated_theme"] = theme

        except requests.exceptions.ConnectionError:
            st.error(
                "Cannot connect to Ollama. "
                "Please check whether Ollama is running."
            )

        except requests.exceptions.Timeout:
            st.error(
                "The AI took too long to respond. "
                "Please try again."
            )

        except requests.exceptions.RequestException as error:
            st.error(f"Ollama request failed: {error}")

        except ValueError as error:
            st.error(str(error))


# -----------------------------
# Display and save generated story
# -----------------------------

if st.session_state.get("generated_story"):
    st.divider()
    st.header("📖 Your Generated Story")

    story = st.session_state["generated_story"]
    title = st.session_state["generated_title"]
    selected_theme = st.session_state["generated_theme"]

    st.markdown(f"### {title}")
    st.caption(f"Theme: {selected_theme}")
    st.write(story)

    st.download_button(
        "⬇️ Download Story",
        data=story,
        file_name="ghost_story.txt",
        mime="text/plain"
    )

    if st.button("💾 Save to Story Library"):
        try:
            save_story(title, selected_theme, story)
            st.success("Story saved successfully!")
        except OSError as error:
            st.error(f"Could not save the story: {error}")


# -----------------------------
# Saved story library
# -----------------------------

st.divider()
st.header("📚 Your Story Library")

saved_stories = load_stories()

if not saved_stories:
    st.write("No saved stories yet. Create your first story!")
else:
    st.write(f"Saved stories: {len(saved_stories)}")

    for index, item in enumerate(saved_stories):
        story_title = item.get("title", "Untitled Story")

        with st.expander(f"👻 {story_title}"):
            st.caption(
                f"Theme: {item.get('theme', 'Unknown')} | "
                f"Created: {item.get('created_at', 'Unknown')}"
            )

            st.write(item.get("story", ""))

st.divider()

st.caption(
    "GhostWriter AI | Python + Streamlit + Ollama | "
    "A local open-weight AI project"
)