import pygame
from settings import Settings
import sys

def run_game():
	# 初始化pygame，屏幕，设置

	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	while True:
		screen.fill(ai_settings.bg_color)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		pygame.display.flip()

run_game()