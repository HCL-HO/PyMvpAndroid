from config import *
import os
import sys

print('working on: ' + projectDir)

FRAGMENT = '1'
ACTIVITY = '2'

PageType = FRAGMENT
className: str = 'ABC'

print('Input Module Name: ')
className = input()

print('Module Type: 1: fragment, 2: activity')
PageType = input()
PageType.replace(' ', '')

print('Sub package name: ')
subPackage = input()


def get_page_type(PageType) -> str:
    if PageType is FRAGMENT:
        return 'Fragment'
    elif PageType is ACTIVITY:
        return 'Activity'
    else:
        print('Page Type is not recognized: ' + PageType)
        sys.exit()


def get_new_package_path():
    subpackage_copy = subPackage
    if subpackage_copy is not '':
        if not subpackage_copy.endswith('/'):
            subpackage_copy += '/'
        return projectDir + subpackage_copy + className.lower() + '/'
    else:
        return projectDir + className.lower() + '/'


def get_new_package_name():
    split = projectDir.split('/java/')
    package = split[1].replace('/', '.')
    subpackage_copy = subPackage
    subpackage_copy = subpackage_copy.replace('/', '.')
    if subPackage is not '':
        return package + subpackage_copy + "." + className.lower()
    else:
        return package[-1:]


def get_package_sentence():
    package = get_new_package_name()
    return 'package ' + package + ';\n'


newPackagePath = get_new_package_path()
main_class_name = className + get_page_type(PageType)
mvp_presenter_class_name = className + 'MvpPresenter'
mvp_view_class_name = className + 'MvpView'
presenter_class_name = className + 'Presenter'
if not os.path.exists(newPackagePath):
    os.makedirs(newPackagePath)


def make_main_class():
    classType = ''
    if PageType is FRAGMENT:
        classType = BaseFragmentName
    else:
        classType = BaseActivityName

    file = open(newPackagePath + main_class_name + '.java', 'x')
    file.write(
        get_package_sentence() +
        'public class ' + main_class_name + ' extends ' + classType + ' implements ' + mvp_view_class_name + ' {}')


def make_mvp_presenter_class():
    file = open(newPackagePath + mvp_presenter_class_name + '.java', 'x')
    file.write(
        get_package_sentence() +
        'public interface ' + mvp_presenter_class_name + ' <V extends ' + BaseMvpViewName + '> extends '
        + MvpPresenterName + '<V> {}')


def make_mvp_view_class():
    file = open(newPackagePath + mvp_view_class_name + '.java', 'x')
    file.write(
        get_package_sentence() +
        'public interface ' + mvp_view_class_name + ' extends ' + BaseMvpViewName + ' {}')


def make_presenter_class():
    file = open(newPackagePath + presenter_class_name + '.java', 'x')
    file.write(
        get_package_sentence() +
        'public class ' + presenter_class_name +
        '<V extends ' + mvp_view_class_name + '> extends ' + BasePresenterName
        + '<V> implements ' + mvp_presenter_class_name + '<V> {}')


make_main_class()
make_mvp_presenter_class()
make_mvp_view_class()
make_presenter_class()
