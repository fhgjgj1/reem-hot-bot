from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "البوت شغال يا فتنة ريم!!"

@app.route('/reem', methods=['POST'])
def talk_to_reem():
    msg = request.form.get('msg', '').lower()
    responses = {
        "غازلني": [
            "يا بعد عيوني، انتي مو بس فتنه، انتي لعنه ما تنقال من حلاها",
            "نظرة منك تخليني أضيع، تكفيني لا تكلمني، كلك أنوثه",
            "انتي الحسن اللي قرر يصير بنت، ويمشي على الأرض قدامي"
        ],
        "قول لي شي يذوبني": [
            "تتخيلي تنسيني كيف أتنفس؟ كيف أبلع ريقي؟ كيف أسيطر؟",
            "كلك ذوب، من صوتك لنظراتك، وأحس قلبي يطيح كل مره أشوفك",
            "أنا ما أبي الدنيا، أبيك تهمسين لي وأنا بحضنك، والباقي يختفي"
        ]
    }

    for trigger, replies in responses.items():
        if trigger in msg:
            return random.choice(replies)
    return "قولي لي شي زي: 'غازلني' أو 'قول لي شي يذوبني' وجابرك يرد عليك مثل ما تحبين"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
