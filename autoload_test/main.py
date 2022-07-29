import os
from autoload import ModuleLoader

ModuleLoader.set_setting(
    base_path=os.getcwd(), 
    strict=False,
    singleton=True
)

loader_a = ModuleLoader()
packages_classes = loader_a.load_classes(
    'packages',
    excludes=['teacher'],
    recursive= True
    )

packages_func = loader_a.load_functions(
    'person',
    excludes=['write_lesson'],
    recursive= True
    )


class_persn = loader_a.load_class('teacher')

clazz = packages_classes[0]
clazz().hello()

classes_teacher = loader_a.load_classes('tools/teacher')
teacher = classes_teacher[0]
teacher.write_lesson()

