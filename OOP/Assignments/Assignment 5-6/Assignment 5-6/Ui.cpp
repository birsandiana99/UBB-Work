#include "Ui.h"
#include "Dog.h"
#include <iostream>
#include <string>
#include <stdlib.h>
#include <Windows.h>
#include <shellapi.h>
//#include "FileMng.h"
#include "FileManagerx.h"

Ui::Ui()
{
	controller = Controller();
}



void Ui::openLink(string link)
{
	ShellExecute(NULL, NULL, "chrome.exe", link.c_str(), NULL, SW_SHOWMAXIMIZED);

}

void Ui::initialise()
{
	controller.add(Dog("labrador", "Puky", 2, "https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12231341/Labrador-Retriever-On-White-07.jpg"));
	controller.add(Dog("akita", "Fluffy", 3, "https://cdn.japantimes.2xx.jp/wp-content/uploads/2018/11/n-akita-a-20181128-870x688.jpg"));
	controller.add(Dog("labrador", "Max", 2, "https://previews.123rf.com/images/studiovandam/studiovandam1702/studiovandam170200114/71407250-labrador-puppy-on-a-white-background-the-labrador-retriever-also-labrador-is-a-type-of-retriever-gun.jpg"));
	controller.add(Dog("labrador", "Becky", 2, "https://www.telegraph.co.uk/content/dam/science/2018/10/21/TELEMMGLPICT000178469115_trans_NvBQzQNjv4BqpVlberWd9EgFPZtcLiMQfyf2A9a6I9YchsjMeADBa08.jpeg?imwidth=450"));
	controller.add(Dog("husky", "Roger", 2, "photo5"));
	controller.add(Dog("pechinez", "Cabral", 2, "photo6"));
	controller.add(Dog("rottweiler", "Shiro", 2, "photo7"));
	controller.add(Dog("golden", "Inej", 2, "photo8"));
	controller.add(Dog("pug", "Alecs", 2, "photo9"));
	controller.add(Dog("yorkshire", "Puppy", 2, "photo10"));

}



void Ui::viewAllDogs(int op){
	
	for (int i = 0; i < controller.getSize(); ++i) {
		//cout <<"aici1:"<< i;
		auto dog = controller.getAllDogs()[i];
		cout << dog.getName() << " - " << dog.getAge() << " - " << dog.getBreed() << " - " << dog.getPhoto() << endl;

		int option;
		
		
		cout << "\t\tPress -1- to adopt the dog"<<endl;
		cout << "\t\tPress -2- to view the next dog"<<endl;
		cout << "\t\tPress -3- to view the photo"<<endl;
		cout << "\t\tPress -0- to eixt"<<endl;
		cin >> option;

		if (option == 0) {
			//HTMLFileManager *htmlfile = new HTMLFileManager();
			//htmlfile->writeToFile(this->controller.getAdoptionList());
			break;
		}
		else if (option == 1) {
			controller.addToAdoptionList(Dog(dog.getBreed(), dog.getName(), dog.getAge(), dog.getPhoto()),op);
			//cout<<"aici2:"<<i;
		}
		else if (option == 3)
		{
			openLink(dog.getPhoto());
		}


		if (i == controller.getSize() - 1) {
			//cout << "aici3"<<i;
			i = -1;
		}
	}


}
void Ui::viewDogsFilter(int op){
	string breed;
	int age;
	cout << "\t\tGive the breed!";
	cin >> breed;
	cout << "\t\tGive the age!";
	cin >> age;

	for (int i = 0; i < controller.getSize(); ++i) {
		
		auto dog = controller.getAllDogs()[i];
		if (dog.compareBreed(breed) == 1 && dog.getAge() <= age)
		{
			cout << dog.getName() << " - " << dog.getAge() << " - " << dog.getBreed() << " - " << dog.getPhoto() << endl;

			int option;
			

			cout << "\t\tPress -1- to adopt the dog";
			cout << "\t\tPress -2- to view the next dog";
			cout << "\t\tPress -3- to open the photo";
			cout << "\t\tPress -0- to eixt";
			cin >> option;

			if (option == 0) {
				break;
			}
			else if (option == 1) {
				controller.addToAdoptionList(Dog(dog.getBreed(), dog.getName(), dog.getAge(), dog.getPhoto()),op);
			}
			else if (option == 3)
			{
				openLink(dog.getPhoto());
			}
		}
			if (i == controller.getSize() - 1) {
				i = -1;
			}
		
		
	}

}
void Ui::viewAdoptionList(){
	for (int i = 0; i < controller.getAdoptionList().size(); i++)
		cout << controller.getAdoptionList()[i].Tostring() << endl;
}
void Ui::MenuAdmin()
{
	cout << "\nYou are on ADMIN mode!\n";
	cout << "\t Press 1 to add a new dog... \n";
	cout << "\t Press 2 to remove a dog... \n";
	cout << "\t Press 3 to update an existing dog... \n";
	cout << "\t Press 4 to show all the dogs... \n";
	cout << "\t Press 0 to exit... \n";

}

