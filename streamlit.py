import streamlit as st

def main():
    st.title('My Portfolio')
    st.write('Welcome to my portfolio! Here, you can learn more about me and my projects.')

    # About Me section
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
