from flask import Flask, render_template, request

app = Flask(__name__)

# =========================
# Smart Rule-Based AI Engine
# =========================
def get_ai_response(question):
    q = question.lower()

    intro = "Sure! Let me explain this clearly step-by-step:\n\n"

    # MINIMUM AGE (NEW)
    if "minimum age" in q or "age to vote" in q:
        return intro + """🎂 MINIMUM AGE REQUIREMENT

✔ The minimum age to vote in India is **18 years**

- You must have completed 18 years
- You must be registered in voter list

✔ This rule is defined by law and strictly followed
"""

    # VOTER REGISTRATION
    elif any(word in q for word in ["register", "voter id", "enroll"]):
        return intro + """🪪 VOTER REGISTRATION PROCESS

1. Visit Official Portal  
2. Fill Form 6  
3. Submit ID + Address Proof  
4. Verification by officer  
5. Voter ID issued  

⏱ Time: 2–4 weeks
"""

    # ELECTION PROCESS
    elif "election process" in q or ("process" in q and "election" in q):
        return intro + """🗳 COMPLETE ELECTION PROCESS

1. Election Announcement  
2. Nomination  
3. Scrutiny  
4. Campaigning  
5. Polling  
6. Counting  
7. Result Declaration  
"""

    # POLLING
    elif any(word in q for word in ["vote", "polling", "how to vote"]):
        return intro + """🗳 HOW TO VOTE

1. Visit polling booth  
2. Show ID proof  
3. Finger ink marking  
4. Use EVM  
5. Confirm via VVPAT  
"""

    # EVM
    elif "evm" in q or "vvpat" in q:
        return intro + """🖥 EVM & VVPAT

- EVM records votes electronically  
- VVPAT shows slip for verification  

✔ Secure and accurate system
"""

    # ELIGIBILITY INFO
    elif any(word in q for word in ["eligibility", "who can vote"]):
        return intro + """👤 WHO CAN VOTE?

✔ 18+ years  
✔ Indian citizen  
✔ Registered voter  

❌ Not allowed if:
- Not registered  
- Disqualified  
"""

    # DOCUMENTS
    elif any(word in q for word in ["document", "documents", "id proof"]):
        return intro + """📄 DOCUMENTS REQUIRED

For Voting:
- Voter ID OR Aadhaar / Passport / Driving License

✔ Must carry original ID  
✔ Name must be in voter list  
"""

    # DEFAULT
    else:
        return """Ask about:
- voter registration  
- election process  
- voting  
- documents  
- eligibility  
- minimum age  
"""


# =========================
# Voter Eligibility Checker
# =========================
def check_eligibility(age, citizen):
    try:
        age = int(age)
    except:
        return "❌ Please enter a valid age"

    if age < 18:
        return "❌ You are NOT eligible to vote (must be 18+)"

    if citizen.lower() != "yes":
        return "❌ Only Indian citizens can vote"

    return "✅ You are ELIGIBLE to vote 🎉"


# =========================
# Flask Route
# =========================
@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    question = ""
    eligibility_result = ""

    if request.method == "POST":

        # Normal AI question
        if "question" in request.form:
            question = request.form.get("question")
            if question:
                answer = get_ai_response(question)

        # Eligibility checker
        if "age" in request.form:
            age = request.form.get("age")
            citizen = request.form.get("citizen")
            eligibility_result = check_eligibility(age, citizen)

    return render_template(
        "index.html",
        answer=answer,
        question=question,
        eligibility_result=eligibility_result
    )


# =========================
# Run App
# =========================
if __name__ == "__main__":
    app.run(debug=True)