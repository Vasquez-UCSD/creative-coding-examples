# ------------------------
# GLOBAL
# ------------------------
ui = []

health = 75
slider_value = 50

dragging_panel = False
dragging_slider = False

panel_offset_x = 0
panel_offset_y = 0

panel_x, panel_y = 40, 40
panel_w, panel_h = 300, 350

click_sound = None


# ------------------------
# UI CLASSES
# ------------------------
class Button:
    def __init__(self, x, y, w, h, label, action):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.label = label
        self.action = action
        self.scale = 1.0

    def draw(self):
        hovered = self.is_hovered()

        # smooth hover animation
        target_scale = 1.08 if hovered else 1.0
        self.scale += (target_scale - self.scale) * 0.2

        px = panel_x + self.x
        py = panel_y + self.y

        push_matrix()

        # scale from center
        translate(px + self.w / 2, py + self.h / 2)
        scale(self.scale)
        translate(-self.w / 2, -self.h / 2)

        # button background
        fill(40, 80, 150, 190)
        stroke(120, 180, 255)
        stroke_weight(1)

        rect(0, 0, self.w, self.h, 12)

        # text
        fill(255)
        text_align(CENTER, CENTER)
        text_size(14)

        text(self.label, self.w / 2, self.h / 2)

        pop_matrix()

    def is_hovered(self):
        px = panel_x + self.x
        py = panel_y + self.y

        return (
            px < mouse_x < px + self.w and
            py < mouse_y < py + self.h
        )

    def click(self):
        global health

        # play sound if available
        if click_sound:
            click_sound.play()

        if self.action == "heal":
            health += 10

        elif self.action == "damage":
            health -= 10

        elif self.action == "reset":
            health = 100

        # clamp health
        health = max(0, min(100, health))


# ------------------------
class Slider:
    def __init__(self, x, y, w):
        self.x, self.y, self.w = x, y, w

    def draw(self):
        global slider_value

        px = panel_x + self.x
        py = panel_y + self.y

        # label
        fill(255)
        text_align(LEFT, BOTTOM)
        text_size(14)

        text(f"Volume: {slider_value}", px, py - 10)

        # slider track
        fill(70)
        no_stroke()

        rect(px, py, self.w, 6, 5)

        # knob position
        knob_x = px + (slider_value / 100) * self.w

        # glow
        fill(255, 120, 120, 80)
        ellipse(knob_x, py + 3, 24, 24)

        # knob
        fill(255, 120, 120)
        stroke(255)

        ellipse(knob_x, py + 3, 16, 16)

    def is_hovered(self):
        px = panel_x + self.x
        py = panel_y + self.y

        return (
            px < mouse_x < px + self.w and
            py - 10 < mouse_y < py + 16
        )

    def drag(self):
        global slider_value

        px = panel_x + self.x

        slider_value = int(
            ((mouse_x - px) / self.w) * 100
        )

        slider_value = max(0, min(100, slider_value))


# ------------------------
class HealthBar:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

    def draw(self):
        global health

        px = panel_x + self.x
        py = panel_y + self.y

        # label
        fill(255)
        text_align(LEFT, BOTTOM)
        text_size(14)

        text(f"Health: {health}", px, py - 8)

        # background
        fill(50)
        no_stroke()

        rect(px, py, self.w, self.h, 6)

        # health amount
        fill(255, 70, 70)

        rect(
            px,
            py,
            self.w * (health / 100),
            self.h,
            6
        )


# ------------------------
# SETUP
# ------------------------
def setup():
    global click_sound

    size(900, 650)
    smooth()

    text_size(14)

    # optional sound
    try:
        click_sound = load_sound("click.wav")
    except:
        click_sound = None

    # build UI
    ui.append(Button(20, 70, 120, 40, "Heal", "heal"))
    ui.append(Button(160, 70, 120, 40, "Damage", "damage"))

    ui.append(Button(20, 130, 260, 40, "Reset", "reset"))

    ui.append(Slider(20, 220, 260))

    ui.append(HealthBar(20, 280, 260, 20))


# ------------------------
# DRAW
# ------------------------
def draw():
    background(18)

    draw_panel()
    draw_ui()
    draw_hotkeys()


# ------------------------
def draw_panel():
    # panel body
    fill(30, 30, 40, 220)
    stroke(100, 150, 255)
    stroke_weight(1)

    rect(panel_x, panel_y, panel_w, panel_h, 16)

    # top draggable header
    fill(45, 55, 80, 200)

    rect(
        panel_x,
        panel_y,
        panel_w,
        42,
        16, 16, 0, 0
    )

    # title
    fill(255)

    text_align(CENTER, CENTER)
    text_size(16)

    text(
        "HUD PANEL (Drag Me)",
        panel_x + panel_w / 2,
        panel_y + 21
    )

    # reset alignment
    text_align(LEFT, TOP)
    text_size(14)


# ------------------------
def draw_ui():
    for element in ui:
        element.draw()


# ------------------------
def draw_hotkeys():
    fill(255)

    text_align(LEFT, TOP)
    text_size(16)

    text(
        "HOTKEYS:\n"
        "W = Heal\n"
        "S = Damage\n"
        "R = Reset\n"
        "Drag Header = Move UI\n"
        "Drag Slider = Change Volume",
        420,
        80
    )


# ------------------------
# INPUT
# ------------------------
def mouse_pressed():
    global dragging_panel
    global dragging_slider
    global panel_offset_x
    global panel_offset_y

    # drag panel only from header
    if (
        panel_x < mouse_x < panel_x + panel_w and
        panel_y < mouse_y < panel_y + 42
    ):
        dragging_panel = True

        panel_offset_x = mouse_x - panel_x
        panel_offset_y = mouse_y - panel_y

    # buttons
    for element in ui:
        if isinstance(element, Button):
            if element.is_hovered():
                element.click()

    # slider
    for element in ui:
        if isinstance(element, Slider):
            if element.is_hovered():
                dragging_slider = True


# ------------------------
def mouse_dragged():
    global panel_x
    global panel_y

    # move panel
    if dragging_panel:
        panel_x = mouse_x - panel_offset_x
        panel_y = mouse_y - panel_offset_y

    # drag slider
    if dragging_slider:
        for element in ui:
            if isinstance(element, Slider):
                element.drag()


# ------------------------
def mouse_released():
    global dragging_panel
    global dragging_slider

    dragging_panel = False
    dragging_slider = False


# ------------------------
def key_pressed():
    global health

    if key == 'w':
        health += 5

    elif key == 's':
        health -= 5

    elif key == 'r':
        health = 100

    # clamp value
    health = max(0, min(100, health))


# ------------------------
# START
# ------------------------
if __name__ == "__main__":
    run_sketch()