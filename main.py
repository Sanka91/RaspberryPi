from backend import Backend
from api_util import APIUtil
from epaperutil import EPaperUtil
from display_controller import DisplayController
from display_outline import DisplayOutline

def main():

    backend = Backend()
    e_paper_util = EPaperUtil()
    e_paper_util.setup_library()

    recipe = Backend.get_recipe()
    qr_code = Backend.get_qr_code(recipe=recipe)

    # Controls writing on screen
    displayController = DisplayController()

    display_outline = DisplayOutline.with_default_values()
    displayController.add_text_to_frame(text=display_outline.header_text, coordinates=display_outline.header_coordinates)
    displayController.add_line_to_frame(x1y1x2y2=display_outline.header_hor_divider)
    displayController.add_line_to_frame(x1y1x2y2=display_outline.vertical_divider)
    displayController.add_line_to_frame(x1y1x2y2=display_outline.footnote_hor_divider)
    displayController.add_text_to_frame(text=display_outline.footnote_text, coordinates=display_outline.footnote_coordinates)

    displayController.add_image_to_frame(image=qr_code.get_formatted_qr_code(), coordinates=(15, 27))

    displayController.add_text_to_frame(text="{}...".format(recipe.title[:25]), coordinates=(120, 20))
    displayController.add_text_to_frame(text="Glutenfrei: {}".format(recipe.isGlutenFree), coordinates=(120, 33))
    displayController.add_text_to_frame(text="Vegan: {}".format(recipe.isVegan), coordinates=(120, 46))
    displayController.add_text_to_frame(text="Vegetarisch: {}".format(recipe.isVegetarian), coordinates=(120, 59))
    displayController.add_text_to_frame(text="Fertig in: {} Min".format(recipe.ready_in_minutes), coordinates=(120, 72))
    displayController.add_text_to_frame(text="Portionen: {}".format(recipe.servings), coordinates=(120, 85))


    print(display_outline.header_text)
    displayController.update_display()


if __name__ == "__main__":
    main()