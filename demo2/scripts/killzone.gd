extends Area2D
@onready var game_level_1: Node = $".."
@onready var killzone: Area2D = $"."

func _on_body_entered(_body: Node2D) -> void:
	print('You died')
	game_level_1.emit_signal("sendData")
	#get_tree().reload_current_scene()
	print("Coins collected is ",LevelInfo.nCoins)
	print("Powerups collected is ",LevelInfo.nPowerup)
	print("Keys collected is ",LevelInfo.nkey)
	print("Prediction ",LevelInfo.target)
	#get_tree().change_scene_to_file("res://scenes/game_lvl_1_dup.tscn")
	
