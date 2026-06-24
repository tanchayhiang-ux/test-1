import streamlit as st
import random

# ----------------------------
# Page Setup
# ----------------------------
st.set_page_config(
    page_title="Composition Adventure",
    page_icon="✏️",
    layout="centered"
)

# ----------------------------
# Session State
# ----------------------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_number" not in st.session_state:
    st.session_state.question_number = 1

if "current_question" not in st.session_state:
    st.session_state.current_question = None

# ----------------------------
# Question Bank
# ----------------------------
questions = [
    {
        "scenario": "You found a lost puppy at the park. What is the BEST opening sentence?",
        "choices": [
            "I was walking in the park when I heard a soft bark.",
            "Dogs are animals.",
            "The park is green.",
            "My favourite food is pizza."
        ],
        "answer": 0,
        "explanation": "A good opening introduces the event and catches the reader's interest."
    },
    {
        "scenario": "Your composition is about a surprise birthday party. Which sentence shows feelings?",
        "choices": [
            "There were balloons.",
            "The cake was round.",
            "I was shocked and excited when everyone shouted 'Surprise!'",
            "The party started at 5pm."
        ],
        "answer": 2,
        "explanation": "Good compositions describe emotions to make the story interesting."
    },
    {
        "scenario": "Which sentence uses descriptive language?",
        "choices": [
            "The dog ran.",
            "The fluffy golden dog sprinted across the grassy field.",
            "The dog is an animal.",
            "I saw a dog."
        ],
        "answer": 1,
        "explanation": "Descriptive words help readers imagine the scene."
    },
    {
        "scenario": "What should happen before the ending of a story?",
        "choices": [
            "The problem is solved.",
            "The title appears.",
            "The author introduces himself.",
            "Nothing happens."
        ],
        "answer": 0,
        "explanation": "Stories usually solve the problem before ending."
    },
    {
        "scenario": "Which sentence is the BEST ending?",
        "choices": [
            "The End.",
            "I learned that helping others brings happiness.",
            "There was a dog.",
            "I went home."
        ],
        "answer": 1,
        "explanation": "A good ending reflects on the experience or lesson learned."
    },
    {
        "scenario": "You are writing about a rainy day. Which sentence creates a vivid picture?",
        "choices": [
            "It rained.",
            "Rain is water.",
            "Huge raindrops drummed loudly on the roof.",
            "The weather changed."
        ],
        "answer": 2,
        "explanation": "Strong details help readers imagine the scene."
    }
]

# ----------------------------
# New Question Function
# ----------------------------
def get_new_question():
    return random.choice(questions)

if st.session_state.current_question is None:
    st.session_state.current_question = get_new_question()

q = st.session_state.current_question

# ----------------------------
# Title
# ----------------------------
st.title("✏️ Composition Adventure")
st.subheader("Help your writing hero earn points!")

st.success(f"🏆 Score: {st.session_state.score}")

st.write(f"### Question {st.session_state.question_number}")

st.info(q["scenario"])

choice = st.radio(
    "Choose the best answer:",
    q["choices"],
    key=f"choice_{st.session_state.question_number}"
)

# ----------------------------
# Submit Answer
# ----------------------------
if st.button("Submit Answer"):

    selected_index = q["choices"].index(choice)

    if selected_index == q["answer"]:
        st.success("🎉 Correct! Great job!")
        st.write("**Why?**")
        st.write(q["explanation"])

        st.session_state.score += 10

    else:
        st.error("❌ Not quite. Try to learn from this!")
        st.write("**Explanation:**")
        st.write(q["explanation"])

        correct_answer = q["choices"][q["answer"]]
        st.write(f"✅ Correct answer: **{correct_answer}**")

# ----------------------------
# Next Question
# ----------------------------
if st.button("Next Question"):

    st.session_state.question_number += 1
    st.session_state.current_question = get_new_question()

    st.rerun()

# ----------------------------
# Achievement Section
# ----------------------------
st.divider()

if st.session_state.score >= 50:
    st.balloons()
    st.success("🌟 Writing Star! You have earned 50 points!")

elif st.session_state.score >= 30:
    st.success("🚀 Great Writer! Keep going!")

elif st.session_state.score >= 10:
    st.info("👍 Good Start! Keep learning!")

# ----------------------------
# Reset Game
# ----------------------------
if st.button("🔄 Start New Game"):
    st.session_state.score = 0
    st.session_state.question_number = 1
    st.session_state.current_question = get_new_question()
    st.rerun()
