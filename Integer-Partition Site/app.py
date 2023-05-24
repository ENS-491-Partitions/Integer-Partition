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

# Example counter functions
def rrcounter(integer, parts):
    # Perform counter logic for roger_ramanujan selection
    return 1

def rrgcounter(integer, parts, distance, max_ones):
    # Perform counter logic for roger_ramanujan_gordon selection
    # ...
    return 1

def capcounter(integer, parts):
    # Perform counter logic for capparelli selection
    # ...
    return 1

# Example generator functions
def rrgenerator(integer, parts):
    # Perform generator logic for roger_ramanujan selection
    return [1]

def rrggenerator(integer, parts, distance, max_ones):
    # Perform generator logic for roger_ramanujan_gordon selection
    for i in range(1,10000000):
        print("")
    return [1]

def capgenerator(integer, parts):
    # Perform generator logic for capparelli selection
    # ...
    return [1]

if __name__ == '__main__':
    app.run(debug=True)
