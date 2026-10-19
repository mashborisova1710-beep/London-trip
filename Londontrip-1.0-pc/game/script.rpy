define n = Character("Situation")
define s = Character("Staff")
define g = Character("Security Guard")

# Load Images with scaling
image airport = im.Scale("airport_bg.jpg", 1920, 1080)
image staff = im.FactorScale("staff.png", 2.0)
image security_guard = im.FactorScale("security_guard.png", 2.0)

# Start with 0 mistakes
default mistakes = 0

label start:
    play music "Do You Think We Could Ever Imagine.mp3"
    $ mistakes = 0
    scene airport
    n "You have arrived in London. You need to go through passport control and check-in. Answer 10 questions. You can make only 2 mistakes!"
    jump q1

# === QUESTION 1 ===
label q1:
    scene airport
    show staff at right, 
    s "Good morning! Can I see your passport, please?"
    menu:
        "Here you are.":
            jump q1_ok
        "I am fine, thank you.":
            $ mistakes += 1
            jump wrong_answer_q1
        "Yes, I have a bag.":
            $ mistakes += 1
            jump wrong_answer_q1
        "Where is the toilet?":
            $ mistakes += 1
            jump wrong_answer_q1

label wrong_answer_q1:
    if mistakes >= 3:
        jump failed
    else:
        n "The officer didn't understand. Try again! (Mistakes: [mistakes]/2)"
        jump q1

label q1_ok:
    s "Thank you. And what is the purpose of your visit?"
    jump q2

# === QUESTION 2 ===
label q2:
    menu:
        "I want to eat.":
            $ mistakes += 1
            jump wrong_answer_q2
        "Tourism. I am on holiday.":
            jump q2_ok
        "Because I like it.":
            $ mistakes += 1
            jump wrong_answer_q2
        "My name is John.":
            $ mistakes += 1
            jump wrong_answer_q2

label wrong_answer_q2:
    if mistakes >= 3:
        jump failed
    else:
        n "Error! This is not an answer about the purpose of your visit. Try again. (Mistakes: [mistakes]/2)"
        jump q2

label q2_ok:
    s "Great! How long are you staying?"
    jump q3

# === QUESTION 3 ===
label q3:
    menu:
        "I am from Russia.":
            $ mistakes += 1
            jump wrong_answer_q3
        "Yes, I am.":
            $ mistakes += 1
            jump wrong_answer_q3
        "By plane.":
            $ mistakes += 1
            jump wrong_answer_q3
        "For two weeks.":
            jump q3_ok

label wrong_answer_q3:
    if mistakes >= 3:
        jump failed
    else:
        n "Error! You were asked about the time. Try again. (Mistakes: [mistakes]/2)"
        jump q3

label q3_ok:
    s "Perfect. Where are you going to stay?"
    jump q4

# === QUESTION 4 ===
label q4:
    menu:
        "At the airport.":
            $ mistakes += 1
            jump wrong_answer_q4
        "In a hotel in the city center.":
            jump q4_ok
        "Yesterday.":
            $ mistakes += 1
            jump wrong_answer_q4
        "I have two bags.":
            $ mistakes += 1
            jump wrong_answer_q4

label wrong_answer_q4:
    if mistakes >= 3:
        jump failed
    else:
        n "Error! The question was about your accommodation. Try again. (Mistakes: [mistakes]/2)"
        jump q4

label q4_ok:
    s "Good. Now go to the baggage claim. Next!"
    hide staff
    n "You passed passport control. But that's not all. You are going to collect your baggage."
    jump q5

# === QUESTION 5 ===
label q5:
    n "You have lost your bag and approach the information desk."
    show security_guard at right, 
    s "Hello! How can I help you?"
    menu:
        "Where is my luggage? I can't find it.":
            jump q5_ok
        "Give me my bag.":
            $ mistakes += 1
            jump wrong_answer_q5
        "Hello! Goodbye!":
            $ mistakes += 1
            jump wrong_answer_q5
        "I don't have a ticket.":
            $ mistakes += 1
            jump wrong_answer_q5

label wrong_answer_q5:
    if mistakes >= 3:
        jump failed
    else:
        n "The staff member didn't understand. Politely explain the problem. (Mistakes: [mistakes]/2)"
        jump q5

label q5_ok:
    s "I see. What does your bag look like?"
    jump q6

