import sys
sys.path.append("plugins\\")

import pluggy
import logging
import importlib
import hook
from pathlib import Path
import pickle
from PySide6.QtWidgets import QApplication

plug_path = Path(__file__).resolve().parent/"plugins"
usr_path = plug_path.parent/"usr.pkl"

pm = pluggy.PluginManager("GetBigFile")
pm.add_hookspecs(hook)
for plug in plug_path.iterdir():
    try:
        mod = importlib.import_module(plug.stem)
        pm.register(mod)
    except ModuleNotFoundError:
        pass
pm.hook.others()
app = QApplication(sys.argv)
window = pm.hook.makeaUi()
if usr_path.exists():
    pass
elif not usr_path.exists():
    window.plug_sql_ask()
window.show()
sys.exit(app.exec())
