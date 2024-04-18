import streamlit as st

def main():
    st.title("Roof Repair Survey")

    # Homepage with start button
    if st.button("Start Survey"):
        choose_aspect()

def choose_aspect():
    st.write("Choose from the following you want to analyze:")
    aspect_option = st.radio(
        "Options:",
        ('Ceiling', 'Floor', 'Roof', 'Wall')
    )

    # Next button to move to the next question
    if st.button("Next"):
        if aspect_option == 'Ceiling':
            question_ceiling()
        elif aspect_option == 'Floor':
            question_floor()
        elif aspect_option == 'Roof':
            question_roof()
        elif aspect_option == 'Wall':
            question_wall()

def question_ceiling():
    st.write("You chose to analyze: Ceiling")
    st.write("Question 1: How long has it been since your ceiling was repaired?")
    option1 = st.radio(
        "Choose an option:",
        ('1 - Very recently', '2 - Within the past year', '3 - 1-3 years ago', '4 - 3-5 years ago', '5 - More than 5 years ago')
    )

    # Next button to move to the next question
    if st.button("Next"):
        st.write("Question 2: How satisfied are you with the quality of the ceiling repair?")
        option2 = st.radio(
            "Choose an option:",
            ('1 - Very Satisfied', '2 - Satisfied', '3 - Neutral', '4 - Dissatisfied', '5 - Very Dissatisfied')
        )

        # Change previous answer button
        if st.button("Change Previous Answer"):
            choose_aspect()
        elif st.button("Next"):
            st.write("Question 3: How effective was the ceiling repair in solving the issue?")
            option3 = st.radio(
                "Choose an option:",
                ('1 - Very Effective', '2 - Effective', '3 - Neutral', '4 - Ineffective', '5 - Very Ineffective')
            )

            # Change previous answer button
            if st.button("Change Previous Answer"):
                question_ceiling()
            elif st.button("Next"):
                st.write("Question 4: How often do you experience issues with your ceiling after the repair?")
                option4 = st.radio(
                    "Choose an option:",
                    ('1 - Never', '2 - Rarely', '3 - Occasionally', '4 - Frequently', '5 - Always')
                )

                if st.button("Change Previous Answer"):
                    question_ceiling()
                elif st.button("Next"):
                    st.write("Question 5: How likely are you to hire the same contractor for future ceiling repairs?")
                    option5 = st.radio(
                        "Choose an option:",
                        ('1 - Very Likely', '2 - Likely', '3 - Neutral', '4 - Unlikely', '5 - Very Unlikely')
                    )
                    if st.button("Next"):
                        show_results('Ceiling', option1, option2, option3, option4, option5)

def question_floor():
    st.write("You chose to analyze: Floor")
    st.write("Question 1: How long has it been since your floor was repaired?")
    option1 = st.radio(
        "Choose an option:",
        ('1 - Very recently', '2 - Within the past year', '3 - 1-3 years ago', '4 - 3-5 years ago', '5 - More than 5 years ago')
    )

    # Next button to move to the next question
    if st.button("Next"):
        st.write("Question 2: How satisfied are you with the quality of the floor repair?")
        option2 = st.radio(
            "Choose an option:",
            ('1 - Very Satisfied', '2 - Satisfied', '3 - Neutral', '4 - Dissatisfied', '5 - Very Dissatisfied')
        )

        # Change previous answer button
        if st.button("Change Previous Answer"):
            choose_aspect()
        elif st.button("Next"):
            st.write("Question 3: How effective was the floor repair in solving the issue?")
            option3 = st.radio(
                "Choose an option:",
                ('1 - Very Effective', '2 - Effective', '3 - Neutral', '4 - Ineffective', '5 - Very Ineffective')
            )

            # Change previous answer button
            if st.button("Change Previous Answer"):
                question_floor()
            elif st.button("Next"):
                st.write("Question 4: How often do you experience issues with your floor after the repair?")
                option4 = st.radio(
                    "Choose an option:",
                    ('1 - Never', '2 - Rarely', '3 - Occasionally', '4 - Frequently', '5 - Always')
                )

                if st.button("Change Previous Answer"):
                    question_floor()
                elif st.button("Next"):
                    st.write("Question 5: How likely are you to hire the same contractor for future floor repairs?")
                    option5 = st.radio(
                        "Choose an option:",
                        ('1 - Very Likely', '2 - Likely', '3 - Neutral', '4 - Unlikely', '5 - Very Unlikely')
                    )
                    if st.button("Next"):
                        show_results('Floor', option1, option2, option3, option4, option5)

