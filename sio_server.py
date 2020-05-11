import socketio
from aiohttp import web

sio = socketio.AsyncServer(cors_allowed_origins='*')

app = web.Application()
app.add_routes([web.static('/model-viewer/', 'model-viewer/')])
sio.attach(app)

m = None
m2 = None
f = None

@sio.event
def connect(sid, environ):
	print('connect ', sid)


@sio.event
def disconnect(sid):
	print('disconnect ', sid)


@sio.event
def model(sid):
	global m
	print('model connected', sid)
	m = sid


@sio.event
def model2(sid):
	global m2
	print('model2 connected', sid)
	m2 = sid


@sio.event
def front(sid):
	global f
	print('front connected', sid)
	f = sid


@sio.event
async def transmit(sid, data):
	# print('transmit', sid)
	# print('data', data)
	if m2 is not None and 'm2' in data.keys():
		await sio.emit('predict', {'m2': data['m2']}, to=m2)
		data.pop('m2')

	if f is not None:
		await sio.emit('transmit', data, to=f)


@sio.event
async def predictions(sid, data):
	print('predictions', sid)
	if m is not None:
		await sio.emit('predictions', data, to=m)
	if f is not None:
		await sio.emit('predictions', data, to=f)


if __name__ == '__main__':
	web.run_app(app)
