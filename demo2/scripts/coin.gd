extends Area2D

@onready var animation_player = $AnimationPlayer
func _on_body_entered(_body: Node2D) -> void:
	print('+1 coin')
	LevelInfo.nCoins +=1
	animation_player.play("pickup_animation")
	



func _on_coinl2_2_ready() -> void:
	if LevelInfo.target != 'C':
		queue_free()
