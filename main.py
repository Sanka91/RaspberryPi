from backend import Backend
from api_util import APIUtil
from epaperutil import EPaperUtil
from display_controller import DisplayController
from display_outline import DisplayOutline
import datetime
import time

def main():

    e_paper_util = EPaperUtil()
    e_paper_util.setup_library()
    today = datetime.datetime.today().day

    # Controls writing on screen
    display_controller = DisplayController()

    # Initial pull of Recipe and Qr Code
    recipe = Backend.get_recipe()
    qr_code = Backend.get_qr_code(recipe=recipe)
    quote = Backend.get_quote()

    def run_motivational_quote_screen():
        display_outline = DisplayOutline(header_text= "Zitat des Tages", header_coordinates=(92, 0))
        display_controller.add_text_to_frame(text=display_outline.header_text,
                                             coordinates=display_outline.header_coordinates,
                                             font_size=e_paper_util.font14_bold)
        display_controller.add_line_to_frame(x1y1x2y2=display_outline.header_hor_divider)

        display_controller.add_text_to_frame(text=quote.screen_content,
                                             coordinates=(20, 23),
                                             font_size=e_paper_util.font14)
        display_controller.add_text_to_frame(text="#{}, {}".format(quote.author, quote.profession),
                                             coordinates=(100, 106),
                                             font_size=e_paper_util.font13_bold)
        display_controller.show_content()

    def run_recipe_and_qr_screen():

        display_outline = DisplayOutline(footnote_text="Rezept des Tages: {}".format(time.strftime('%d.%m.%Y')))
        display_controller.add_text_to_frame(text=display_outline.header_text, coordinates=display_outline.header_coordinates, font_size=EPaperUtil.font14_bold)
        display_controller.add_line_to_frame(x1y1x2y2=display_outline.header_hor_divider)
        display_controller.add_line_to_frame(x1y1x2y2=display_outline.vertical_divider)
        display_controller.add_line_to_frame(x1y1x2y2=display_outline.footnote_hor_divider)
        display_controller.add_text_to_frame(text=display_outline.footnote_text, coordinates=display_outline.footnote_coordinates, font_size=EPaperUtil.font14_bold)

        display_controller.add_image_to_frame(image=qr_code.get_formatted_qr_code(), coordinates=(15, 27))

        display_controller.add_text_to_frame(text="{}".format(recipe.display_title), coordinates=(120, 20), font_size=EPaperUtil.font14)
        display_controller.add_text_to_frame(text="Glutenfrei: {}".format(recipe.isGlutenFree), coordinates=(120, 40))
        display_controller.add_text_to_frame(text="Vegan: {}".format(recipe.isVegan), coordinates=(120, 53))
        display_controller.add_text_to_frame(text="Vegetarisch: {}".format(recipe.isVegetarian), coordinates=(120, 66))
        display_controller.add_text_to_frame(text="Fertig in: {} Min".format(recipe.ready_in_minutes), coordinates=(120, 79))
        display_controller.add_text_to_frame(text="Portionen: {}".format(recipe.servings), coordinates=(120, 92))

        display_controller.show_content()

    # Updates Recipe and QR Code via API each new day
    while True:
        if datetime.datetime.today().day != today:
            today = datetime.datetime.today().day
            recipe = Backend.get_recipe()
            qr_code = Backend.get_qr_code(recipe=recipe)
        else:
            run_recipe_and_qr_screen()
            time.sleep(60)
            display_controller.clear_display()
            run_motivational_quote_screen()
            time.sleep(60)
            display_controller.clear_display()


if __name__ == "__main__":
    main()