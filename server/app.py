from sanic import Sanic
from sanic.response import json
app = Sanic()

@app.route('/read_points', methods = ['POST'])
async def test(request):
#    print(request.body.address)    
    print(request.json)
    return json({'hello': 'world'})

if __name__ == '__main__':
        app.run(port=5000)
