class button_util():
    def __init__(self) -> None:
        pass

    def make_button_style(
        self,
        background_color=None,
        color=None,
        height=None,               
        width=None,               
        margin_top=None,               
        margin_left=None,
        border_radius=None
    ):

    # white_button_style = {'background-color': 'white',
    #                       'color': 'black',
    #                       'height': '50px',
    #                       'width': '100px',
    #                       'margin-top': '10px',
    #                       'margin-left': '10px'}

    # red_button_style = {'background-color': 'red',
    #                     'color': 'white',
    #                     'height': '50px',
    #                     'width': '100px',
    #                     'margin-top': '10px',
    #                     'margin-left': '10px'}

        button_style = dict()
        button_style['background-color'] = background_color               
        button_style['color'] = color               
        button_style['height'] = height               
        button_style['width'] = width               
        button_style['margin-top'] = margin_top               
        button_style['margin-left'] = margin_left
        button_style['border-radius'] = border_radius

        return button_style