capital_map = {
"Montgomery": "Alabama",
"Juneau": "Alaska",
"Phoenix": "Arizona",
"Little Rock": "Arkansas",
"Sacramento": "California",
"Denver": "Colorado",
"Hartford": "Connecticut",
"Dover": "Delaware",
"Tallahassee": "Florida",
"Atlanta": "Georgia",
"Honolulu": "Hawaii",
"Boise": "Idaho",
"Springfield": "Illinois",
"Indianapolis": "Indiana",
"Des Moines": "Iowa",
"Topeka": "Kansas",
"Frankfort": "Kentucky",
"Baton Rouge": "Louisiana",
"Augusta": "Maine",
"Annapolis": "Maryland",
"Boston": "Massachusetts",
"Lansing": "Michigan",
"St. Paul": "Minnesota",
"Jackson": "Mississippi",
"Jefferson City": "Missouri",
"Helena": "Montana",
"Lincoln": "Nebraska",
"Carson City": "Nevada",
"Concord": "New Hampshire",
"Trenton": "New Jersey",
"Santa Fe": "New Mexico",
"Albany": "New York",
"Raleigh": "North Carolina",
"Bismarck": "North Dakota",
"Columbus": "Ohio",
"Oklahoma City": "Oklahoma",
"Salem": "Oregon",
"Harrisburg": "Pennsylvania",
"Providence": "Rhode Island",
"Columbia": "South Carolina",
"Pierre": "South Dakota",
"Nashville": "Tennessee",
"Austin": "Texas",
"Salt Lake City": "Utah",
"Montpelier": "Vermont",
"Richmond": "Virginia",
"Olympia": "Washington",
"Charleston": "West Virginia",
"Madison": "Wisconsin",
"Cheyenne": "Wyoming"
}

state_map = {v: k for k, v in capital_map.items()}

import random;

states = list(state_map.keys())
total_states = len(states)
capitals = list(capital_map.keys())
user_input = ""

while len(states) != 0:
    state_dice = random.randint(0, len(states)-1)
    state = states[state_dice];
    capital = state_map[state]
    correct_answer = random.randint(1, 4)
    j = 1
    choices = []
    while j <= 4:
        if correct_answer == j:
            choices.append(capital)
        else:
            while True:
                wrong_dice = random.randint(0, len(capitals)-1)
                wrong = capitals[wrong_dice]
                if wrong not in choices:
                    if wrong != capital:
                        choices.append(wrong)
                        break;
        j += 1

    print("Capital Quizzer -- Completed {} out of {}".format(
        total_states - len(states), total_states))
    print("What is the state capital of {}?".format(state))
    print("1. " + choices[0])
    print("2. " + choices[1])
    print("3. " + choices[2])
    print("4. " + choices[3])
    print("Pick 1, 2, 3, 4, or q to quit:")
    selection = -1
    while selection != correct_answer:
        user_input = input("> ")
        if user_input not in '1234qQ':
            print("Invalid.... Pick again")
        else:
            if user_input in 'qQ':
                break;
            else:
                selection = int(user_input)
                if selection == correct_answer:
                    print("Correct... Great job")
                    states.remove(state)
                else:
                    print("Wrong... Pick again")
    if user_input in 'qQ':
        break;
print("You correctly guessed {} state capitals".format(total_states - len(states)))

