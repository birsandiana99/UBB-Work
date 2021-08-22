#include "LabGUI.h"
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QListWidget>
#include <QHBoxLayout>
#include <QFormLayout>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);

	QHBoxLayout* hbox = new QHBoxLayout();

	QFormLayout *formLayoutLeft = new QFormLayout{};

	QLabel* dogsLabel = new QLabel{ "All dogs:" };
	formLayoutLeft->addWidget(dogsLabel);

	QListWidget *listDogs = new QListWidget();
	new QListWidgetItem("Gone With the Wind", listDogs);
	//new QListWidgetItem("The Three Musketeers", &list);
	formLayoutLeft->addWidget(listDogs);
	
	QLineEdit* nameTextBox = new QLineEdit{};
	QLabel* nameLabel = new QLabel{ "&Name: " };
	nameLabel->setBuddy(nameTextBox);

	QLineEdit* ageTextBox = new QLineEdit{};
	QLabel* ageLabel = new QLabel{ "&Age:" };
	ageLabel->setBuddy(ageTextBox);

	QLineEdit* breedTextBox = new QLineEdit{};
	QLabel* breedLabel = new QLabel{ "&Breed:" };
	breedLabel->setBuddy(breedTextBox);

	QLineEdit* picTextBox = new QLineEdit{};
	QLabel* picLabel = new QLabel{ "&Photo:" };
	picLabel->setBuddy(picTextBox);

	formLayoutLeft->addRow(nameLabel, nameTextBox);
	formLayoutLeft->addRow(ageLabel, ageTextBox);
	formLayoutLeft->addRow(breedLabel, breedTextBox);
	formLayoutLeft->addRow(picLabel, picTextBox);

	QGridLayout *gridLayoutDogs = new QGridLayout{};
	gridLayoutDogs->addWidget(new QPushButton("Add"), 0, 0);
	gridLayoutDogs->addWidget(new QPushButton("Delete"), 0, 1);
	gridLayoutDogs->addWidget(new QPushButton("Update"), 0, 2);
	gridLayoutDogs->addWidget(new QPushButton("Filter"), 1, 1);
	QWidget* buttonsDogs = new QWidget{};
	buttonsDogs->setLayout(gridLayoutDogs);
	formLayoutLeft->addWidget(buttonsDogs);

	QFormLayout *formLayoutCenter = new QFormLayout{};

	QGridLayout *gridLayoutCenter = new QGridLayout{};
	gridLayoutCenter->addWidget(new QPushButton("Adopt"), 0, 0);
	//gridLayoutCenter->setAlignment(Qt::AlignHCenter);
	QWidget* adoptButton = new QWidget{};
	adoptButton->setLayout(gridLayoutCenter);
	formLayoutCenter->addWidget(adoptButton);


	/**/

	QFormLayout *formLayoutRight = new QFormLayout{};

	QLabel* adoptedLabel = new QLabel{ "Adopted:" };
	formLayoutRight->addWidget(adoptedLabel);

	QListWidget *listAdopt = new QListWidget();
	listAdopt->setFixedHeight(300);
	new QListWidgetItem("Gone With the Wind", listAdopt);
	//new QListWidgetItem("The Three Musketeers", &list);
	formLayoutRight->addWidget(listAdopt);

	QGridLayout *gridLayoutAdopt = new QGridLayout{};
	//gridLayoutAdopt
	//gridLayoutAdopt->addWidget(new QPushButton("Adopt"), 0, 0);
	//gridLayoutAdopt->addWidget(new QPushButton("Next"), 0, 1);
	QWidget* buttonsAdopt = new QWidget{};
	buttonsAdopt->setLayout(gridLayoutAdopt);
	formLayoutRight->addWidget(buttonsAdopt);
	
	/*
	QHBoxLayout* hbox1 = new QHBoxLayout();
	//QGridLayout *gridLayout2 = new QGridLayout{};
	hbox1->addWidget(new QPushButton("Adopt"), 0, 0);
	hbox1->setAlignment(Qt::AlignCenter);
	QWidget* buttons2 = new QWidget{};
	buttons2->setLayout(hbox1);
	formLayout->addWidget(buttons2);
	*/
	



	QWidget *wnd = new QWidget{};
	hbox->addLayout(formLayoutLeft);
	hbox->addLayout(formLayoutCenter);
	hbox->addLayout(formLayoutRight);
	wnd->setLayout(hbox);
	wnd->show();

	

	



	return a.exec();
}
