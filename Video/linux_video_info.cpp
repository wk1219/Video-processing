#include <iostream>
#include <io.h>
#include <sys/stat.h>
#include <sys/types.h>
using namespace std;

int main(void) {
	struct stat* buf = nullptr;
	stat("C:\\Users\\sjms1\\Desktop", buf);
	if (buf->st_mode & S_IFREG)
		cout << "regular file" << endl;
	else if (buf->st_mode & S_IFDIR)
		cout << "directory" << endl;
	else
		cout << "other file" << endl;

	
}