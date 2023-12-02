from flask import Flask, render_template
import os
import datetime


from cassini.saturn_printer import SaturnPrinter

app = Flask(__name__)


@app.route('/')
def home():
    # Get the printer data
    printer = SaturnPrinter.find_printers(broadcast=None)[0]
    attrs = printer.desc['Data']['Attributes']
    status = printer.desc['Data']['Status']
    print_info = status['PrintInfo']
    file_info = status['FileTransferInfo']
    totalTime = datetime.timedelta(seconds=datetime.timedelta(milliseconds= print_info['TotalTicks']).seconds)
    currentTime = datetime.timedelta(seconds=datetime.timedelta(milliseconds = print_info['CurrentTicks']).seconds)
    return render_template('index.html', printer=printer, attrs=attrs, status=status, print_info=print_info, file_info=file_info, currentTime=currentTime,totalTime=totalTime)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)