#include "TestLab13.h"
#include <QtWidgets/QApplication>
#include <QApplication>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <qradiobutton.h>
#include <QListWidget>
#include <QHBoxLayout>
#include <QFormLayout>
#include <string.h>
#include <qstring.h>
#include <qpainter.h>
#include <qpalette.h>
#include <qfont.h>
#include "Controller.h"
using namespace std;

QListWidget *myEquationList;
Controller ctrl;

void populateEquations()
{
	if (myEquationList->count() > 0)
		myEquationList->clear();

	for (auto &eq : ctrl.getAllEquations())
	{
		QString currentEq= QString::fromStdString(eq.toString());
		QListWidgetItem *item = new QListWidgetItem(currentEq);
		
		myEquationList->addItem(item);
	}
	if (ctrl.getAllEquations().size() > 0)
		myEquationList->setCurrentRow(0);

	

	QListWidgetItem *item = new QListWidgetItem("dfsdsfs");
	QListWidgetItem *item2 = new QListWidgetItem("dfsdsfs");
	QListWidgetItem *item3 = new QListWidgetItem("dfsdsfs");
	myEquationList->addItem(item);
	myEquationList->addItem(item2);
	myEquationList->addItem(item3);
}

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	//TestLab13 w;
	QWidget *mainProgram = new QWidget{};

	QHBoxLayout *hbox = new QHBoxLayout{};
	


	QFormLayout *myLayout = new QFormLayout{};

	QLabel *allEqLabel = new QLabel{ "Equations: " };
	myLayout->addWidget(allEqLabel);


	myEquationList = new QListWidget{};
	myEquationList->setSelectionMode(QAbstractItemView::SingleSelection);
	populateEquations();
	myLayout->addWidget(myEquationList);

	QLineEdit* aTB = new QLineEdit{};
	QLabel* aL = new QLabel{ "a:" };

	QLineEdit* bTB = new QLineEdit{};
	QLabel* bL = new QLabel{ "b:" };

	QLineEdit* cTB = new QLineEdit{};
	QLabel* cL = new QLabel{ "c:" };

	myLayout->addRow(aL, aTB);
	myLayout->addRow(bL, bTB);
	myLayout->addRow(cL, cTB);


	QPushButton *updateButton = new QPushButton{"Update"};
	QPushButton *computeButton = new QPushButton{"Compute"};
	
	myLayout->addRow(updateButton);
	myLayout->addRow(computeButton);


	

	QObject::connect(updateButton, &QPushButton::clicked, [aTB, bTB, cTB]() {
		double a = aTB->text().toDouble();
		double b = bTB->text().toDouble();
		double c = cTB->text().toDouble();

		auto eq = ctrl.getAllEquations()[myEquationList->currentIndex().row()];

		ctrl.update(eq,a,b,c);
		populateEquations();

	});

	QLabel *sol1 = new QLabel{"r1: "};
	QLabel* s1 = new QLabel{};
	QLabel *sol2 = new QLabel{"r2: "};
	QLabel* s2 = new QLabel{};
	myLayout->addRow(sol1,s1);
	myLayout->addRow(sol2,s2);



	QObject::connect(computeButton, &QPushButton::clicked, [aTB, bTB, cTB]() {
		auto eq = ctrl.getAllEquations()[myEquationList->currentIndex().row()];
		sol solution =  eq.computeResult();
		int x = solution.x1;
		int y = solution.x2;
		string st1 = to_string(x);
		string st2 = to_string(y);
		//s1->setText(st1);
		//s1->setText(solution.x1.to_string);
		//s2->setText(solution.x1.to_string);
		//populateEquations();

	});

	

	hbox->addLayout(myLayout);
	mainProgram->setLayout(hbox);

	mainProgram->show();
	return a.exec();
}
