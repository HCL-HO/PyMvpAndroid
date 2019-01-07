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


def get_new_package_name():
    subpackage_copy = subPackage
    if subpackage_copy is not '':
        if not subpackage_copy.endswith('/'):
            subpackage_copy += '/'
        return projectDir + subpackage_copy + className.lower() + '/'
    else:
        return projectDir + className.lower() + '/'


newPackagePath = get_new_package_name()
main_class_name = className + get_page_type(PageType)
mvp_presenter_class_name = className + 'MvpPresenter'
mvp_view_class_name = className + 'MvpView'
presenter_class_name = className + 'Presenter'
if not os.path.exists(newPackagePath):
    os.makedirs(newPackagePath)


def make_main_class():
    file = open(newPackagePath + main_class_name + '.java', 'x')
    file.write(
        'public class ' + main_class_name + ' extends MvpBaseFragment implements ' + mvp_view_class_name + ' {}')


def make_mvp_presenter_class():
    file = open(newPackagePath + mvp_presenter_class_name + '.java', 'x')
    file.write(
        'public interface ' + mvp_presenter_class_name + ' <V extends ' + mvp_view_class_name + '> extends '
        + BasePresenterName + '<V> {}')


def make_mvp_view_class():
    file = open(newPackagePath + mvp_view_class_name + '.java', 'x')
    file.write(
        'public interface ' + mvp_view_class_name + ' extends ' + BaseMvpViewName + ' {}')


def make_presenter_class():
    file = open(newPackagePath + presenter_class_name + '.java', 'x')
    file.write('public class ' + presenter_class_name +
               '<V extends ' + mvp_view_class_name + '> extends ' + BasePresenterName
               + '<V> implements ' + mvp_presenter_class_name + '<V> {}')


make_main_class()
make_mvp_presenter_class()
make_mvp_view_class()
make_presenter_class()
