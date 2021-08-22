#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_TestLab13.h"

class TestLab13 : public QMainWindow
{
	Q_OBJECT

public:
	TestLab13(QWidget *parent = Q_NULLPTR);

private:
	Ui::TestLab13Class ui;
};
