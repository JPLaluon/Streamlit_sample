import page

import streamlit as st

def main():
    st.title('Concrete House Maintenance Analyzer')
    st.write('Welcome to Concrete House Maintenance Analyzer! '
             'This program will help you identify the parts of your '
             'house that either need maintenance or not. If it needs maintenance, '
             'you will be given numerical scalar measurements for each component of '
             'the building to guide you through the whole process within this service. '
             'If not, then an approximation of how long does it take before the next '
             'maintenance will be provided based on the information that’s been provided.')

    # Define the sidebar navigation
    page = st.sidebar.selectbox("Select a page", ["Home", "Information"])

    # Program Proper - Home Page
    if page == "Home":
        st.header('Concrete House Maintenance Analyzer')
        st.write('Click below to start analyzing.')

        # Button to navigate to the information page
        if st.button("Start"):
            st.experimental_rerun()
def display_questions():
    st.title("Answer the Questions")

        # Sample questions
        questions = [
                "How satisfied are you with the product quality?",
                "How likely are you to recommend our service to others?",
                "How easy was it to use our website?"
            ]

        # Display questions and collect responses
        for i, question in enumerate(questions):
            st.subheader(f"Question {i + 1}: {question}")
            likert_scale_response = st.slider("", 1, 5, 3, key=f"question_{i + 1}")
            st.write(f"You rated this question: {likert_scale_response}")

        def main():
            st.title("Welcome to My Website")

            # Button to lead to new interface
            if st.button("Start"):
                display_questions()


        # Information page
    elif page == "Information":
        st.header("Information Interface")
        st.write("This is the information interface.")
        st.write("New information goes here.")

    # Projects section
    st.header('Projects')

    project_1 = {
        'title': 'Project 1',
        'description': 'Description of project 1.',
        'github_link': 'https://github.com/example/project1',
        'demo_link': 'https://demo.project1.com'
    }

    projects = [project_1]

    for project in projects:
        st.subheader(project['title'])
        st.write(project['description'])
        st.write('GitHub: [{}]({})'.format(project['title'], project['github_link']))
        st.write('Demo: [{}]({})'.format(project['title'], project['demo_link']))

if __name__ == '__main__':
    main()
