from ui.main_window import MainWindow, Config
from json import load

with open("config.json") as config_file:
    config = Config(**load(config_file))
    main_window = MainWindow(config)
    main_window.run()

