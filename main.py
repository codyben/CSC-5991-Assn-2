# Cody Benkoski
# hk2327@wayne.edu
import random
from flask import Flask, request, jsonify
app = Flask(__name__)
random.seed(5991)
JOKES = (
    {
        "setup": "What do you call a fish with no eyes?",
        "punchline": "A fsh.",
        "comedy_factor": random.randrange(0, 100, step=1) / 100.0
    },
    {
        "setup": "What do you call a can opener that doesn't work?",
        "punchline": "A can't opener!",
        "comedy_factor": random.randrange(0, 100, step=1) / 100.0
    },
    {
        "setup": "Did you hear about the Italian chef who died?",
        "punchline": "He pasta-way",
        "comedy_factor": random.randrange(0, 100, step=1) / 100.0
    },
    {
        "setup": "I sold my vacuum the other day.",
        "punchline": "All it was doing was collecting dust.",
        "comedy_factor": random.randrange(0, 100, step=1) / 100.0
    },
    {
        "setup": "I like elephants.",
        "punchline": "Everything else is irrelephant.",
        "comedy_factor": random.randrange(0, 100, step=1) / 100.0
    },
    {
        "setup": "Two guys walk into a bar.",
        "punchline": "The third guy ducks.",
        "comedy_factor": random.randrange(0, 100, step=1) / 100.0
    },
    {
        "setup": "What do you call a fake noodle?",
        "punchline": "An impasta.",
        "comedy_factor": random.randrange(0, 100, step=1) / 100.0
    },
    {
        "setup": "Why can't a nose be 12 inches long?",
        "punchline": "Because then it'd be a foot.",
        "comedy_factor": random.randrange(0, 100, step=1) / 100.0
    },
    {
        "setup": "The wedding was so beautiful",
        "punchline": "Even the cake was in tiers.",
        "comedy_factor": random.randrange(0, 100, step=1) / 100.0
    },
    {
        "setup": "What do you call a fly with no wings?",
        "punchline": "A walk.",
        "comedy_factor": random.randrange(0, 100, step=1) / 100.0
    }
)

@app.route('/joke', methods=['GET'])
@app.route('/joke/', methods=['GET'])
def joke():
    num_jokes = int(request.args.get("num", 1))
    return jsonify(random.choices(JOKES, k=num_jokes)) # changing this to comply with the "JSON Array" requirement.


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
