from flask import Flask, render_template
import os

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    current_reports = {}

    report_directories = ['/home/sean_dev/dev/dra/logs', '/home/sean_dev/dev/AutoDev/logs/']
    
    for dir_path in report_directories:
        for filename in os.listdir(dir_path):
            if filename.endswith(".log"):
                with open(f"{dir_path}/{filename}", 'r') as f:
                    content = f.read()
                    current_reports[filename] = content
    
    return render_template('index.html', reports=current_reports)

if __name__ == '__main__':
    app.run(debug=True)