def question_roof():
    st.write("You chose to analyze: Roof")
    st.write("Question 1: How long has it been since your roof was repaired?")
    option1 = st.radio(
        "Choose an option:",
        ('1 - Very recently', '2 - Within the past year', '3 - 1-3 years ago', '4 - 3-5 years ago', '5 - More than 5 years ago')
    )

    # Next button to move to the next question
    if st.button("Next"):
        st.write("Question 2: How satisfied are you with the quality of the roof repair?")
        option2 = st.radio(
            "Choose an option:",
            ('1 - Very Satisfied', '2 - Satisfied', '3 - Neutral', '4 - Dissatisfied', '5 - Very Dissatisfied')
        )

        # Change previous answer button
        if st.button("Change Previous Answer"):
            choose_aspect()
        elif st.button("Next"):
            st.write("Question 3: How effective was the roof repair in solving the issue?")
            option3 = st.radio(
                "Choose an option:",
                ('1 - Very Effective', '2 - Effective', '3 - Neutral', '4 - Ineffective', '5 - Very Ineffective')
            )

            # Change previous answer button
            if st.button("Change Previous Answer"):
                question_roof()
            elif st.button("Next"):
                st.write("Question 4: How often do you experience issues with your roof after the repair?")
                option4 = st.radio(
                    "Choose an option:",
                    ('1 - Never', '2 - Rarely', '3 - Occasionally', '4 - Frequently', '5 - Always')
                )

                if st.button("Change Previous Answer"):
                    question_roof()
                elif st.button("Next"):
                    st.write("Question 5: How likely are you to hire the same contractor for future roof repairs?")
                    option5 = st.radio(
                        "Choose an option:",
                        ('1 - Very Likely', '2 - Likely', '3 - Neutral', '4 - Unlikely', '5 - Very Unlikely')
                    )
                    if st.button("Next"):
                        show_results('Roof', option1, option2, option3, option4, option5)

def question_wall():
    st.write("You chose to analyze: Wall")
    st.write("Question 1: How long has it been since your wall was repaired?")
    option1 = st.radio(
        "Choose an option:",
        ('1 - Very recently', '2 - Within the past year', '3 - 1-3 years ago', '4 - 3-5 years ago', '5 - More than 5 years ago')
    )

    # Next button to move to the next question
    if st.button("Next"):
        st.write("Question 2: How satisfied are you with the quality of the wall repair?")
        option2 = st.radio(
            "Choose an option:",
            ('1 - Very Satisfied', '2 - Satisfied', '3 - Neutral', '4 - Dissatisfied', '5 - Very Dissatisfied')
        )

        # Change previous answer button
        if st.button("Change Previous Answer"):
            choose_aspect()
        elif st.button("Next"):
            st.write("Question 3: How effective was the wall repair in solving the issue?")
            option3 = st.radio(
                "Choose an option:",
                ('1 - Very Effective', '2 - Effective', '3 - Neutral', '4 - Ineffective', '5 - Very Ineffective')
            )

            # Change previous answer button
            if st.button("Change Previous Answer"):
                question_wall()
            elif st.button("Next"):
                st.write("Question 4: How often do you experience issues with your wall after the repair?")
                option4 = st.radio(
                    "Choose an option:",
                    ('1 - Never', '2 - Rarely', '3 - Occasionally', '4 - Frequently', '5 - Always')
                )

                if st.button("Change Previous Answer"):
                    question_wall()
                elif st.button("Next"):
                    st.write("Question 5: How likely are you to hire the same contractor for future wall repairs?")
                    option5 = st.radio(
                        "Choose an option:",
                        ('1 - Very Likely', '2 - Likely', '3 - Neutral', '4 - Unlikely', '5 - Very Unlikely')
                    )
                    if st.button("Next"):
                        show_results('Wall', option1, option2, option3, option4, option5)

def show_results(chosen_aspect, prev_answer1, prev_answer2, prev_answer3, prev_answer4, prev_answer5):
    st.title("Survey Results")
    st.write(f"Aspect Analyzed: {chosen_aspect}")
    st.write("Question 1: How long has it been since the repair?")
    st.write("Your Answer:", prev_answer1.split('-')[1].strip())

    st.write("Question 2: How satisfied are you with the quality of the repair?")
    st.write("Your Answer:", prev_answer2.split('-')[1].strip())

    st.write("Question 3: How effective was the repair in solving the issue?")
    st.write("Your Answer:", prev_answer3.split('-')[1].strip())

    st.write("Question 4: How often do you experience issues with the repaired aspect?")
    st.write("Your Answer:", prev_answer4.split('-')[1].strip())

    st.write("Question 5: How likely are you to hire the same contractor for future repairs?")
    st.write("Your Answer:", prev_answer5.split('-')[1].strip())

    if st.button("Go to Home Page"):
        main()

if __name__ == "__main__":
    main()
