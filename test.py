# 셋업
import os, pygame, sys, random, time
from pygame.locals import *

# 현재 파일의 디렉토리로 작업 디렉토리 설정
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()  # Pygame 초기화
clock = pygame.time.Clock()  # 프레임 속도를 조절하기 위한 Clock 객체 생성
pygame.display.set_caption("우주 전쟁")  # 윈도우 제목 설정
screen = pygame.display.set_mode((640, 650))  # 게임 화면 크기 설정

# 적군 이미지 로드 및 변환
badguy_image = pygame.image.load("image/badguy.png").convert()  # 70x45 크기의 이미지
badguy_image.set_colorkey((0,0,0)) # 특정색(검은색)을 투명하게

fighter_image = pygame.image.load("image/fighter.png").convert()   # 100 * 59 
fighter_image.set_colorkey((255,255,255))

missile_image = pygame.image.load("image\missile.png").convert()
missile_image.set_colorkey((255,255,255))


last_badguys_time = 0        # 악당이 마지막에 나온 시각을 기록 
last_missile_spawn_time = 0  # 미사일이 마지막에 나온 시각을 기록


# 클래스 정의
class Badguy:
    def __init__(self):  # 초기화 메서드
        self.x = random.randint(0, 570)  # 적군의 x 위치를 랜덤으로 설정 (화면 내에서)
        self.y = -100  
        self.dy = random.randint(2,6)               # 떨어지는 속도
        self.dx = random.choice((-1,1))*self.dy     # 방향

    def move(self):  # 적군의 움직임 메서드
        if self.x < 0 or self.x > 570 :
            self.dx = (self.dx)*(-1) # self.dx *=-1
        self.x += self.dx
        self.dy += 0.2
        self.y +=self.dy

    def draw(self):  # 적군을 그리는 메서드
        screen.blit(badguy_image, (self.x, self.y))  # 적군 이미지를 현재 위치에 그리기
    def off_screen(self):
        return self.y > 640 
class Fighter :
    def __init__(self) :
        self.x = 320
    def move(self) :
        if pressed_keys[K_LEFT] and self.x > 0 :
            self.x -= 7
        if pressed_keys[K_RIGHT] and self.x < 540 :
            self.x += 7
    def draw(self):
        screen.blit(fighter_image, (self.x, 591))

    def fire(self) :
        missiles.append(Missile(self.x+50))
class Missile :
    def __init__(self, x) :
        self.x = x
        self.y = 591

    def move(self) :
        self.y -= 5

    def off_screen(self) :
        return self.y < -8
    
    def draw(self) :
     screen.blit(missile_image, (self.x-4, self.y))
# 리스트
baduys = []             # 악당0
fighter = Fighter()
missiles = []

# 게임 루프
while True:  # 무한 루프 시작
    clock.tick(60)  # 초당 60프레임으로 설정
    for event in pygame.event.get():  # 이벤트 처리
        if event.type == QUIT:  # 창 닫기 이벤트 처리
            sys.exit()  # 프로그램 종료

       # if event.type == KEYDOWN and event.key == K_SPACE :
            #fighter.fire()
    
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_SPACE] and time.time() - last_missile_spawn_time > 0.2:
        fighter.fire()
        last_missile_spawn_time = time.time()
        

    if time.time() - last_badguys_time > 0.5:
        baduys.append(Badguy())
        last_badguys_time = time.time()
    
    screen.fill((0, 0, 0))  # 화면을 검은색으로 채움    #RGB
    fighter.move()
    fighter.draw()

    i = 0
    while i < len(baduys):
        baduys[i].move()  
        baduys[i].draw()   
        if baduys[i].off_screen():
            del baduys[i]
            i -= 1 
        i += 1
    
    i = 0
    while i < len(missiles):
        missiles[i].move()
        missiles[i].draw()
        if missiles[i].off_screen():
            del missiles[i]
            i -= 1
        i += 1


    pygame.display.update()  
