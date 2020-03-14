#include <iostream>
#include <windows.h>
#include <locale>
#include <string.h>
#include <cstdlib>
#include <opencv2/opencv.hpp>

#pragma warning(disable: 4996)
using namespace std;
using namespace cv;
class Video {
private:
	int num;
	char fileName[25];
	int fileSize;
	char fileLength[10];
	char makeTime[30];
	char resolution[10];
	char url[100];

public:

	void setVideo(int _num, char* _fileName, int _fileSize, char* _fileLength, char* _makeTime, char* _resolution, char* _url) 
	{
		this->num = _num;
		strcpy(this->fileName, _fileName);
		this->fileSize = _fileSize;
		strcpy(this->fileLength, _fileLength);
		strcpy(this->makeTime, _makeTime);
		strcpy(this->resolution, _resolution);
		strcpy(this->url, _url);
	}
	
	void printInfo() {
		cout << "--------------------------------------------" << endl;
		cout << "Num : " << num << endl;
		cout << "FileName : " << fileName << endl;
		cout << "FileSize : " << fileSize << " Byte" << endl;
		cout << "FileLength : " << fileLength << endl;
		cout << "MakeTime : " << makeTime << endl;
		cout << "Resolution : "<< resolution << endl;
		cout << "Path : " << url << endl;
		cout << "--------------------------------------------" << endl;
	}
};

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
	int num = 1;

	cout << "Search Path = " << path << endl;
	hSrch = FindFirstFile(path, &wfd);
	if (hSrch == INVALID_HANDLE_VALUE) {
		return;
	}

	_splitpath(path, drive, dir, NULL, NULL);
	while (bResult) {
		Video vid = Video();
		if (wfd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
			if (strcmp(wfd.cFileName, ".") && strcmp(wfd.cFileName, "..")) {
				cout << newpath << drive << dir << wfd.cFileName << endl;

				cout << "File Size : " << fileSize << endl;
				FileList(newpath, filepath);
			}
		}
		else {
			sprintf(filepath, "%s%s%s", drive, dir, wfd.cFileName);	// Combine path
			FileTimeToSystemTime(&wfd.ftCreationTime, &utc);
			SystemTimeToTzSpecificLocalTime(NULL, &utc, &lt);

			VideoCapture cap(filepath);
			int width = cvRound(cap.get(CAP_PROP_FRAME_WIDTH));		// Video Info : Frame Width  (Resolution)
			int height = cvRound(cap.get(CAP_PROP_FRAME_HEIGHT));	// Video Info : Frame Height (Resolution)
			double fps = cap.get(CAP_PROP_FPS);						// Video Info : FPS
			int fcount = cvRound(cap.get(CAP_PROP_FRAME_COUNT));	// Video Info : Frame Count
			int length = fcount / fps;								// Video Info : Length (Time)

			char vidMakeTime[100];	
			char vidLength[10];
			char vidResolution[20];

			sprintf(vidLength, "%d", length);						// Convert Integer to String
			fileSize = (((int)wfd.nFileSizeHigh) << 32) + wfd.nFileSizeLow;
			sprintf(vidMakeTime, "%d-%02d-%02d %02d:%02d:%02d", lt.wYear, lt.wMonth, lt.wDay, lt.wHour, lt.wMinute, lt.wMinute);	// Convert creationTime Format
			sprintf(vidResolution, "%dX%d", width, height);			// Combine Width & Height

			vid.setVideo(num, wfd.cFileName, fileSize, vidLength, vidMakeTime, vidResolution, filepath);	// Set Video Object
			vid.printInfo();		// Print Video Info

			/*
			cout << "FPS : " << fps << endl;
			cout << "Frame Count : " << fcount << endl;
			cout << "-------------------------------------------" << endl;
			*/
			num++;
		}
		bResult = FindNextFile(hSrch, &wfd);
	}
	FindClose(hSrch);
}

int main()
{
	char Path[100] = "Path";
	char filePath[100] = "filePath";

	strcat(Path, "\\*.*");
	FileList(Path, filePath);
}