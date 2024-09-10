from flask import Flask, render_template, request

app = Flask(__name__)

def needs_treatment(data):
    return (
        (data['Screen_time'] in ['5-6 hours', '6+ hours']) or
        (data['AnxietyAboutMissingUpdates'] == 'Often') or
        (data['DifficultyStopping'] == 'Often') or
        (data['StressAnxietyAfterUse'] == 'Often') or
        (data['FrequencyOfSadness'] == 'Often') or
        (data['TroubleSleeping'] == 'Often') or
        (data['FeelingIsolated'] == 'Often') or
        (data['ComparisonToOthers'] == 'Often')
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            'Screen_time': request.form.get('screen_time'),
            'AnxietyAboutMissingUpdates': request.form.get('anxiety_about_missing_updates'),
            'DifficultyStopping': request.form.get('difficulty_stopping'),
            'StressAnxietyAfterUse': request.form.get('stress_anxiety_after_use'),
            'FrequencyOfSadness': request.form.get('frequency_of_sadness'),
            'TroubleSleeping': request.form.get('trouble_sleeping'),
            'FeelingIsolated': request.form.get('feeling_isolated'),
            'ComparisonToOthers': request.form.get('comparison_to_others')
        }
        result = needs_treatment(data)
        return render_template('result.html', result=result, data=data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
