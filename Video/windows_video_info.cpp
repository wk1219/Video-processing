#include <iostream>
#include <windows.h>
#include <locale>
#pragma warning(disable: 4996)
using namespace std;

void FileList(char *path) {
	WIN32_FIND_DATA wfd;
	HANDLE hSrch;
	BOOL bResult = TRUE;
	char drive[_MAX_DRIVE];
	char dir[MAX_PATH];
	char newpath[MAX_PATH];
	char file[MAX_PATH];
	int fileSize = -1;
	cout << "Search Path = " << path << endl;
	hSrch = FindFirstFile(path, &wfd);
	if (hSrch == INVALID_HANDLE_VALUE) {
		return;
	}
	_splitpath(path, drive, dir, NULL, NULL);
	while (bResult) {
		if (wfd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
			if (strcmp(wfd.cFileName, ".") && strcmp(wfd.cFileName, "..")) {
				cout << newpath << drive << dir << wfd.cFileName << endl;

				cout << "File Size : " << fileSize << endl;
				FileList(newpath);
			}
		}
		else {
			cout << drive << dir << wfd.cFileName << endl;
			fileSize = (((int)wfd.nFileSizeHigh) << 32) + wfd.nFileSizeLow;
			cout << "File Name : " << wfd.cFileName << endl;
			cout << "File Size : " << fileSize << " Byte" << endl;
			cout << "Length : " << endl;
			//cout << "Make time : " << wfd.ftCreationTime << endl;
			cout << "Resolution : " << endl;
		}
		bResult = FindNextFile(hSrch, &wfd);
	}
	FindClose(hSrch);
}

void main()
{
	std::locale::global(std::locale("ko_KR.UTF-8"));
	// char Path[MAX_PATH];
	// GetWindowsDirectory(Path, MAX_PATH);   // System Directory (Windows)
	char Path[100] = "C:\\Users\\sjms1\\Desktop\\video";

	strcat(Path, "\\*.*");
	FileList(Path);
	// cout << "MAX_PATH : "<< Path << endl;
}