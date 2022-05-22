import time


class DisplayOutline:

    def __init__(self,
                 header_text,
                 header_coordinates,
                 header_hor_divider,
                 vertical_divider,
                 footnote_hor_divider,
                 footnote_text,
                 footnote_coordinates
                 ):
        self.header_text = header_text
        self.header_coordinates = header_coordinates
        self.header_hor_divider = header_hor_divider
        self.vertical_divider = vertical_divider
        self.footnote_hor_divider = footnote_hor_divider
        self.footnote_text = footnote_text
        self.footnote_coordinates = footnote_coordinates

    @classmethod
    def with_default_values(cls):
        return cls(
            header_text="Hallo Euckenstraße 17",
            header_coordinates=(85, 0),
            header_hor_divider=(5, 20, 291, 20),
            vertical_divider=(105, 25, 105, 103),
            footnote_hor_divider=(5, 108, 291, 108),
            footnote_text="Rezept des Tages: {}".format(time.strftime('%d.%m.%Y')),
            footnote_coordinates=(60, 105)
        )


