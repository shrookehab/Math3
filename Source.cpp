#include <iostream>
#include <string>

using namespace std;
int main()
{
	int c = 0, y, z;
	bool x = true;
	string s, s1, s2;
	getline(cin, s);
	//////////////////////////////
	while (1) {
		if (s.find("not") != -1) {
			if (s.find("not") == 0) {
				y = s.find("not");
				s.insert(y + 5, ")");
				s.replace(0, 3, "( ! ");
			}
			else {
				y = s.find("not");
				s.insert(y - 1, "(");
				s.insert(y + 6, ")");
				s.replace(s.find("not"), 3, "! ");
			}
		}
		else break;
	}
	/////////////////////////////
	while (1) {
		if (s.find("and") != -1) {
			y = s.find("and");
			if (y == 2) {
				//z = s.size();
				//s.copy(s1, z, 0);
				s1.insert(0, "(");
				s1.append(s, 0, 7);
				s1.insert(8, ")");
				s.replace(0, 7, s1);
				s.replace(s.find("and"), 3, "&&");

				//s1.swap(s2);

				s1 = "";


			}
			else {
				s.insert(y - 2, "(");
				s.insert(y + 6, ")");
				s.replace(s.find("and"), 3, "&&");
			}
		}
		else break;
	}
	/////////////////////////////
	while (1) {
		if (s.find("or") != -1) {
			y = s.find("or");
			if (y == 2) {
				//z = s.size();
				//s.copy(s1, z, 0);
				s1.insert(0, "(");
				s1.append(s, 0, 6);
				s1.insert(7, ")");
				s.replace(0, 6, s1);
				s.replace(s.find("or"), 2, "||");

				//s1.swap(s2);

				s1 = "";
			}
			else {



				s.insert(y - 3, "(");
				s.insert(y + 5, ")");
				s.replace(s.find("or"), 2, "||");
			}
		}
		else break;
	}
	/////////////////////////////
	while (1) {
		if (s.find("imply") != -1) {
			y = s.find("imply");
			if (y == 2) {
				//z = s.size();
				//s.copy(s1, z, 0);
				s1.insert(0, "(");
				s1.append(s, 0, 9);
				s1.insert(10, ")");
				s.replace(0, 9, s1);
				s.replace(s.find("imply"), 5, "->");

				//s1.swap(s2);

				s1 = "";
			}
			else {

				s.insert(y - 3, "(");
				s.insert(y + 8, ")");
				s.replace(s.find("imply"), 5, "->");
			}
		}
		else
			break;
	}
	/////////////////////////////
	while (1) {
		if (s.find("iff") != -1) {
			y = s.find("iff");
			if (y == 2) {
				//z = s.size();
				//s.copy(s1, z, 0);
				s1.insert(0, "(");
				s1.append(s, 0, 7);
				s1.insert(8, ")");
				s.replace(0, 7, s1);
				s.replace(s.find("iff"), 3, "<->");

				//s1.swap(s2);

				s1 = "";


			}
			else {


			s.insert(y - 3, "(");
			s.insert(y + 6, ")");
			s.replace(s.find("iff"), 3, "<->");
		}
	}
		else break;
	}
	/////////////////////////////
	while (1) {
		if (s.find("xor") != -1) {
			y = s.find("xor");
			if (y == 2) {
				//z = s.size();
				//s.copy(s1, z, 0);
				s1.insert(0, "(");
				s1.append(s, 0, 7);
				s1.insert(8, ")");
				s.replace(0, 7, s1);
				s.replace(s.find("xor"), 3, "+||");

				//s1.swap(s2);

				s1 = "";


			}
			else {


				s.insert(y - 3, "(");
				s.insert(y + 6, ")");
				s.replace(s.find("xor"), 3, "+||");
			}
		}
		else break;
	}
	///////////////////////////////////////
	cout << s << endl << s1 << endl;
	system("pause");
	return 0;
}

