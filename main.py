import pygame

# zainicjowanie biblioteki
pygame.init()

# stworzenie okna gry
window = pygame.display.set_mode((800,600))

# stworzenie nieskończonej pętli
run = True
while run:

   # oczytywanie zdazreń wywołanych przez gracza
   for event in pygame.event.get():
        if event.type == pygame.QUIT: #jeśli gracz zamknie okno gry
            run = False