import debugpy


def setup_debugpy() -> None:
    debugpy.listen(5678)
    print("Warte auf Debugger...")
    debugpy.wait_for_client()  # Pausiert das Skript, bis VS Code verbunden ist
    print("Debugger verbunden, starte Server...")
