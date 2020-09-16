#!/usr/bin/env python

import i2c_lcd_driver
from time import sleep
from flask import Flask, jsonify, make_response, request, render_template
from datetime import datetime
mylcd = i2c_lcd_driver.lcd()

app = Flask(__name__)
#app.config['SERVER_NAME']= 'caroline.local'

def currentTime():
    dateraw=datetime.now()
    timeFormat=dateraw.strftime("%-I:%M %p")
    return timeFormat
    
def switchAvailable() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Status:Available", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)

def switchBusy() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Status: Busy", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchAway() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Status: Away", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchMeeting() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("In a meeting", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchPhone() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("On the phone", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchField() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("In the field", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchRemote() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Working Remotely", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchLunch() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("At Lunch", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)

def switchDoctor() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Doctors Office", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)

def switchDentist() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Dentist Office", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)
    
def switchClear() :
    mylcd.lcd_clear()
    sleep(1)

# API switchAvailable
@app.route('/api/available', methods=['GET'])
def apiavailable() :
    switchAvailable()
    return jsonify({})
    
# API Busy
@app.route('/api/busy', methods=['GET'])
def apiBusy() :
    switchBusy()
    return jsonify({})
    
# API Away
@app.route('/api/away', methods=['GET'])
def apiAway() :
    switchAway()
    return jsonify({})
    
# API switchMeeting
@app.route('/api/meeting', methods=['GET'])
def apiMeeting() :
    switchMeeting()
    return jsonify({})
    
# API switchPhone
@app.route('/api/phone', methods=['GET'])
def apiPhone() :
    global globalLastCalledApi
    globalLastCalledApi = '/api/Phone'
    switchPhone()
    return jsonify({})
    
# API switchField
@app.route('/api/field', methods=['GET'])
def apiField() :
    switchField()
    return jsonify({})
    
# API switchRemote
@app.route('/api/remote', methods=['GET'])
def apiRemote() :
    switchRemote()
    return jsonify({})
    
# API switchLunch
@app.route('/api/lunch', methods=['GET'])
def apiLunch() :
    switchLunch()
    return jsonify({})

# API switchDoctor
@app.route('/api/doctor', methods=['GET'])
def apiDoctor() :
    switchDoctor()
    return jsonify({})

# API switchDentist
@app.route('/api/dentist', methods=['GET'])
def apiDentist() :
    switchDentist()
    return jsonify({})
    
# API clear
@app.route('/api/clear', methods=['GET'])
def apiClear() :
    switchClear()
    return jsonify({})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    
@app.route('/')
def index():
    #url_for('html', filename='lcd.html')
    return render_template('lcd.html')
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='10.0.90.175')
    #app.run(host='10.0.0.113')
