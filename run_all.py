import importlib
from pathlib import Path

modules = sorted(list(Path('.').glob('day*')), key=lambda x: int(str(x)[3:]))
modules = [str(x) for x in modules]

for module in modules:
    day = importlib.import_module('%s.%s' % (module, module,))
    day.print_solutions_for_day()
