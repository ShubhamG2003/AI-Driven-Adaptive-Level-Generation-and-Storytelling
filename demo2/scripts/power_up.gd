extends Area2D
@onready var p_animation_player = $AnimationPlayer
func _on_body_entered(_body: Node2D) -> void:
	print('+1 powerup')
	LevelInfo.nPowerup +=1
	p_animation_player.play("power_pickup")



func _on_powerupl2_2_ready() -> void:
	if LevelInfo.target != 'P':
		queue_free()
