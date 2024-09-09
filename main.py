def on_forever():
    if input.compass_heading() < 10 and input.compass_heading() > 350:
        basic.show_arrow(ArrowNames.NORTH)
    elif input.compass_heading() < 100 and input.compass_heading() > 80:
        basic.show_arrow(ArrowNames.EAST)
    elif input.compass_heading() < 190 and input.compass_heading() > 170:
        basic.show_arrow(ArrowNames.SOUTH)
    elif input.compass_heading() < 280 and input.compass_heading() > 260:
        basic.show_arrow(ArrowNames.WEST)
    else:
        basic.show_icon(IconNames.SKULL)
basic.forever(on_forever)
