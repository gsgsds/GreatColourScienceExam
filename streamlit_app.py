import streamlit as st


def get_score(selection):
    # A selection is a tuple of a score and another tuple
    # for example: (('Geography', 'Latin', 'Music', 'French'), 24) returns 24
    return selection[1]


scores = {
    "Art": 0,
    "Economics": 0,
    "French": 0,
    "Geography": 0,
    "German": 0,
    "History": 0,
    "Latin": 0,
    "Music": 0,
    "Technology": 0
}

choice1 = ["French", "German"]

choice2 = ["Art", "Economics", "French", "Geography"]

choice3 = ["Art", "Geography", "History", "Technology", "Music", "Economics"]

choice4 = ["Economics", "History", "Music", "Technology", "Latin"]

all_choices = [choice1, choice2, choice3, choice4]

# Press the green button in the gutter to run the script.
def main():

    for subject in scores.keys():
        score1 = int(st.text_input("From a scale of 0 to 5, How much do you like " + subject + "?:\n"))
        while score1 < 0 or score1 > 5:
            score1 = int(st.text_input("Please input a value between 0 and 5:\n"))

        if subject == "Economics":
            score2 = score1
        else:
            score2 = int(st.text_input("From a scale of 0 to 5, what is your average mark in " + subject + "?:\n"))
            while score2 < 0 or score2 > 5:
                score2 = int(st.text_input("Please input a value between 0 and 5:\n"))
        scores[subject] = score1 + score2

    all_selections = set()

    for subject1 in choice1:
        for subject2 in choice2:
            if subject1 == subject2:
                continue
            else:
                for subject3 in choice3:
                    if subject3 == subject2 or subject3 == subject1:
                        continue
                    else:
                        for subject4 in choice4:
                            if subject4 == subject3 or subject4 == subject2 or subject4 == subject1:
                                continue
                            else:
                                selection = tuple(sorted([subject1, subject2, subject3, subject4]))
                                has_humanity = 'Geography' in selection or 'History' in selection
                                if selection in all_selections or not has_humanity:
                                    continue
                                else:
                                    # at this point, selection is valid so we calculate total score
                                    total_score = scores[subject1] + scores[subject2] + scores[subject3] + scores[subject4]
                                    all_selections.add((selection, total_score))

    all_selections = list(all_selections)
    all_selections.sort(key=get_score, reverse=True)

    st.write('Your top 5 choices are:')
    for idx in range(5):
        selection = all_selections[idx]
        st.write('(' + str(idx+1) + ') ' + ', '.join(selection[0]) + ', with a score of ' + str(selection[1]) + '.')

    pass


st.title("GCSE Options Optimiser")
main()
