import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110

# Open the window and set the background
arcade.open_window(400, 400, "Complex Loops - Box")

arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# Loop for each row
for row in range(10):
    # Loop for each column
    # Change the number of columns depending on the row we are in
    for column in range(10):
        # Calculate our location
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        if(row+column)%2==0:
            color_rec=arcade.color.RED
        else:
            color_rec=arcade.color.BLUE

        # Draw the item
        arcade.draw_rectangle_filled(x, y,10,10,color_rec,45)

# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()