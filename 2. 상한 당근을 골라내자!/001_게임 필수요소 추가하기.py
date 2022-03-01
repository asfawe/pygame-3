import pygame as pg
from pygame.constants import QUIT

pg.init()

화면가로길이, 화면세로길이 = (980, 940)
화면 = pg.display.set_mode([화면가로길이, 화면세로길이])
pg.display.set_caption('상한 당근을 싱싱한 당근으로! By 인피니티 스톤')

# 글꼴설정
글꼴 = pg.font.SysFont('malgungothic', 35)

#이미지초기화

pg.display.update()

while True:
    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            pg.display.quit()