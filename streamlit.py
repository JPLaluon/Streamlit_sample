import streamlit as st

# Home Page
def home():
    st.title("Welcome to Survey App")
    st.write("This is a survey about your experience.")
    if st.button("Start"):
        st.session_state['current_page'] = 'questions'
        st.session_state['current_question'] = 0
        st.session_state['responses'] = []

# Questions Page
def questions():
    st.title("Answer the Questions")
    questions = [
        "How satisfied are you with the product quality?",
        "How likely are you to recommend our service to others?",
        "How easy was it to use our website?"
    ]
    current_question = st.session_state['current_question']
    if current_question < len(questions):
        st.subheader(f"Question {current_question + 1}: {questions[current_question]}")
        response_submitted = st.session_state.get('response_submitted', False)
        if not response_submitted:
            response = st.radio("", options=[1, 2, 3, 4, 5], index=2, key=f"question_{current_question}")
            st.session_state['responses'].append(response)
            st.session_state['response_submitted'] = True
        else:
            st.write("You have already submitted a response for this question.")
        if st.button("Next"):
            st.session_state['current_question'] += 1
            st.session_state['response_submitted'] = False
    else:
        st.write("All questions answered.")
        st.button("See Results", key="result")
        st.session_state['current_page'] = 'result'

# Result Page
def result():
    st.title("Survey Results")
    st.write("Your responses:")
    for i, response in enumerate(st.session_state['responses']):
        st.write(f"Question {i+1}: {response}")
        if response == 1:
            st.write("HAHAHA")
        elif response == 2:
            st.write("HEHEHE")
        elif response == 3:
            st.write("HIHIHI")
        elif response == 4:
            st.write("HOHOHO")
        elif response == 5:
            st.write("HUHUHU")
            
# Main function to control page flow
def main():
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'home'

    if st.session_state['current_page'] == 'home':
        home()
    elif st.session_state['current_page'] == 'questions':
        questions()
    elif st.session_state['current_page'] == 'result':
        result()

if __name__ == "__main__":
    main()
