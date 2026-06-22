from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store RSVPs (in-memory storage)
rsvps = []

@app.route('/')
def event_page():
    return render_template('event.html')

@app.route('/rsvp', methods=['POST'])
def rsvp():
    name = request.form.get('name')
    email = request.form.get('email')
    
    if name and email:
        rsvps.append({'name': name, 'email': email})
        return render_template('thank_you.html', name=name)
    
    return redirect(url_for('event_page'))

if __name__ == '__main__':
    app.run(debug=True)
