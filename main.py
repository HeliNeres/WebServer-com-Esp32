from machine import Pin, PWM
import uasyncio
from microdot_asyncio import Microdot, Response
from microdot_utemplate import render_template

led = Pin(2, Pin.OUT)
ledpwm = PWM(led)
ledpwm.freq(5000)
ledpwm.duty(0)

app = Microdot()
Response.default_content_type = 'text/html'

@app.route('/')
async def hello(request):
    return render_template('index.html')#, led_value = str(ledpwm.duty()))

@app.route('/liga')
async def ligar(request):
    ledpwm.duty(1023)
    return "ligado"

@app.route('/desliga')
async def desligar(request):
    ledpwm.duty(0)
    return "desligado"

@app.post('/slider')
async def slider(request):
    ledpwm.duty(int(str(request.body,'utf-8')))
    return "slider"

def start_server():
    print('Starting microdot app')
    try:
        app.run(port=80)
    except:
        app.shutdown()
        
# Start the server right away
start_server()