void Ui::MenuUser()
{
	cout << "\nYou are on USER mode!\n";
	cout << "\t Press 1 to view the dogs, one by one \n";
	cout << "\t Press 2 to view the adoption list\n";
	cout << "\t Press 3 to see all dogs of a breed, smaller than an age given\n";
}

void Ui::run()
{	
	//initialise();

	



	int switchMode = 3, command = 1;
	//FileManager txtFileManager = FileManager();
	//txtFileManager.writeToFile(controller);
	//txtFileManager.loadFromFile(controller.getAllDogs());

	while (switchMode != 0)
	{
		cout << "Choose the mode you want to operate on.\n";
		cout << "\tPress 1 to enter ADMIN mode.\n";
		cout << "\tPress 2 to enter USER mode.\n";
		cout << "\tPress 0 to EXIT the application.\n";
		cin >> switchMode;
		if (switchMode == 1)
		{
			
			
				MenuAdmin();
				
				while (command != 0)
				{	
					cout << "\nEnter a command: ";
					cin >> command;

					if (command == 1)
					{
						string breed, name, photo;
						int age;
						//
						cout << "\t Enter a breed: ";
						//cin.getline(breed,256);
						//breed = this->readString();
						cin >> breed;
						cout << "\t Enter a name: ";
						//cin.getline(name,256);
						//name = this->readString();//this->readString();
						cin >> name;
						//name = "";
						//cin.get();
						cout << "\t Enter the age: ";
						cin >> age;
						//age = 0;
						cout << "\t Enter a photo: ";
						//cin.getline(photo, 256);
						//photo = this->readString();
						cin >> photo;
						//int ok = controller.add(Dog(breed, name, age, photo));
						try {
							int ok = controller.add(Dog(breed, name, age, photo));
							if (ok == -1)
								cout << "\t Dog already exists!";
							else if(ok!=0)
								cout << "\t Dog added!";
						}
						
						catch (MyRepoException &e) {
							cout << e.getMessage();
						}
							//scout << msg << endl;
					}
						//if (ok == 1)
						//{
							//cout << "\t Dog added!";
							//txtFileManager.writeToFile(controller.getAllDogs());
						//}
						//else
							//cout << "Couldn't add the dog! Make sure all data is correct!";
					
					else
						if (command == 2)
						{
							string name;
							cout << "\t Enter the name of the dog you want to delete: ";
							cin >> name;
							controller.remove(name);
							//txtFileManager.writeToFile(controller.getAllDogs());
						}
						else
							if (command == 3)
							{
								string name, new_name;
								cout << "\t Enter the name of the dog you want to update: ";
								cin >> name;
								cout << "\t Enter the new name: ";
								cin >> new_name;
								controller.update(name, new_name);
								//txtFileManager.writeToFile(controller.getAllDogs());
							}
							else
								if (command == 4)
								{
									for (int i = 0; i < controller.getSize(); i++)
										cout << controller.getAllDogs()[i].Tostring()<<endl;
								
								}
								else
									if(command!=0)
										cout << "Invalid command! Try again!";

				}
		}
		else
			if (switchMode == 2)
			{
				cout << "First you must choose what kind of files you will use(For the adoption list)!!" << endl;
				cout << "Press 1 for text files.";
				cout << endl << "Press 2 for html files!";
				int op;
				cin >> op;
				


				MenuUser();
				command = -1;
				while (command != 0)
				{

					
					cout << "\nEnter a command: ";
					cin >> command;
					if (command == 1)
					{
						viewAllDogs(op);
					}
					else
						if (command == 2) {
							viewAdoptionList();
							//string docType = "html";
							//string path= "C:\Users\Admin\Desktop\Assignment 5 - 6\Assignment 5 - 6\htmlFile.html";
						//	string sysComand;
							//sysComand = docType + path;
							//system("C:\Users\Admin\Desktop\Assignment 5 - 6\Assignment 5 - 6\htmlFile.html");
							if (op == 1)
								system("start fisierAdoptie.txt");
							else if(op == 2) 
								system("start htmlFile.html");
							//system("open C:\Users\Admin\Desktop\Assignment 5 - 6\Assignment 5 - 6\htmlFile.html");
							//ShellExecute(NULL, "open", "C:\Users\Admin\Desktop\Assignment 5 - 6\Assignment 5 - 6\htmlFile.html", NULL, NULL, SW_SHOWNORMAL);
						}
						else
							if (command == 3)
							{
								if (op == 1)
									viewDogsFilter(op);
								else
									viewDogsFilter(op);

							}
				}
			}
			else
				if(switchMode!=0)
					cout << "Invalid mode. Try again!";
	}
	
}

Ui::~Ui()
{
	//this->controller.~Controller();
}

string Ui::readString()
{

	char input[256];
	cin.getline(input, 256);
	cout << input;
	return input;
}
