#include "Assignment12.h"
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QListWidget>
#include <QHBoxLayout>
#include <QFormLayout>
#include "Controller.h"
#include "FileManager.h"
#include "qpalette.h"
using namespace std;

Controller ctrl = Controller();
QListWidget* dogsList;
QListWidget* adoptionList;

void addDogsToWindow() {

	if (dogsList->count() > 0)
		dogsList->clear();

	for (auto d : ctrl.getAllDogs())
	{
		QString currentDog = QString::fromStdString(d.getName() + ", " + to_string(d.getAge()) + ", " + d.getBreed() + ", " + d.getPhoto());
		QListWidgetItem* item = new QListWidgetItem{ currentDog};
		dogsList->addItem(item);
	}

	if (ctrl.getAllDogs().size() > 0)
		dogsList->setCurrentRow(0);

}

void addAdoptionListToWindow() {
	if (adoptionList->count() >= 0)
		adoptionList->clear();

	for (auto d : ctrl.getAdoptionList())
	{
		QString currentDog = QString::fromStdString(d.getName() + ", " + to_string(d.getAge()) + ", " + d.getBreed() + ", " + d.getPhoto());
		QListWidgetItem* item = new QListWidgetItem{ currentDog };
		adoptionList->addItem(item);
	}

	if (ctrl.getAdoptionList().size() > 0)
		adoptionList->setCurrentRow(0);




}




