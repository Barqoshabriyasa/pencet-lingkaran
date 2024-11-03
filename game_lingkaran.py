import pygame
from pygame import mixer
# Inisialisasi Pygame
pygame.init()
mixer.init()

#upload audio
audio = mixer.Sound(r"D:\VSCODE LABIRIN\game lingkaran.mp3")

# Ukuran layar
screen = pygame.display.set_mode((500, 500)) #layar/scene
# Warna
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Posisi dan ukuran kotak
circle_pos = [100, 100]  # x, y, width, height
circle_color = RED
circle_radius = 30
# Kecepatan gerakan kotak
circle_speed = 3
# Fungsi untuk memeriksa apakah kotak diklik
def is_circle_clicked(pos, circle_pos, circle_radius):
    x, y = pos #tentukan posisinya
    circle_x, circle_y = circle_pos
    distance = ((x- circle_x)**2 + (y - circle_y)**2) ** 0.5
    circle_width, circle_height = circle_pos
    return distance <= circle_radius
# Loop utama
running = True
clock = pygame.time.Clock()  # Untuk mengatur frame rate
while running:
    for event in pygame.event.get(): #mengatur supaya game selalu berjalan
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if is_circle_clicked(event.pos, circle_pos, circle_radius):
                mixer.Sound.play(audio)
                # Ganti warna kotak saat diklik
                circle_color = GREEN if circle_color == RED else RED if circle_color== BLUE else BLUE if circle_color == GREEN else GREEN

    # Update posisi kotak
    circle_pos[1] += circle_speed
    
    # Pantulkan kotak jika mencapai tepi layar
    if circle_pos[1] - circle_radius <= 0 or circle_pos[1] + circle_radius >= screen.get_width():
        circle_speed = -circle_speed

    # Mengisi layar dengan warna putih
    screen.fill((100,1,2))

    # Menggambar kotak
    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)

    # Update layar
    pygame.display.flip()
    
    # Batasi frame rate
    clock.tick(60)

# Keluar dari Pygame
pygame.quit()
