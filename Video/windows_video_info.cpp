#include <iostream>
#include <windows.h>
#include <locale>
#include <string.h>
#include <cstdlib>
#include <opencv2/opencv.hpp>

#pragma warning(disable: 4996)
using namespace std;
using namespace cv;

void FileList(char *path, char *filepath) {
	WIN32_FIND_DATA wfd;
	HANDLE hSrch;
	SYSTEMTIME utc, lt;
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
				FileList(newpath, filepath);
			}
		}
		else {
			//cout << drive << dir << wfd.cFileName << endl;
			sprintf(filepath, "%s%s%s", drive, dir, wfd.cFileName);
			FileTimeToSystemTime(&wfd.ftCreationTime, &utc);
			SystemTimeToTzSpecificLocalTime(NULL, &utc, &lt);
			VideoCapture cap(filepath);
			int width = cvRound(cap.get(CAP_PROP_FRAME_WIDTH));
			int height = cvRound(cap.get(CAP_PROP_FRAME_HEIGHT));
			double fps = cap.get(CAP_PROP_FPS);
			int fcount = cvRound(cap.get(CAP_PROP_FRAME_COUNT));
			char creationTime[100];
			int length = fcount / fps;
			fileSize = (((int)wfd.nFileSizeHigh) << 32) + wfd.nFileSizeLow;
			sprintf(creationTime, "%d-%02d-%02d %02d:%02d:%02d", lt.wYear, lt.wMonth, lt.wDay, lt.wHour, lt.wMinute, lt.wMinute);
			
			// Print Video Info
			cout << "-------------------------------------------" << endl;
			cout << "File Name : " << wfd.cFileName << endl;
			cout << "File Size : " << fileSize << " Byte" << endl;
			cout << "Length : " << length << endl;
			cout << "MK time : " << creationTime << endl;
			cout << "Resolution : " << width << "X" << height << endl;
			cout << "File Path : " << filepath << endl;

			cout << "FPS : " << fps << endl;
			cout << "Frame Count : " << fcount << endl;
			cout << "-------------------------------------------" << endl;
		}
		bResult = FindNextFile(hSrch, &wfd);
	}
	FindClose(hSrch);
}

void main()
{
	char Path[100] = "C:\\Users\\sjms1\\Desktop\\video";
	char filepath[100] = "C:\\Users\\sjms1\\Desktop\\video\\";

	strcat(Path, "\\*.*");
	FileList(Path, filepath);
}