from config import *
import os

FRAGMENT = 1
ACTIVITY = 2

PageType = FRAGMENT


def get_page_type(PageType) -> str:
    if PageType is FRAGMENT:
        return 'Fragment'
    elif PageType is ACTIVITY:
        return 'Activity'
    else:
        print('Page Type is not recognized')
        return ''


className = 'ABC'

newPackagePath = projectDir + className.lower()

if not os.path.exists(newPackagePath):
    os.makedirs(newPackagePath)

open(newPackagePath + className + get_page_type(PageType) + '.java', 'x')
open(newPackagePath + className + 'MvpPresenter' + '.java', 'x')
open(newPackagePath + className + 'MVPView' + '.java', 'x')
open(newPackagePath + className + 'Presenter' + '.java', 'x')
