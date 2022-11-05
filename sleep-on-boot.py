from talon import app, actions

# https://talon.wiki/basic_customization/#turn-off-talon-listening-on-start-up
def disable():
    actions.speech.disable()

app.register("ready", disable)