# === QUESTION 6 ===
label q6:
    menu:
        "It is very heavy.":
            $ mistakes += 1
            jump wrong_answer_q6
        "It is a large black suitcase.":
            jump q6_ok
        "I bought it yesterday.":
            $ mistakes += 1
            jump wrong_answer_q6
        "It is mine.":
            $ mistakes += 1
            jump wrong_answer_q6

label wrong_answer_q6:
    if mistakes >= 3:
        jump failed
    else:
        n "Error! You need to describe the appearance (color, size). Try again. (Mistakes: [mistakes]/2)"
        jump q6

label q6_ok:
    s "Okay. I will check. Please wait."
    hide security_guard
    n "You found your bag! Now you need to check in for your flight."
    jump q7

# === QUESTION 7 ===
label q7:
    # Здесь можно добавить показ другого персонажа, если он есть
    show staff at right, 
    s "Good afternoon. Where are you flying to today?"
    menu:
        "Flight SU123.":
            $ mistakes += 1
            jump wrong_answer_q7
        "I fly today.":
            $ mistakes += 1
            jump wrong_answer_q7
        "I am flying to London.":
            jump q7_ok
        "No, thank you.":
            $ mistakes += 1
            jump wrong_answer_q7

label wrong_answer_q7:
    if mistakes >= 3:
        jump failed
    else:
        n "Error! You were asked about your destination and flight number. Try again. (Mistakes: [mistakes]/2)"
        jump q7

label q7_ok:
    s "Thank you. How many bags are you checking in?"
    jump q8

# === QUESTION 8 ===
label q8:
    menu:
        "Just one suitcase, please.":
            jump q8_ok
        "I have a lot.":
            $ mistakes += 1
            jump wrong_answer_q8
        "Yes, I am.":
            $ mistakes += 1
            jump wrong_answer_q8
        "No, I don't like bags.":
            $ mistakes += 1
            jump wrong_answer_q8

label wrong_answer_q8:
    if mistakes >= 3:
        jump failed
    else:
        n "Error! You need to name the quantity. Try again. (Mistakes: [mistakes]/2)"
        jump q8

label q8_ok:
    s "Okay. Would you like a window or an aisle seat?"
    jump q9

# === QUESTION 9 ===
label q9:
    menu:
        "Yes, I would.":
            $ mistakes += 1
            jump wrong_answer_q9
        "A window seat, please.":
            jump q9_ok
        "I don't have a window.":
            $ mistakes += 1
            jump wrong_answer_q9
        "The plane is big.":
            $ mistakes += 1
            jump wrong_answer_q9

label wrong_answer_q9:
    if mistakes >= 3:
        jump failed
    else:
        n "Error! You were asked about your seat preference. Try again. (Mistakes: [mistakes]/2)"
        jump q9

label q9_ok:
    s "Here is your boarding pass. Have a nice flight!"
    hide staff
    n "You have checked in. One last step."
    jump q10

# === QUESTION 10 ===
label q10:
    n "You are looking for your boarding gate. You ask a security guard."
    # Внимание: Здесь опять появляется staff, хотя это охранник.
    # Если для охранника есть отдельная картинка, замените staff на нее.
    show security_guard at right, 
    s "Yes? Can I help you?"
    menu:
        "Where is gate 12?":
            jump q10_ok
        "I want to fly.":
            $ mistakes += 1
            jump wrong_answer_q10
        "Where is my plane?":
            $ mistakes += 1
            jump wrong_answer_q10
        "Give me a ticket.":
            $ mistakes += 1
            jump wrong_answer_q10

label wrong_answer_q10:
    if mistakes >= 3:
        jump failed
    else:
        n "Error! Ask about the specific gate. Try again. (Mistakes: [mistakes]/2)"
        jump q10

label q10_ok:
    s "Go straight and turn left. It's over there."
    hide security_guard
    n "You found your gate and boarded the plane. Victory! You successfully passed the airport!"
    jump win

# === WIN ===
label win:
    scene airport
    n "🎉 Level 'Airport' completed! You did a great job."
    menu:
        "What's next?"
        "Play again":
            jump start
        "Exit":
            return

# === FAILED ===
label failed:
    scene airport
    hide staff
    n "❌ FAILED. You made 3 mistakes and couldn't pass the airport control."
    menu:
        "What's next?"
        "Try again from the beginning":
            jump start
        "Exit":
            return
