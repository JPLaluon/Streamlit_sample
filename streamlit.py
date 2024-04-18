import streamlit as st

def main():
    st.title('Concrete House Maintenance Analyzer')
    st.write('Welcome to Concrete House Maintenance Analyzer!'
             'This program will help you identify the parts of your'
             'house that either need maintenance or not. If it needs maintenance,'
             'you will be given numerical scalar measurements for each component of'
             'the building to guide you through the whole process within this service.'
             'If not, then an approximation of how long does it take before the next'
             'maintenance will be provided based on the information that’s been provided.')

    # Program Proper
    st.header('About Me')
    st.write('I am a Python developer with a passion for building web applications and data analysis projects.')
    st.write('Feel free to reach out to me at example@email.com.')

    # Projects section
    st.header('Projects')

    project_1 = {
        'title': 'Project 1',
        'description': 'Description of project 1.',
        'github_link': 'https://github.com/example/project1',
        'demo_link': 'https://demo.project1.com'
    }

    project_2 = {
        'title': 'Project 2',
        'description': 'Description of project 2.',
        'github_link': 'https://github.com/example/project2',
        'demo_link': 'https://demo.project2.com'
    }

    projects = [project_1, project_2]

    for project in projects:
        st.subheader(project['title'])
        st.write(project['description'])
        st.write('GitHub: [{}]({})'.format(project['title'], project['github_link']))
        st.write('Demo: [{}]({})'.format(project['title'], project['demo_link']))

if __name__ == '__main__':
    main()
