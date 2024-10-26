import pygame, sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
pygame.display.set_caption("공유학교 첫 시간 ")
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
img_bg = pygame.image.load("image\pg_bg.png")       # 160*360
img_chara = [
    pygame.image.load("image\pg_chara0.png"),       # 192*96
    pygame.image.load("image\pg_chara1.png")        # 192*96
]

tmr = 0
pl_x = 224
pl_y = 160


# 게임 루프 
while True:
    tmr += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN)
            if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                screen = pygame.display.set_mode((640, 360))

    x = tmr % 160
    key = pygame.key.get_pressed()
    
    # 오른쪽으로 이동
    if key[pygame.K_d]:
        pl_x += 20
        # 경계 검사 및 캐릭터 위치 재설정
        if pl_x > 640:  # 오른쪽 경계를 넘어갔을 때
            pl_x = -192  # 왼쪽에서 다시 등장
    # 왼쪽으로 이동
    if key[pygame.K_a]:
        pl_x -= 20  # x축에서 위치를 감소시킵니다
        if pl_x < -192:  # 왼쪽 경계를 넘어갔을 때
            pl_x = 640  # 오른쪽에서 다시 등장

    # 배경 그리기
    for i in range(5): 
        screen.blit(img_bg, [i * 160 - x, 0])           # 배경이미지 표시
    screen.blit(img_chara[tmr % 2], [pl_x, pl_y])  # 캐릭터 위치 업데이트
    pygame.display.update()
    clock.tick(5)
