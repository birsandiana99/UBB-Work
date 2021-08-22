#include "ui.h"
#include "contr.h"
#include "domain.h"
#include <stdio.h>
#include <string.h>
#include "test.h"
#include "validate.h"


void menu()
{
	printf("Press 1. to add an offer...\n");
	printf("Press 2. to delete an offer...\n");
	printf("Press 3. to update an offer...\n");
	printf("Press 4. to show all the offers...\n");
	printf("Press 5. to view all the offers with the address containing a certain string...\n");
	printf("Press 6. for a given surface display all offers sorted ascending by price... \n");
	printf("Press 7. to view all the offers having a given type with the surface greater than a value...\n");
	printf("Press 8. to undo the last operation...\n");
	printf("Press 9. to redo the last operation...\n");
	printf("Press 0. to continue...\n");
}

void printOffers()
{
	if (offers->size == 0)
	{
		printf("There are no offers!\n");
		return;
	}

	int i;
	for (i = 0; i < offers->size; ++i)
		printf("%d. Type: %s // Address: %s // Surface: %d // Price: %d\n", i + 1, offers->arr[i]->type, offers->arr[i]->address, offers->arr[i]->surface, offers->arr[i]->price);

	printf("\n");
}


void run()
{
	
	/*
	testValidator();
	testAdd();
	testUpdate();
	testDelete();
	testFound();
	testUndo();
	*/
	runController();
	initialise_offers();

	/*c_updatePrice("adr1", 123444, 1);
	printOffers();
	undoOperation();
	printOffers();
	redoOperation();
	printOffers();
	*/
	//int v1[500];
	//int n = c_viewOffersType("apartment", 1200, v1);

	int option = 1;
	while (option != 0)
	{
		menu();
		printf("\nChoose an option from above...");
		scanf_s("%d", &option);
		printf("\n");
		if (option == 1)
		{
			char type[50]="", address[50]="";
			int price, surface;

			printf("\t Insert the offer's type: ");
			scanf_s("%s", &type,50);
			printf("\n");
			if (validateType(type) == -1)
				printf("\t Invalid type(must be house, penthouse or apartment! \n");

			else
			{

				printf("\t Insert the offer's address: ");
				scanf_s("%s", &address, 50);
				printf("\n");

				if (validateAddress(address) == -1)
					printf("\t Address field cannot be void! \n");
				else
				{
					if (c_find(address)> -1)
						printf("\t Offer coult not be added! Address already exists. \n");

					else
					{
						printf("\t Insert the offer's surface: ");
						scanf_s("%d", &surface);
						printf("\n");
						if (validateSurface(surface) == -1)
							printf("\t Invalid surface! It must be greater than 0! \n");
						else
						{
							printf("\t Insert the offer's price: ");
							scanf_s("%d", &price);
							printf("\n");
							
							if (validatePrice(price) == -1)
								printf("\t Price must be greater than 0! \n");
							else
							{ 
								addOffer(type, address, surface, price,1);
								printf("\t Offer added successfully! \n");
								printf("\n");
							}
							
						}
						

					}
				}
			}
		}
		else
			if(option == 2)
			{
				char address[50] = "";
				printf("\t Insert the address of the real estate you want to delete: ");
				scanf_s("%s", &address, 50);
				printf("\n");


				if (c_delete(address,1) == -1)
					printf("\t Offer could not be deleted! Address does not exist! \n");
				else
					printf("\t Offer deleted successfully! \n \n");

			}
			else
				if (option == 3)
				{
					char address[50] = "";
					printf("\t Enter the address of the real estate you want to update: ");
					scanf_s("%s", &address, 50);
					printf("\n");
					if (c_find(address) == -1)
						printf("\t Address does not exist! \n");
					else
					{
						char s[3] = "";
						printf("\t Press p to update its price...\n");
						printf("\t Press s to update its surface...\n");
						printf("\t Enter an option: ");
						scanf_s("%s", &s, 3);
						printf("\n");
						if (strcmp(s, "p") == 0)
						{
							int price;
							printf("\t Enter the new price: ");
							scanf_s("%d", &price);
							c_updatePrice(address, price,1);

						}
						else
							if (strcmp(s, "s") == 0)
							{
								int surface;
								printf("\t Enter the new surface: ");
								scanf_s("%d", &surface);
								c_updateSurface(address, surface,1);
							}
							else
								printf("\t Invalid command!");


					}
					

				}
				else 
					if (option == 4)
					{
						printOffers();
					}
					else
						if (option == 5)
						{
							char s[50];
							printf("\t Insert the substring you want to search for: ");
							scanf_s("%s", &s, 50);
							printf("\n");
							int ct = 0;
							for (int i = 0; i <= offers->size-1; i++)
							{
								//printf("%d \n",i);
								int ok = c_substring(i, s);
								//printf("%d", i);
								if (ok == 1)
								{
									ct++;
									printf("\t %d. Type: %s // Address: %s // Surface: %d // Price: %d\n", i + 1, offers->arr[i]->type, offers->arr[i]->address, offers->arr[i]->surface, offers->arr[i]->price);
								}
							}
							if (ct == 0)
								printf("\t No real estates with the given property!\n");
							printf("\n");
						}
						else
							if (option == 6)
							{
								int n, surface;
								printf("\t Enter a surface: ");
								scanf_s("%d", &surface);
								printf("\n");
								int v[100];
								n = display_surface(surface, v);
								for (int i = 0; i <n; i++)
								{
										printf("\t %d. Type: %s // Address: %s // Surface: %d // Price: %d\n", i + 1, offers->arr[v[i]]->type, offers->arr[v[i]]->address, offers->arr[v[i]]->surface, offers->arr[v[i]]->price);
								}
							}
							else
								if (option == 7)
								{
									char type[50] = "";
									int surface;

									printf("\t Insert the offer's type: ");
									scanf_s("%s", &type, 50);
									printf("\n");
									if (validateType(type) == -1)
										printf("\t Invalid type(must be house, penthouse or apartment! \n");
									else
									{
										printf("\t Insert the offer's surface: ");
										scanf_s("%d", &surface);
										printf("\n");
										if (validateSurface(surface) == -1)
											printf("\t Invalid surface! It must be greater than 0! \n");
										else
										{
											int v[100];
											int n = c_viewOffersType(type, surface, v);
											if (n == 0)
											{
												printf("No offers with the given property");
											}
											else
											{
												for(int i=0;i<n;i++)
													printf("%d. Type: %s // Address: %s // Surface: %d // Price: %d\n", i + 1, offers->arr[v[i]]->type, offers->arr[v[i]]->address, offers->arr[v[i]]->surface, offers->arr[v[i]]->price);
											}
										}
									}
								}
								else
									if (option == 8)
									{
										int ok = undoOperation();
										if (ok == -1)
											printf("Undo failed!\n");
										else
											printf("Success!");

										printf("\n");
									}
									else
										if (option == 9)
										{
											int ok = redoOperation();
											if (ok == -1)
												printf("Redo Failed!\n");
											else
												printf("Success!");
										}
										else
											if(option != 0)
												printf("InvalidCommand");
					


	}

	

	







	/*
	addOffer("house", "ads3423", 42342, 342);
	addOffer("house", "astadsfds", 6666, 342);
	addOffer("house", "adfasta", 42342, 666);
	addOffer("house", "ads3asta423", 111111, 342);
	addOffer("house", "ads3423", 42342, 342);
	addOffer("house", "ads3423", 42342, 342);

	
	initialise_offers();
	c_delete("adr1");
	c_updatePrice("adr2", 123123);
	c_updateSurface("adr3", 696969);

	printOffers();


	for (int i = 0; i <= offers->size; i++)
	{
		int ok = c_substring(i, "asta");
		if (ok == 1)
		{
			printf("%d. Type: %s // Address: %s // Surface: %d // Price: %d\n", i + 1, offers->arr[i]->type, offers->arr[i]->address, offers->arr[i]->surface, offers->arr[i]->price);
		}
	}
	*/







}
