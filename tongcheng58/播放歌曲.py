import pygame
import time
t=100
music_path=r"D:\Documents\Downloads\滨崎步 - myall.mp3"
pygame.mixer.init()

pygame.mixer.music.load(music_path)
pygame.mixer.music.play()  
time.sleep(t)
pygame.mixer.music.stop()

print('已经播放%d秒'%t)
