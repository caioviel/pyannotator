#!/bin/bash
#rcc=pyside-rcc
#uic=pyside-uic

pyrcc4 ui/icons.qrc > ui/icons_rc.py
pyuic4 ui/PreviewWidget.ui > ui/ui_PreviewWidget.py
pyuic4 ui/AnnotationListItem.ui > ui/ui_AnnotationListItem.py
pyuic4 ui/MainProjectWidget.ui > ui/ui_MainProjectWidget.py
pyuic4 ui/InformationAnnotationWidget.ui > ui/ui_InformationAnnotationWidget.py
pyuic4 ui/ProjectChooseWidget.ui > ui/ui_ProjectChooseWidget.py
pyuic4 ui/ProjectChooseWidget.ui > ui/ui_ProjectChooseWidget.py
pyuic4 ui/WaitingDialog.ui > ui/ui_WaitingDialog.py
pyuic4 ui/VideoPlayer.ui > ui/ui_VideoPlayer.py

