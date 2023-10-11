import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import menu
import textwrap
from utils.constants import *
from objects import *

pygame.init()

pygame.display.set_caption("Plant Growing Simulator")
window = pygame.display.set_mode((window_width, window_height))
img_point = pygame.image.load("assets/images1/point.png")
img_point = pygame.transform.scale(img_point, (xgrid_image_width, xgrid_image_height))
img_death = pygame.image.load("assets/images1/death.png")
img_death = pygame.transform.scale(img_death, (xgrid_image_width, xgrid_image_height))
sliders = []
outputs = []
point_list = []
global lives
lives_text = TextBox(window, 950, 353, 0, 0, fontSize=30, textColour=GREY1)

# Define recognized RGB combinations for RED, YELLOW, and GREEN
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

def update_slider_colors(sliders, point_list):
    for i, slider in enumerate(sliders):
        if i == 1 or i == 3:
            if point_list[i] <= 0:
                slider.handleColour = (204, 0, 0)  # Dimmed RED
            elif point_list[i] == 1:
                slider.handleColour = (204, 204, 0)  # Dimmed YELLOW
            else:
                slider.handleColour = (0, 153, 0)  # Dimmed GREEN
        else:
            if point_list[i] <= 0:
                slider.handleColour = (204, 0, 0)  # Dimmed RED
            else:
                slider.handleColour = (0, 153, 0)  # Dimmed GREEN


# Create sliders
for i, (parameter, range_) in enumerate(zip(parameters, ranges)):
    min_, max_ = range_
    sliders.append(Slider(window, 100 + 670, 58 + (i * 35), 300, 10, min=min_, max=max_, step=1, handleColour=BLUE, colour=GREY, handleRadius=10))
    outputs.append(TextBox(window, 420 + 670, 80 + (i * 35), 0, 0, fontSize=24, textColour=GREY1))
    outputs[i].disable()

def draw_interface(plant, points, point_list):
    window.fill(BLACK)
    lives_text.setText("Antal liv - " + str(lives))
    # Load plant name
    plant_name_text = font_header.render(plant.name, True, GREY1)
    # Draw gridlines
    for x in range(0, window_width, cell_width):
        pygame.draw.line(window, WHITE, (x, 0), (x, window_height))
    for y in range(0, window_height, cell_height):
        pygame.draw.line(window, WHITE, (0, y), (window_width, y))

    for i in range(xgrid_height):
        for j in range(xgrid_width):
            cell_x = xgrid_x + j * xgrid_cell_width
            cell_y = xgrid_y + i * xgrid_cell_height

            pygame.draw.rect(window, WHITE, (cell_x, cell_y, xgrid_cell_width, xgrid_cell_height), 1)

    # Top-left: Plant name
    window.blit(plant_name_text, ((cell_width // 2) - plant_name_text.get_width() // 2, 20))

    # Top-left: Plant image
    img = plant.image
    window.blit(img, (img_x, img_y))

    # Top-right: Parameter headline
    window.blit(parametre_text, (parametre_x, 20))

    # Bottom-left: "Egenskaber" header
    window.blit(egenskaber_text, (egenskaber_x, egenskaber_y))

    # Parameters: Labels, sliders, and outputs
    for i, parameter in enumerate(parameters):
        label_text = font_param.render(parameter, True, GREY1)
        window.blit(label_text, (param_x, param_y+i*param_spacing))
    
    # Simulate button
    pygame.draw.rect(window, button_color, button_rect)
    window.blit(button_text, button_text_rect)


    # Draw images in xgrid cells
    xgrid_images = points
    if -1 in point_list:
        for i in range(9):
            cell_x = xgrid_x + (i % xgrid_width) * xgrid_cell_width + 5
            cell_y = xgrid_y + (i // xgrid_width) * xgrid_cell_height + 5
            window.blit(img_death, (cell_x, cell_y))
    else:
        for i in range(xgrid_images):
            cell_x = xgrid_x + (i % xgrid_width) * xgrid_cell_width + 5
            cell_y = xgrid_y + (i // xgrid_width) * xgrid_cell_height + 5
            window.blit(img_point, (cell_x, cell_y))
    
    # Display plant description
    if plant.name in PLANT_NAMES:
        index = PLANT_NAMES.index(plant.name)
        description = PLANT_DESCRIPTIONS[index]
        description_lines = textwrap.wrap(description, 69)  # Wrap the description text
        for i, line in enumerate(description_lines):
            line_text = font_param.render(line, True, GREY1)
            window.blit(line_text, (25, egenskaber_y + 40 + (i * 25)))



def draw_squares(plant):
    global lives
    point_list = []
    run = True
    lives = 7
    points = 0
    # Reset slider values
    for slider, initial_value in zip(sliders, initial_values):
        slider.setValue(initial_value)
        slider.handleColour = BLUE

    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                elif event.key == pygame.K_BACKSPACE:
                    run = False
                    menu.run_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    arguments = [slider.getValue() for slider in sliders]
                    points, point_list = plant.simulate(arguments)
                    update_slider_colors(sliders, point_list)
                    lives -= 1
                    lives_text.setText("Antal liv = " + str(lives))
                    if lives < 0:
                        run = False
                        menu.run_menu()


        draw_interface(plant, points, point_list)
        for slider, output, unit in zip(sliders, outputs, units):
            if slider.max == 2:
                if slider.getValue() == 0:
                    output.setText(unit[0])
                elif slider.getValue() == 1:
                    output.setText(unit[1])
                else:
                    output.setText(unit[2])
            else:
                output.setText(str(slider.getValue()) + " " + unit)
        pygame_widgets.update(events)
        pygame.display.update()
