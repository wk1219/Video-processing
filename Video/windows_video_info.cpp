#include <iostream>
#include <windows.h>
#include <locale>
#include <string.h>
#include <opencv2/opencv.hpp>

#pragma warning(disable: 4996)
using namespace std;
using namespace cv;

void FileList(char *path, char *ppath) {
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
				FileList(newpath, ppath);
			}
		}
		else {
			cout << drive << dir << wfd.cFileName << endl;
			strcat(ppath, wfd.cFileName);
			VideoCapture cap(ppath);
			int width = cvRound(cap.get(CAP_PROP_FRAME_WIDTH));
			int height = cvRound(cap.get(CAP_PROP_FRAME_HEIGHT));
			double fps = cap.get(CAP_PROP_FPS);
			int fcount = cvRound(cap.get(CAP_PROP_FRAME_COUNT));
			fileSize = (((int)wfd.nFileSizeHigh) << 32) + wfd.nFileSizeLow;
		
			cout << "File Name : " << wfd.cFileName << endl;
			cout << "File Size : " << fileSize << " Byte" << endl;
			// cout << "Length : " << wfd.dwFileAttributes << endl;
			// cout << "Make time : " << wfd.ftCreationTime << endl;
			cout << "Resolution : " << width << "X" << height << endl;
			cout << "File Path : " << ppath << endl;

			cout << "FPS : " << fps << endl;
			cout << "Frame Count : " << fcount << endl;


			// cout << GetFileAttributes(wfd.cFileName) << endl;
		}
		bResult = FindNextFile(hSrch, &wfd);
	}
	FindClose(hSrch);
}

void main()
{
	//std::locale::global(std::locale("ko_KR.UTF-8"));
	// char Path[MAX_PATH];
	// GetWindowsDirectory(Path, MAX_PATH);   // System Directory (Windows)
	char Path[100] = "Path";
	char path[100] = "ppath";

	strcat(Path, "\\*.*");
	FileList(Path, path);
	// cout << "MAX_PATH : "<< Path << endl;
}