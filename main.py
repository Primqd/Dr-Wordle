import streamlit as st
from guess_logic import hint, guess, give_up, fun_fact, reload
from streamlit_js_eval import streamlit_js_eval

curr = st.session_state

def good(k, k_response = ""):
    if k == "True":
        return "You got the word!"
    elif k == "False":
        return "Not a valid response, try again"
    else:
        return k_response
if 'hint' not in curr:
    curr.hint = hint()
if 'previous' not in curr:
    curr.previous = []

st.image("diseasewordle.jpg")

st.markdown("<h5 style='text-align: center; color: white;'>Guess a hidden disease by typing in the box. Dr. Wordle will return shared features with the hidden disease.</h5>", unsafe_allow_html=True)

guessed = st.text_input("Guess Here:")
if guessed:
    response = guess(guessed)
    if response == "True":
        st.write("You got the word! " + fun_fact())
    elif response == "False": st.write("Not a valid response")
    else:
        st.markdown(f"**{response}**")
        curr.previous.append((guessed, good(guessed, response)))
else:
    st.write("No input detected. Try again.")

st.divider()
st.write("\n")
st.write("Previous Guesses:")

for _ in range(-1, -len(curr.previous) - 1, -1):
    i = curr.previous[_]
    st.write(f"{i[0]}: **{i[1]}**")

st.divider()
st.write("\n")
if st.button('Hint'):
    st.write(f'Hint: {curr.hint}')
if st.button('Give Up'):
    st.write(f'You gave up. The answer is {give_up()}.')
if st.button("New Puzzle"):
    reload()
    streamlit_js_eval(js_expressions="parent.window.location.reload()")
st.write("Created as part of WAForge")
st.write("By Franklin Chen, Varun Patankar, Karunya Penumalla")