int main(int argc, char *argv[])
{
	QApplication a(argc, argv);

	QHBoxLayout* hbox = new QHBoxLayout();

	QFormLayout *formLayoutLeft = new QFormLayout{};

	QLabel* dogsLabel = new QLabel{ "All dogs:" };
	formLayoutLeft->addWidget(dogsLabel);

	dogsList = new QListWidget();
	dogsList->setSelectionMode(QAbstractItemView::SingleSelection);
	addDogsToWindow();
	formLayoutLeft->addWidget(dogsList);

	//QString qss = QString("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))");
	

	QLineEdit* nameTB = new QLineEdit{};
	QLabel* nameLabel = new QLabel{ "&Name: " };
	nameLabel->setBuddy(nameTB);


	QLineEdit* newNameTB = new QLineEdit{};
	QLabel* newName = new QLabel{ "&New name: " };
	newName->setBuddy(newNameTB);

	QLineEdit* ageTB = new QLineEdit{};
	QLabel* ageLabel = new QLabel{ "&Age:" };
	ageLabel->setBuddy(ageTB);

	QLineEdit* breedTB = new QLineEdit{};
	QLabel* breedLabel = new QLabel{ "&Breed:" };
	breedLabel->setBuddy(breedTB);

	QLineEdit* pictureTB = new QLineEdit{};
	QLabel* picLabel = new QLabel{ "&Photo:" };
	picLabel->setBuddy(pictureTB);


	formLayoutLeft->addRow(nameLabel, nameTB);
	formLayoutLeft->addRow(ageLabel, ageTB);
	formLayoutLeft->addRow(breedLabel, breedTB);
	formLayoutLeft->addRow(picLabel, pictureTB);
	formLayoutLeft->addRow(newName, newNameTB);



	QGridLayout *dogsGridLayout = new QGridLayout{};
	/*dogsGridLayout->addWidget(new QPushButton("Add"), 0, 0);
	dogsGridLayout->addWidget(new QPushButton("Delete"), 1, 0);
	dogsGridLayout->addWidget(new QPushButton("Update"), 2, 0);
	dogsGridLayout->addWidget(new QPushButton("Filter"), 3, 0);*/
	QWidget *dogButtons = new QWidget{};
	//dogButtons->setLayout(dogsGridLayout);
	//formLayoutLeft->addWidget(dogButtons);

	QPushButton *buttonForAdding = new QPushButton("Add");
	dogsGridLayout->addWidget(buttonForAdding, 0, 0);
	QObject::connect(buttonForAdding, &QPushButton::clicked, [nameTB, ageTB, breedTB, pictureTB]() {
		string name = nameTB->text().toUtf8().constData();
		int age = ageTB->text().toInt();
		string breed = breedTB->text().toUtf8().constData();
		string photo = pictureTB->text().toUtf8().constData();
		Dog d = Dog(breed, name, age, photo);
		ctrl.add(d);
		addDogsToWindow();


	});


	QPushButton *buttonForDeleting = new QPushButton("Delete");
	dogsGridLayout->addWidget(buttonForDeleting, 0, 1);
	QObject::connect(buttonForDeleting, &QPushButton::clicked, [nameTB]() {
		//string name = nameTB->text().toUtf8().constData();
		//ctrl.remove(name);
		//addDogsToWindow();

		auto dog = ctrl.getAllDogs()[dogsList->currentIndex().row()];
		string name = dog.getName();
		ctrl.remove(name);
		addDogsToWindow();
	});


		
	QPushButton *buttonForUpdating = new QPushButton("Update");
	dogsGridLayout->addWidget(buttonForUpdating, 0, 2);
	QObject::connect(buttonForDeleting, &QPushButton::clicked, [nameTB,newNameTB]() {
		string name = nameTB->text().toUtf8().constData();
		string newName = newNameTB->text().toUtf8().constData();
		//int age = ageTB->text().toInt();
		//string breed = breedTB->text().toUtf8().constData();
		//string photo = pictureTB->text().toUtf8().constData();
		//Dog d = Dog(breed, name, age, photo);
		ctrl.update(name, newName);
		addDogsToWindow();

	});


	dogButtons->setLayout(dogsGridLayout);
	formLayoutLeft->addWidget(dogButtons);


	QFormLayout *formLayoutCenter = new QFormLayout{};
	QGridLayout *gridLayoutCenter = new QGridLayout{};
	/*
	gridLayoutCenter->addWidget(new QPushButton("Adopt"), 0, 0);
	QWidget *adoptionButton = new QWidget{}; 
	adoptionButton->setLayout(gridLayoutCenter);
	formLayoutCenter->addWidget(adoptionButton);
	*/

	QPushButton *buttonForAdoption = new QPushButton("Adopt");
	gridLayoutCenter->addWidget(buttonForAdoption, 0, 0);
	QObject::connect(buttonForAdoption, &QPushButton::clicked, []() {
		auto dog = ctrl.getAllDogs()[dogsList->currentIndex().row()];
		ctrl.addToAdoptionList(dog, 2);
		addAdoptionListToWindow();
	});

	QWidget *adoptButton = new QWidget{};
	adoptButton->setLayout(gridLayoutCenter);
	formLayoutCenter->addWidget(adoptButton);


	QFormLayout *formLayoutRight = new QFormLayout{};
	QLabel* adoptedLbl = new QLabel{ "Adopted:" };
	formLayoutRight->addWidget(adoptedLbl);

	adoptionList = new QListWidget();
	adoptionList->setFixedHeight(300);
	//new QListWidgetItem("Gone With the Wind", adoptionList);
	formLayoutRight->addWidget(adoptionList);

	QPushButton *buttonForAdoptl = new QPushButton("View adoption list:");
	gridLayoutCenter->addWidget(buttonForAdoptl, 1, 0);
	QObject::connect(buttonForAdoptl, &QPushButton::clicked, []() {
		//////
		system("start htmlFile.html");
	});

	QGridLayout *adoptGridLayout = new QGridLayout{};
	QWidget* buttonsAdopt = new QWidget{};
	buttonsAdopt->setLayout(adoptGridLayout);
	formLayoutRight->addWidget(buttonsAdopt);


	QLinearGradient *myGradient = new QLinearGradient{ QPointF(100, 100), QPointF(200, 200) };
	myGradient->setColorAt(0, Qt::blue);
	myGradient->setColorAt(1, Qt::white);

	QWidget *windows = new QWidget{};
	QPalette *palette = new QPalette{};

	palette->setBrush(QPalette::Background, *myGradient);
	//mainProgram->setAutoFillBackground(true);
	windows->setPalette(*palette);
	

	
	hbox->addLayout(formLayoutLeft);
	hbox->addLayout(formLayoutCenter);
	hbox->addLayout(formLayoutRight);
	windows->setLayout(hbox);
	windows->show();

	return a.exec();
}
