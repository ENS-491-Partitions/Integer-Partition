from flask import Flask, render_template, request
import Algos
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selection = request.form['selection']
        algorithm = request.form['algorithm']
        result = None

        if algorithm == 'counter':
            if selection == 'roger_ramanujan':
                print("here")
                integer = int(request.form['integer'])
                num_parts = int(request.form['num_parts'])
                result = Algos.mRogerRG(integer, num_parts, 2, 2)
            elif selection == 'roger_ramanujan_gordon':
                integer = int(request.form['integer'])
                num_parts = int(request.form['num_parts'])
                distance = int(request.form['distance'])
                max_ones = int(request.form['max_ones'])
                result = Algos.mRogerRG(integer, num_parts, distance, max_ones)
            elif selection == 'capparelli':
                integer = int(request.form['integer'])
                num_parts = int(request.form['num_parts'])
                result = Algos.capcounter(integer, num_parts)
        elif algorithm == 'generator':
            if selection == 'roger_ramanujan':
                integer = int(request.form['integer'])
                num_parts = int(request.form['num_parts'])
                result = Algos.ListRRGpartitions(integer, num_parts, 2, 2)
            elif selection == 'roger_ramanujan_gordon':
                integer = int(request.form['integer'])
                num_parts = int(request.form['num_parts'])
                distance = int(request.form['distance'])
                max_ones = int(request.form['max_ones'])
                result = Algos.ListRRGpartitions(integer, num_parts, distance, max_ones)
            elif selection == 'capparelli':
                integer = int(request.form['integer'])
                num_parts = int(request.form['num_parts'])
                result = Algos.capgenerator(integer, num_parts)
        
        counter_output = None
        generator_output = None
        if algorithm == 'counter':
            counter_output = result
        elif algorithm == 'generator':
            generator_output = result
        
        return render_template('index.html', counter_output=counter_output, generator_output=generator_output)

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
