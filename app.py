```python
import streamlit as st
import random

# ==================================
# PAGE CONFIG
# ==================================
st.set_page_config(
    page_title="Composition Adventure Game",
    page_icon="✏️",
    layout="centered"
)

# ==================================
# GAME QUESTIONS
# ==================================
QUESTIONS = [
    {
        "question": "Which is the BEST opening sentence for a story about a lost puppy?",
        "options": [
            "Dogs are animals.",
            "I was walking in the park when I heard a frightened bark.",
            "The weather was hot.",
            "I like puppies."
        ],
        "answer": 1,
        "explanation": "A good opening introduces the event and makes readers curious."
    },
    {
        "question": "Which sentence shows feelings?",
        "options": [
            "The cake was on the table.",
            "I felt nervous as I stepped onto the stage.",
            "The room was large.",
            "There were many chairs."
        ],
        "answer": 1,
        "explanation": "Stories become more interesting when feelings are included."
    },
    {
        "question": "Which sentence uses descriptive language?",
        "options": [
            "The bird flew.",
            "The colourful bird soared across the bright blue sky.",
            "I saw a bird.",
            "Birds have wings."
        ],
        "answer": 1,
        "explanation": "Descriptive words help readers imagine the scene."
    },
    {
        "question": "What should every good story have?",
        "options": [
            "A problem",
            "Only a title",
            "Many colours",
            "A long paragraph"
        ],
        "answer": 0,
        "explanation": "A problem makes the story exciting and gives characters something to solve."
    },
    {
        "question": "Which is the BEST ending?",
        "options": [
            "The End.",
            "I learned that helping others brings happiness.",
            "Then I went home.",
            "It happened yesterday."
        ],
        "answer": 1,
        "explanation": "A strong ending often includes a lesson or reflection."
    },
    {
        "question": "Which sentence creates suspense?",
        "options": [
            "I opened the door.",
            "The door slowly creaked open as strange sounds echoed inside.",
            "The house was old.",
            "I walked away."
        ],
        "answer": 1,
        "explanation": "Suspense keeps readers wondering what will happen next."
    }
]

# ==================================
# SESSION STATE
# ==================================
if "score" not in st.session_state:
    st.session_state.score = 0

if "question" not in st.session_state:
    st.session_state.question = random.choice(QUESTIONS)

if "answered" not in st.session_state:
    st.session_state.answered = False

# ==================================
# TITLE
# ==================================
st.title("🎮 Composition Adventure Game")
st.write("Help your writing hero earn points and become a Story Master!")

st.markdown(
    f"""
    ### 🏆 Score: {st.session_state.score}
    """
)

st.divider()

# ==================================
# DISPLAY QUESTION
# ==================================
current = st.session_state.question

st.subheader("📚 Writing Challenge")

selected = st.radio(
    current["question"],
    current["options"]
)

# ==================================
# CHECK ANSWER
# ==================================
if st.button("✅ Submit Answer") and not st.session_state.answered:

    selected_index = current["options"].index(selected)

    if selected_index == current["answer"]:

        st.success("🎉 Correct!")
        st.write(current["explanation"])

        st.session_state.score += 10

    else:

        st.error("❌ Not quite right.")

        st.write(
            f"Correct Answer: **{current['options'][current['answer']]}**"
        )

        st.info(current["explanation"])

    st.session_state.answered = True

# ==================================
# NEXT QUESTION
# ==================================
if st.session_state.answered:

    if st.button("➡️ Next Challenge"):

        st.session_state.question = random.choice(QUESTIONS)
        st.session_state.answered = False
        st.rerun()

# ==================================
# ACHIEVEMENTS
# ==================================
st.divider()

st.subheader("⭐ Achievement Level")

if st.session_state.score >= 50:
    st.balloons()
    st.success("🏆 Story Master")

elif st.session_state.score >= 30:
    st.success("🌟 Writing Star")

elif st.session_state.score >= 10:
    st.info("👍 Beginner Writer")

else:
    st.write("Play more to unlock badges!")

# ==================================
# WRITING TIP
# ==================================
tips = [
    "Use interesting adjectives.",
    "Include feelings in your story.",
    "Describe what characters see and hear.",
    "Create a problem and solution.",
    "Use dialogue to make stories lively.",
    "End your story with a lesson learned."
]

st.divider()

st.subheader("💡 Writing Tip")
st.success(random.choice(tips))

# ==================================
# NEW GAME
# ==================================
st.divider()

if st.button("🔄 Start New Game"):
    st.session_state.score = 0
    st.session_state.question = random.choice(QUESTIONS)
    st.session_state.answered = False
    st.rerun()

st.caption("✏️ Composition Adventure Game for Young Writers")
```
