import streamlit as st
from guess_logic import hint, guess, give_up, fun_fact, reload
from streamlit_js_eval import streamlit_js_eval

def main():
    curr = st.session_state # i hate session state :(

    if 'hint' not in curr:
        curr.hint = hint()
    if 'previous' not in curr:
        curr.previous = []

    image = st.image("diseasewordle.jpg")

    title = st.markdown("<h5 style='text-align: center; color: white;'>Guess a hidden disease by typing in the box. Dr. Wordle will return shared features with the hidden disease.</h5>", unsafe_allow_html=True)

    guessed = st.text_input("Guess Here:")
    if guessed:
        response = guess(guessed)
        print(response)
        if response == "You got the word!": st.write(response + " " + fun_fact())
        elif response == "Not a disease, please try again.": st.write(response)
        else:
            st.markdown(f"**{response}**")
            curr.previous.append((guessed, response))
    else:
        st.write("No input detected, try again.")

    st.divider()
    st.write("\n")
    st.write("Previous Guesses:")

    for i in range(-1, -len(curr.previous) - 1, -1): # queue rendering
        # can't use actual queue cause i have to create and destory it every time ://
        st.write(f"{curr.previous[i][0]}: **{curr.previous[i][1]}**")

    st.divider()
    st.write("\n")

    if st.button('Hint'):
        st.write(f'Hint: {curr.hint}')
    if st.button('Give Up'):
        st.write(f'You gave up. The answer is {give_up()}.')
    if st.button("New Puzzle"):
        reload()
        streamlit_js_eval(js_expressions="parent.window.location.reload()") # reset the page

    st.write("Created as part of WAForge")
    st.write("By Franklin Chen, Varun Patankar, Karunya Penumalla")
    
if __name__ == "__main__": main()