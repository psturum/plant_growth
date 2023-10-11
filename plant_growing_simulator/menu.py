import pygame
from pygame.locals import *
import squares
from utils.constants import *
from objects import *

pygame.init()

window = pygame.display.set_mode((window_width, window_height))
font = pygame.font.Font(None, 24)
font1 = pygame.font.Font(None, 22)
img_height = cell_height // 3
img_width = cell_width1 - 20
selected_cell = 1  # Currently selected cell

# Load the images
images = []
images1 = []
for img_path in IMG_NAMES:
    img = pygame.image.load("assets/images/" + img_path)
    img = pygame.transform.scale(img, (img_width, img_height))
    images.append(img)

for img_path in IMG_NAMES:
    img = pygame.image.load("assets/images/" + img_path)
    img = pygame.transform.scale(img, (img_widthyhh, img_heightyhh))
    images1.append(img)

def draw_interface():
    window.fill(BLACK)

    # Draw the menu grid
    for i in range(grid_height):
        for j in range(grid_width1):
            cell_x = j * cell_width1
            cell_y = i * cell_height

            # Determine cell color based on selection and hover state
            cell_color = (0, 0, 0)
            if i * grid_width1 + j + 1 == selected_cell:
                cell_color = (100, 100, 100)

            pygame.draw.rect(window, cell_color, (cell_x, cell_y, cell_width1, cell_height))
            pygame.draw.rect(window, WHITE, (cell_x, cell_y, cell_width1, cell_height), 1)

            # Split the plant name into lines
            plant_name = PLANT_NAMES[i * grid_width1 + j]
            max_chars_per_line = 20  # Maximum characters per line
            lines = [plant_name[i:i + max_chars_per_line] for i in range(0, len(plant_name), max_chars_per_line)]

            # Render each line of text separately
            line_height = font.get_height()
            for line_number, line in enumerate(lines):
                line_render = font.render(line, True, GREY1)
                line_x = cell_x + cell_width1 // 2 - line_render.get_width() // 2
                line_y = cell_y + 20 + 20 * line_number
                window.blit(line_render, (line_x, line_y))

            # Display the image
            img = images[i * grid_width1 + j]
            img_x = cell_x + 10
            img_y = cell_y + (cell_height - img_height) // 2 - 30
            window.blit(img, (img_x, img_y))

            # Display the plant properties
            plant_properties = PLANT_DATA.get(plant_name)
            if plant_properties:
                gode_egenskaber = plant_properties.get('Gode egenskaber', [])
                line_y = cell_y + cell_height - 3 * line_height - 70

                for prop in gode_egenskaber:
                    if len(prop) > max_chars_per_line:
                        prop_lines = [prop[i:i + max_chars_per_line] for i in range(0, len(prop), max_chars_per_line)]
                        for prop_line in prop_lines:
                            if prop_line != prop_lines[-1]:
                                prop_line += "-"  # Add "-" at the end of the line
                            prop_render = font1.render(prop_line, True, GREY1)
                            prop_x = cell_x + cell_width1 // 2 - prop_render.get_width() // 2
                            window.blit(prop_render, (prop_x, line_y))
                            line_y += line_height
                            line_y += line_height  # Add extra space between lines
                    else:
                        prop_render = font1.render(prop, True, GREY1)
                        prop_x = cell_x + cell_width1 // 2 - prop_render.get_width() // 2
                        window.blit(prop_render, (prop_x, line_y))
                        line_y += line_height
                        line_y += line_height  # Add extra space between lines

    pygame.display.update()




def run_menu():
    global selected_cell, hover_cell

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP:
                    selected_cell -= grid_width1
                    if selected_cell <= 0:
                        selected_cell += len(PLANT_NAMES)
                elif event.key == K_DOWN:
                    selected_cell += grid_width1
                    if selected_cell > len(PLANT_NAMES):
                        selected_cell -= len(PLANT_NAMES)
                elif event.key == K_LEFT:
                    selected_cell -= 1
                    if selected_cell <= 0:
                        selected_cell += len(PLANT_NAMES)
                elif event.key == K_RIGHT:
                    selected_cell += 1
                    if selected_cell > len(PLANT_NAMES):
                        selected_cell -= len(PLANT_NAMES)
                elif event.key == K_RETURN:
                    # Proceed to the next screen with 4 squares
                    plant = Plant(
                        name=PLANT_NAMES[selected_cell - 1],
                        image=images1[PLANT_NAMES.index(PLANT_NAMES[selected_cell - 1])],
                    )
                    squares.draw_squares(plant)  # Pass the plant name
                    selected_cell = 1

        draw_interface()

    pygame.quit()
