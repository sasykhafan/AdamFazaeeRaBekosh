import pygame, random, time
pygame.init()
TOOL, ARZ = 1600, 900
disp = pygame.display.set_mode((TOOL, ARZ))
icon = pygame.image.load('bazi_icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('منو') 
background_music = pygame.mixer.Sound('oiia_space.mp3')
background_music.play()
bg = pygame.image.load("background.jpg")
disp.blit(bg, (0, 0))
cour = pygame.font.Font('Lato-Regular.ttf', 40)


########### منو ################


notdone = True
while notdone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                notdone = False
                
    text = cour.render('Press ESC to go to the game', True, (255,0,0))
    disp.blit(bg, (0, 0))
    disp.blit(text, (200,200)) 
    pygame.display.update()


pygame.quit()

########### بازی ################

pygame.init()
pygame.key.set_repeat(100, 10)
disp = pygame.display.set_mode((TOOL, ARZ))
icon = pygame.image.load('bazi_icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('آدم فضایی ها را بکش') 
disp.blit(bg, (0, 0))
tofang1 = pygame.image.load('gun1.png', "")
tofang1_w, tofang1_h = TOOL // 20 * 3, ARZ // 20 * 3
tofang1 = pygame.transform.scale(tofang1, (tofang1_w,tofang1_h))
tofang1_x, tofang1_y = 0, 0

tir_e_tofang = pygame.image.load('Kenny_GlobShot_Item.png', "")
tir_e_tofang_w, tir_e_tofang_h = tofang1_w // 3, tofang1_h // 3
tir_e_tofang = pygame.transform.scale(tir_e_tofang, (tir_e_tofang_w,tir_e_tofang_h))

list_e_tirha = []


notdone = True
akharin_tir = time.time()
while notdone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notdone = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                tofang1_y -= ARZ // 100
                if tofang1_y < 0:
                    tofang1_y = 0
            if event.key == pygame.K_s:
                tofang1_y += ARZ // 100
                if tofang1_y + tofang1_h > ARZ:
                    tofang1_y = ARZ - tofang1_h
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if float(time.time() - akharin_tir) < 0.7:
                continue
            akharin_tir = time.time()
            list_e_tirha.append((tofang1_x + tofang1_w , tofang1_y + tofang1_h // 2))
                
    for i in range(len(list_e_tirha)):
        list_e_tirha[i] = (list_e_tirha[i][0] + 1, list_e_tirha[i][1])
            
    while len(list_e_tirha) > 0 and list_e_tirha[0][0] > TOOL:
        del list_e_tirha[0]
        
    disp.blit(bg, (0, 0))
    pygame.draw.line(disp,(255,255,255), (TOOL // 6,0),(TOOL // 6, ARZ),5)   
    disp.blit(tofang1,(tofang1_x,tofang1_y))
    for tir in list_e_tirha:
        disp.blit(tir_e_tofang,tir)
    pygame.display.update()


pygame.quit() 