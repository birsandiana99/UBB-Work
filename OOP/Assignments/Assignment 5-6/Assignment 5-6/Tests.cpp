#include "Tests.h"
#include <assert.h>
#include "DynamicVector.h"
#include <iostream>
Tests::Tests()
{
}

void Tests::testDynamicVector()
{
	DynamicVector<Dog> d = DynamicVector<Dog>();
	assert(d.getCap() == 10);
	Dog d1 = Dog("abc", "aaa", 12, "ph1");
	d.add(d1);
	assert(d.getSize() == 1);

	d.deleteElem(0);
	assert(d.getSize() == 0);

	d.add(d1);
	assert(d[0].getAge() == d1.getAge());

	DynamicVector<Dog> dv2 = DynamicVector<Dog>(d);
	assert(dv2.getSize() == 1);

	DynamicVector<Dog> dv3 = DynamicVector<Dog>();
	Dog dog1 = Dog("abc", "aaa", 12, "ph1");
	Dog d2 = Dog("fsd", "aaa", 12, "ph1");
	Dog d3 = Dog("afsdfdsbc", "aaa", 12, "ph1");
	Dog d4 = Dog("aebc", "aaa", 12, "ph1");
	Dog d5 = Dog("adsbc", "aaa", 12, "ph1");
	Dog d6 = Dog("abaaac", "aaa", 12, "ph1");
	Dog d7 = Dog("abvvc", "aaa", 12, "ph1");
	Dog d8 = Dog("abccc", "aaa", 12, "ph1");
	Dog d9 = Dog("abwwc", "aaa", 12, "ph1");
	Dog d10 = Dog("aqwbc", "aaa", 12, "ph1");
	Dog d11= Dog("abcre", "aaa", 12, "ph1");
	dv3.add(dog1);
	dv3.add(d2);
	dv3.add(d3);
	dv3.add(d4);
	dv3.add(d5);
	dv3.add(d6);
	dv3.add(d7);
	dv3.add(d8);
	dv3.add(d9);
	dv3.add(d10);
	dv3.add(d11);

	DynamicVector<Dog> dv4 = DynamicVector<Dog>();
	dv4 = dv3;

	assert(dv4.getSize() == 11);
	const string str1 = "aaa";
	int i = dv4.searchElem(str1);
//	cout << i;
	assert(i==0);

	dv4.updateElem(0, "bbc", "aaa", 12, "ph1");
	assert(dv4[0].getName().compare("bbc")==0);


	assert(dv4.getArray()[0].getAge()== 12);
	DynamicVector<Dog> dv5 = DynamicVector<Dog>();
	dv5.add(Dog("asa", "asda", 12, "asdsa"));
	dv4 = dv4 + dv5;
	assert(dv4.getSize() == 12);
	//dv4 = dv4 + Dog("22", "34f", 1, "fre");
	//dv4 = Dog("22", "34f", 1, "fre") + dv4;

	dv4.deleteElem(10);
	assert(dv4.getSize() == 11);
	assert(dv4.searchElem("sdsdwefrege") == -1);
}

void Tests::testController()
{
	Controller c = Controller();
	Dog d1 = Dog("fsd", "aada", 12, "ph1");
	Dog d2 = Dog("afsdfdsbc", "argergaa", 12, "ph1");
	Dog d3 = Dog("aebc", "name2", 12, "ph1");
	Dog d4 = Dog("adsbc", "sf", 12, "ph1");
	Dog d5 = Dog("abaaac", "32", 12, "ph1");
	Dog d6 = Dog("abvvc", "6543", 12, "ph1");
	Dog d7 = Dog("abccc", "134", 12, "ph1");
	Dog d8 = Dog("abwwc", "name22", 12, "ph1");
	Dog d9 = Dog("aqwbc", "54", 12, "ph1");
	Dog d10 = Dog("abcre", "123", 12, "ph1");
	c.add(d1);
	c.add(d2);
	c.add(d3);
	c.add(d4);
	c.add(d5);
	c.add(d6);
	c.add(d7);
	c.add(d8);
	c.add(d9);
	c.add(d10);
	c.add(d1);
	assert(c.add(d1) == -1);
	assert(c.remove("efihowi") == -1);
	c.remove("wgwrgvsd");

	assert(c.alreadyExists("name2") == 1);
	assert(c.getAllDogs().size() == 10);
	//c.addToAdoptionList(d1);
	//assert(c.addToAdoptionList(d1) == -1);
	
//	c.addToAdoptionList(d1);

	//c.addToAdoptionList(d2);
//	assert(c.getAdoptionList().size() == 2);


	
	c.remove("123");
	assert(c.getAllDogs().size() == 9);

	assert(c.update("name2", "newName")==1);
	assert(c.getAllDogs()[2].getName() == "newName");



}

void Tests::testDog()
{
	Dog dog1 = Dog("abc", "aaa", 12, "ph1");
	assert(dog1.getName() == "aaa");
	assert(dog1.getBreed() == "abc");
	assert(dog1.getAge() == 12);
	assert(dog1.getPhoto()=="ph1");

	dog1.setAge(10);
	dog1.setBreed("breed");
	dog1.setName("ana");
	dog1.setPhoto("photo");

	assert(dog1.compareBreed("breed") == 1);
	assert(dog1.compareBreed("breedsfd") == 0);

	assert(dog1.getName() == "ana");
	assert(dog1.getBreed() == "breed");
	assert(dog1.getAge() == 10);
	assert(dog1.getPhoto() == "photo");

	string s = dog1.Tostring();


}

void Tests::testRepo()
{
	Repository r = Repository();
	r.add(Dog("breed", "name", 1, "photo"));
	assert(r.getLen() == 1);
}




void Tests::runAll()
{
	testDog();
	testDynamicVector();
	testController();
	testRepo();
}

Tests::~Tests()
{
}
