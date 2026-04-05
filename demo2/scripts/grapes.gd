extends Area2D
@onready var k_animation_player = $AnimationPlayer
func _on_body_entered(body: Node2D) -> void:
		print('+1 key')
		LevelInfo.nkey +=1
		k_animation_player.play("key_pickup")



func _on_keyl2_2_ready() -> void:
	if LevelInfo.target != 'K':
		queue_free()
