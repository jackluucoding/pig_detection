# questions.py

questions = [
    {
        # Maps to Sub-Step: "Platform selection"
        # Explanation: This question checks whether the victim met the scammer on a channel commonly used by scammers
        # (dating app, social media, or random text).
        "text": "Did you first meet or connect with this person via a dating app, social media, or a random message?",
        "weight_yes": 10,
        "red_flag": "Unsolicited contact on social/dating app"
    },
    {
        # Maps to Sub-Step: "Approach strategy"
        "text": "Did they claim to have messaged you by accident or use a ‘friendly introduction’ approach (e.g., wrong number)?",
        "weight_yes": 10,
        "red_flag": "Accidental/wrong-number introduction"
    },
    {
        # Maps to Sub-Step: "Profile crafting"
        "text": "Does their profile seem suspiciously polished or use images you suspect might be stolen or fake?",
        "weight_yes": 5,
        "red_flag": "Potentially fake or stolen profile photos"
    },
    {
        # Maps to Sub-Step: "Frequent communication"
        "text": "Have they begun texting/calling you daily, quickly making themselves part of your daily routine?",
        "weight_yes": 10,
        "red_flag": "Excessive communication and emotional reliance"
    },
    # {
    #     # Maps to Sub-Step: "Sharing personal stories"
    #     "text": "Do they frequently share personal stories of success or hardship that seem aimed at winning sympathy or trust?",
    #     "weight_yes": 5,
    #     "red_flag": "Emotional anecdotes to build trust"
    # },
    # {
    #     # Maps to Sub-Step: "Mirroring interests"
    #     "text": "Do they often mirror your interests, hobbies, or values to seem remarkably compatible with you?",
    #     "weight_yes": 5,
    #     "red_flag": "Suspiciously perfect compatibility"
    # },
    # {
    #     # Maps to Sub-Step: "Expressing affection"
    #     "text": "Have they declared affection or romantic feelings unusually quickly, despite limited real-life contact?",
    #     "weight_yes": 10,
    #     "red_flag": "Premature declarations of love"
    # },
    # {
    #     # Maps to Sub-Step: "Casual mention of success"
    #     "text": "Have they casually mentioned significant financial success—especially in crypto or trading—during conversations?",
    #     "weight_yes": 10,
    #     "red_flag": "Boasts of financial success"
    # },
    # {
    #     # Maps to Sub-Step: "Sharing success stories"
    #     "text": "Have they shown screenshots or told stories claiming large profits from an investment or trading platform?",
    #     "weight_yes": 15,
    #     "red_flag": "Evidence of high investment returns"
    # },
    # {
    #     # Maps to Sub-Step: "Promise of financial freedom"
    #     "text": "Have they promised you could quickly achieve financial freedom by following their investment advice?",
    #     "weight_yes": 15,
    #     "red_flag": "Promises of easy wealth"
    # },
    # {
    #     # Maps to Sub-Step: "Initial small investment"
    #     "text": "Did they encourage you to invest a small amount at first, saying it was ‘safe’ or a ‘trial run’?",
    #     "weight_yes": 15,
    #     "red_flag": "Push for initial small investment"
    # },
    # {
    #     # Maps to Sub-Step: "Facilitating early profits"
    #     "text": "After your initial investment, did they show you small profits or allow a quick withdrawal to build your trust?",
    #     "weight_yes": 15,
    #     "red_flag": "Facilitated small profits to gain confidence"
    # },
    # {
    #     # Maps to Sub-Step: "Building confidence"
    #     "text": "Have they repeatedly emphasized how ‘reliable’ or ‘profitable’ the platform is, to boost your confidence?",
    #     "weight_yes": 10,
    #     "red_flag": "Frequent assurances of legitimacy"
    # },
    # {
    #     # Maps to Sub-Step: "Encouraging larger investments"
    #     "text": "Have they been pressuring you to invest a larger sum, claiming urgent or time-sensitive opportunities?",
    #     "weight_yes": 15,
    #     "red_flag": "Pressure to invest bigger amounts"
    # },
    # {
    #     # Maps to Sub-Step: "Leveraging emotional bond"
    #     "text": "Do they use your emotional connection or guilt-trip you into committing more money than you’re comfortable with?",
    #     "weight_yes": 15,
    #     "red_flag": "Emotional manipulation for more funds"
    # },
    # {
    #     # Maps to Sub-Step: "Fake platforms and wallets"
    #     "text": "Have they asked you to use a trading platform or wallet you’ve never heard of (possibly with limited online info)?",
    #     "weight_yes": 15,
    #     "red_flag": "Directing to suspicious platform/wallet"
    # },
    # {
    #     # Maps to Sub-Step: "Withdrawal issues"
    #     "text": "Did you face unexpected fees, taxes, or other obstacles when you tried to withdraw or access your funds?",
    #     "weight_yes": 20,
    #     "red_flag": "Withdrawal blocked by surprise fees/taxes"
    # },
    # {
    #     # Maps to Sub-Step: "Request for additional payments"
    #     "text": "Are they asking you to send additional payments or cryptocurrency to unlock or release your account balance?",
    #     "weight_yes": 20,
    #     "red_flag": "Extra payments to ‘unlock’ funds"
    # },
    {
        # Maps to Sub-Step: "Increasing pressure"
        "text": "Have they used urgent deadlines, legal threats, or other high-pressure tactics to push you to pay more?",
        "weight_yes": 15,
        "red_flag": "Escalating pressure tactics"
    },
    {
        # Maps to Sub-Step: "Ghosting and disappearing"
        "text": "After you questioned them or tried to withdraw your money, did they block or ghost you?",
        "weight_yes": 15,
        "red_flag": "Ghosting after withdrawal attempt"
    },
    {
        # Maps to Sub-Step: "Dismantling accounts"
        "text": "Does their website or platform now appear offline, deactivated, or inaccessible, leaving you no way to recover funds?",
        "weight_yes": 15,
        "red_flag": "Platform vanished after investment"
    }
]

# A helper constant for the maximum possible score
MAX_SCORE = sum(q["weight_yes"] for q in questions)
