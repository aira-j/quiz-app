print("👋 welcome to the quiz")
a=input("do you want to start(y/n): ")
if a in "n":
    print("see you next time")

elif a in "y":
    print("🚀 Let's begin")
    name=input("enter your name: ")
    print("hi", name, "let's begin your quiz")
    print("📢 RULES: u get +1 mark for each correct answer and 0 for each wrong or skipped question")
    print("🎯 so lets begin")
    score=0
    q=1
    script= [{"question": "What is the capital of India?", "A": "Mumbai", "B":"Delhi", "C": "Kolkata", "D":"Chennai", "answer": "B"},
           {"question": "Which language is known as the language of the web?", "A": "Python", "B":"C++", "C": "JavaScript", "D":"Java", "answer": "C"},
           {"question": "What does CPU stand for?", "A": "Central Process Unit", "B":"Computer Personal Unit", "C": "Central Processing Unit", "D":"Control Processing Unit", "answer": "C"},
           {"question": "Which planet is known as the Red Planet?", "A": "Mars", "B":"Jupiter", "C": "Saturn", "D":"Venus", "answer": "A"},
           {"question": "Who wrote Mahabharat?", "A": "Kalidas", "B":"Ved Vyas", "C": "Tulsidas", "D":"Valmiki", "answer": "B"}]
    for i in script:
        
        print("question",q, ":" , i["question"])
        print("🔹A: ", i["A"]) 
        print("🔹B: ", i["B"])
        print("🔹C: ", i["C"])
        print("🔹D: ", i["D"])
        ans=input("your answer (A/B/C/D/skip): ")
        if ans.upper() == i["answer"]:
            score+=1
            print("✅ Yay! you got it right")
        elif ans in "skip":
            print("⏭️ let's move to the next question")
        else:
            print("❌ Oops you got it wrong! the correct ans was:", i["answer"])
        q+=1
    
    print(name, "your final score is:", score)
    if score==5:
        print("💯 genius")
    elif score >=3:
        print("👏 well done")
    else:
        print("🤞 try again")
    print("thanks for playing")
        



