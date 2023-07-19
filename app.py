from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        user_input = request.form['input']
        recommendations = recommendation_engine(user_input)
        return render_template('recommendations.html', recommendations=recommendations)
    
    else:
        return "This route only accepts POST requests."


from recommendation_script import recommend_cities

def recommendation_engine(user_input):
    
    recommendations = recommend_cities(user_input) 
    
    return recommendations

@app.route('/city/<city_name>')
def city_page(city_name):
    
    city_file_path = f"city_pages/{city_name}.html"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
