extends Node

const HOST: String = "127.0.0.1"
const PORT: int = 5000
const RECONNECT_TIMEOUT: float = 3.0
const Client = preload("res://scripts/tcp_client.gd")
var _client: Client = Client.new()
signal sendData

func _ready() -> void:
	_client.connected.connect(_handle_client_connected)
	_client.disconnected.connect(_handle_client_disconnected)
	_client.error.connect(_handle_client_error)
	_client.data.connect(_handle_client_data)
	add_child(_client)
	_client.connect_to_host(HOST, PORT)
	self.sendData.connect(sendPredictData)
	
func _connect_after_timeout(timeout: float) -> void:
	await get_tree().create_timer(timeout).timeout # Delay for timeout
	_client.connect_to_host(HOST, PORT)
	
func _handle_client_connected() -> void:
	print("Client connected to server.")
	#var message:PackedByteArray = "6,9,13,23,0,5,8,6,10".to_utf8_buffer()
	#print("Data send : ",message.get_string_from_utf8())
	#_client.send(message)
	
func _handle_client_data(data: PackedByteArray) -> void:
	var msg =  data.get_string_from_utf8()
	LevelInfo.target= msg[2]
	print("Client data : ", msg, "Prediction : ",LevelInfo.target)
	get_tree().change_scene_to_file("res://scenes/game_lvl_1_dup.tscn")
	
	
func _handle_client_disconnected() -> void:
	print("Client disconnected from server.")
	_connect_after_timeout(RECONNECT_TIMEOUT) # Try to reconnect after 3 seconds
	
func _handle_client_error() -> void:
	print("Client error.")
	_connect_after_timeout(RECONNECT_TIMEOUT) # Try to reconnect after 3 seconds
	
func  sendPredictData()->void:
	var msg=str(LevelInfo.nPowerup)+","+str(LevelInfo.nCoins)+","+str(LevelInfo.nkey)
	var message:PackedByteArray = msg.to_utf8_buffer()
	print("Data send : ",msg)
	_client.send(message)
