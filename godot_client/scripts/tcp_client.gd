extends Node

signal connected
signal data
signal disconnected
signal error

var _status: int=0
var _stream: StreamPeerTCP = StreamPeerTCP.new()
# Called when the node enters the scene tree for the first time.

func _ready() -> void:
	_status = _stream.get_status()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta: float) -> void:
	_stream.poll()
	var new_status: int = _stream.get_status()
	if new_status != _status:
		_status = new_status
		match _status:
			_stream.STATUS_NONE:
				print('Disconnected from host.')
				emit_signal('disconnected')
			_stream.STATUS_CONNECTING:
				print('Connecting to host.')
			_stream.STATUS_CONNECTED:
				print('Connected to host.')
				emit_signal('connected')
			_stream.STATUS_ERROR:
				print("Error with socket stream")
				emit_signal('error')
	if _status == _stream.STATUS_CONNECTED:
		var avaliable_bytes: int = _stream.get_available_bytes()
		if avaliable_bytes > 0:
			print('avaliable bytes: ', avaliable_bytes)
			var data1: Array = _stream.get_partial_data(avaliable_bytes)
			if data1[0] != OK:
				print("Error getting data from stream", data1[0])
				emit_signal('error')
			else:
				emit_signal('data', data1[1])
				
func connect_to_host(host: String , port:int) -> void:
	print("Connecting to %s:%d" % [host,port])
	_status = _stream.STATUS_NONE
	if _stream.connect_to_host(host,port) != OK:
		print('Error connecting to host')
		emit_signal('error')
		
func send(data1: PackedByteArray) -> bool:
	if _status != _stream.STATUS_CONNECTED:
		print('Error: Stream is not currently connected. ')
		return false
	var error1: int = _stream.put_data(data1)
	if error1 != OK:
		print("error writing to stream: ", error1)
		return false
	return true
