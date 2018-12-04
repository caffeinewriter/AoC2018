from timeit import timeit
from pathlib import Path

modules = sorted(list(Path('.').glob('day*')), key=lambda x: int(str(x)[3:]))
modules = [str(x) for x in modules]

for module in modules:
    print('Testing %s...' % module)
    print('Testing part_1()...')
    exec_str = '''
from {module}.{module} import part_1
part_1()
'''.format(module=module)
    part_1_bench = timeit(exec_str, number=100)
    print('Total execution time: %1.5f\nAverage execution time: %1.5f' %
          (part_1_bench, part_1_bench / 100,))
    print('Testing part_2()...')
    exec_str = '''
from {module}.{module} import part_2
part_2()
'''.format(module=module)
    part_2_bench = timeit(exec_str, number=100)
    print('Total execution time: %1.5f\nAverage execution time: %1.5f' %
          (part_2_bench, part_2_bench / 100,))
