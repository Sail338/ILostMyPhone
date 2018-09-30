from funk import three_circle
from sanic import Sanic
from sanic.response import json
app = Sanic()
address_map = dict()
q = []
@app.route('/read_points', methods = ['POST'])
async def test(request):
    json_ = request.json    
    #print(request)
    if json_['address'] not in address_map:
        print("not there")
        address_map[json_['address']] = dict()
    tuple_map = address_map[json_['address']]
    id_ = json_['id']
    rssi = json_['rssi']
    if id_  not in tuple_map:
        tuple_map[id_] = rssi
        print(tuple_map)
        if len(tuple_map) == 3:
             a =three_circle.get_user_location_by_response(tuple_map['a'],tuple_map['b'],tuple_map['c'])
             print(a)
             tuple_map = {}
             q_node = {'status':200,'address':json_['address'],'x':a[0],'y':a[1]}
             q.append(q_node)
             address_map[json_['address']] = {}
    return json({"hello": "world"})

@app.route('/send_queue'):
    def popFromQ(request):
        if len(q) > 0:
            return json(q.pop())
        else:
            return json({'status':400})
        




if __name__ == '__main__':
        app.run(port=5000,debug= True)
