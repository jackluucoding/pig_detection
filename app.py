from flask import Flask, render_template_string, request

app = Flask(__name__)

# Define our questions, their weights, and a short "red flag" description
questions = [
    {
        "id": "q1",
        "text": "Did you meet this person on a social media or dating platform, or via a random unexpected text?",
        "weight_yes": 10,
        "red_flag": "Met on social media/dating app or random text"
    },
    {
        "id": "q2",
        "text": "Does their profile have few photos with limited verifiable information?",
        "weight_yes": 5,
        "red_flag": "Sparse or fake-looking online profile"
    },
    {
        "id": "q3",
        "text": "Have they been texting/calling you daily, quickly building a personal or romantic connection?",
        "weight_yes": 10,
        "red_flag": "Rapid emotional bonding or excessive communication"
    },
    {
        "id": "q4",
        "text": "Have they already professed strong affection or a desire for a serious relationship, despite limited contact?",
        "weight_yes": 10,
        "red_flag": "Unusually fast declarations of love"
    },
    {
        "id": "q5",
        "text": "Have they brought up cryptocurrency or high-return investments, claiming significant personal success?",
        "weight_yes": 15,
        "red_flag": "Promises of quick wealth or success stories"
    },
    {
        "id": "q6",
        "text": "Have they encouraged you to invest a small amount with promises of easy or quick returns?",
        "weight_yes": 15,
        "red_flag": "Push for initial small investment"
    },
    {
        "id": "q7",
        "text": "After seeing small profits, did they pressure you to invest larger amounts or mention urgent 'opportunities'?",
        "weight_yes": 15,
        "red_flag": "Pressure to invest larger sums"
    },
    {
        "id": "q8",
        "text": "Are you hearing about unexpected fees, taxes, or platform requirements before you can withdraw?",
        "weight_yes": 20,
        "red_flag": "Claims of extra fees/taxes blocking withdrawals"
    },
    {
        "id": "q9",
        "text": "Has this person asked you to send more money to 'unlock' or 'release' your investments?",
        "weight_yes": 20,
        "red_flag": "Requests for more payments to access funds"
    },
    {
        "id": "q10",
        "text": "Have they blocked, ghosted, or avoided you when you questioned them or tried to cash out?",
        "weight_yes": 15,
        "red_flag": "Ghosting or sudden silence when discussing withdrawals"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Calculate total score based on user responses
        total_score = 0
        triggered_flags = []
        max_score = sum(q["weight_yes"] for q in questions)

        for q in questions:
            user_response = request.form.get(q["id"])
            if user_response == "yes":
                total_score += q["weight_yes"]
                triggered_flags.append(q["red_flag"])

        # Compute percentage
        risk_percent = (total_score / max_score) * 100

        # Determine risk level (example thresholds)
        if risk_percent <= 30:
            risk_level = "Low Risk"
        elif risk_percent <= 60:
            risk_level = "Moderate Risk"
        elif risk_percent <= 90:
            risk_level = "High Risk"
        else:
            risk_level = "Very High Risk"

        # Display results in a simple HTML template
        results_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Pig Butchering Scam Assessment - Results</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }
                .container {
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                .red-flag {
                    color: #b30000;
                }
                .risk-level {
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Assessment Results</h2>
                <p>Total Score: {{ total_score }} / {{ max_score }} ({{ risk_percent }}%)</p>
                <p class="risk-level">Overall Risk: {{ risk_level }}</p>
                
                {% if triggered_flags %}
                <h4>Red Flags Identified:</h4>
                <ul>
                {% for flag in triggered_flags %}
                    <li class="red-flag">{{ flag }}</li>
                {% endfor %}
                </ul>
                {% else %}
                <p>No major red flags identified based on your answers.</p>
                {% endif %}
                
                <h4>Recommendation</h4>
                {% if risk_level == "High Risk" or risk_level == "Very High Risk" %}
                <p>
                    1. Stop sending money or personal info immediately.<br>
                    2. Verify identity/platform legitimacy.<br>
                    3. Consult a trusted friend or financial professional.<br>
                    4. Consider reporting the incident to authorities.
                </p>
                {% elif risk_level == "Moderate Risk" %}
                <p>
                    1. Exercise caution and independently verify all claims.<br>
                    2. Discuss concerns with a trusted friend or advisor.<br>
                    3. Consider pausing communication until verified.
                </p>
                {% else %}
                <p>Indicators are low, but stay vigilant. Reassess if new red flags appear.</p>
                {% endif %}

                <a href="/">Back to Assessment</a>
            </div>
        </body>
        </html>
        """
        return render_template_string(results_template,
                                      total_score=total_score,
                                      max_score=max_score,
                                      risk_percent=f"{risk_percent:.1f}",
                                      risk_level=risk_level,
                                      triggered_flags=triggered_flags)

    # If GET request, render the question form
    form_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pig Butchering Scam Assessment</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            .question {
                margin-bottom: 15px;
            }
            label {
                display: block;
                margin: 5px 0;
            }
            .submit-btn {
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #008cba;
                color: #fff;
                border: none;
                cursor: pointer;
                border-radius: 5px;
            }
            .submit-btn:hover {
                background-color: #006b95;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Pig Butchering Scam Risk Assessment</h2>
            <p>Please answer each question with "Yes" or "No". Then click "Submit" to see your risk score.</p>
            <form method="POST">
                {% for q in questions %}
                    <div class="question">
                        <p><strong>{{ loop.index }}. {{ q.text }}</strong></p>
                        <label>
                            <input type="radio" name="{{ q.id }}" value="yes" required> Yes
                        </label>
                        <label>
                            <input type="radio" name="{{ q.id }}" value="no"> No
                        </label>
                    </div>
                {% endfor %}
                <button type="submit" class="submit-btn">Submit</button>
            </form>
        </div>
    </body>
    </html>
    """
    return render_template_string(form_template, questions=questions)


if __name__ == "__main__":
    # Run the Flask development server
    # Note: For production, use a production-ready server (Gunicorn, uWSGI, etc.)
    app.run(debug=True, port=5000)
