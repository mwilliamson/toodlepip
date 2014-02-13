from datetime import timedelta

import xdg.BaseDirectory
import tempman


def create_temp_dir():
    temp_root = tempman.root(
        xdg.BaseDirectory.save_data_path("toodlepip/tmp"),
        timeout=timedelta(days=1)
    )
    return temp_root.create_temp_dir()
