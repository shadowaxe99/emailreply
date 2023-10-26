```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(String(50), nullable=False)
    feedback = Column(Text, nullable=False)

@app.route('/feedback', methods=['POST'])
def provideFeedback():
    user_id = request.json['user_id']
    feedback = request.json['feedback']
    new_feedback = Feedback(user_id=user_id, feedback=feedback)
    db.session.add(new_feedback)
    db.session.commit()
    return jsonify({"message": "Feedback received"}), 201

@app.route('/feedback/<user_id>', methods=['GET'])
def getFeedback(user_id):
    feedback = Feedback.query.filter_by(user_id=user_id).all()
    return jsonify([f.feedback for f in feedback])

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```