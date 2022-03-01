from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class sponsorList(db.Model):
    word = db.Column(db.String(80),primary_key = True)

    def __repr__(self):
        return f'{self.word}'

@app.route('/api/vocab')
def get_vocab():
    vocab_dict = sponsorList.query.all()
    output =[str(word) for word in vocab_dict]
    return {"vocab" : output }

@app.route('/api/vocab',methods=['POST'])
def post_vocab():
    try:
        for sponsorWord in request.json['vocab']:
            sponsorlst=sponsorList(word=sponsorWord)
            db.session.add(sponsorlst)
            db.session.commit()

        vocab_dict = sponsorList.query.all()
        output =[str(word) for word in vocab_dict]
    except:
        return {"Error":f'UNIQUE constraint failed: {sponsorWord} keyword already present'}
    return {"vocab_post" : output }

@app.route('/api/prediction',methods=['POST'])
def post_text():
    post_text = request.json['post_text']
    text_words = post_text.split()
    output = 'non-sponsored'
    for words in text_words:
        try:
            sponsorlst=sponsorList.query.get_or_404(words)
        except: 
            sponsorlst = None
        if sponsorlst:
            output = 'sponsored'
            break
    return {"vocab" : output }

if __name__=='__main__':
    app.run(debug='True',host='0.0.0.0')