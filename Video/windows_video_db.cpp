#include <iostream>
#include <windows.h>
#include <locale>
#include <string.h>
#include <cstdlib>
#include <mysql.h>
#include <list>
#include <opencv2/opencv.hpp>
#pragma warning(disable: 4996)
#pragma comment(lib, "libmysql.lib") 

#define DB_HOST "localhost"
#define DB_USER "root"
#define DB_PW "mt4714573"
#define DB_NAME "web"

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

	int getNum() {
		return this->num;
	}

	char* getName() {
		return this->fileName;
	}

	int getSize() {
		return this->fileSize;
	}

	char* getLength() {
		return this->fileLength;
	}

	char* getMakeTime() {
		return this->makeTime;
	}

	char* getResolution() {
		return this->resolution;
	}

	char* getUrl() {
		return this->url;
	}

	void printInfo() {
		cout << "--------------------------------------------" << endl;
		cout << "NUM : " << getNum() << endl;
		cout << "FileName : " << getName() << endl;
		cout << "FileSize : " << getSize() << " Byte" << endl;
		cout << "FileLength : " << getLength() << endl;
		cout << "MakeTime : " << getMakeTime() << endl;
		cout << "Resolution : " << getResolution() << endl;
		cout << "Path : " << getUrl() << endl;
		cout << "--------------------------------------------" << endl;
	}
};
void db_insert(Video vid);
void db_select();

void FileList(char* path, char* filepath) {
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

			//vid.setVideo(num, wfd.cFileName, fileSize, vidLength, vidMakeTime, vidResolution, filepath);	// Set Video Object
			vid.setVideo(num, wfd.cFileName, fileSize, vidLength, vidMakeTime, vidResolution, filepath);
			vid.printInfo();		// Print Video Info
			db_insert(vid);
			//db_select();

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
void db_insert(Video vid) {
	MYSQL mysql;
	MYSQL_RES* res;
	MYSQL_ROW row;
	int fields;
	int i;
	list <string> vlist;
	list<string>::iterator iter;
	MYSQL_FIELD* field;
	char buf[255];

	mysql_init(&mysql);

	mysql_real_connect(&mysql, DB_HOST, DB_USER, DB_PW, DB_NAME, 3306, NULL, 0);
	sprintf(buf, "insert into web.video values""('%d', '%s', '%d', '%s', '%s', '%s', '%s')",
		vid.getNum(), vid.getName(), vid.getSize(), vid.getLength(), vid.getMakeTime(), vid.getResolution(), vid.getUrl());
	mysql_query(&mysql, buf);
	cout << "Insert Success!!" << endl;
}
 void db_select() {
	MYSQL mysql;
	MYSQL_RES* res;
	MYSQL_ROW row;
	int fields;
	int i;
	list <string> vlist;
	list<string>::iterator iter;
	MYSQL_FIELD* field;

	mysql_init(&mysql);
	mysql_real_connect(&mysql, DB_HOST, DB_USER, DB_PW, DB_NAME, 3306, NULL, 0);
	mysql_query(&mysql, "SELECT * FROM video");
	res = mysql_store_result(&mysql);
	fields = mysql_num_fields(res);

	while (row = mysql_fetch_row(res))
	{
		for (i = 0; i < fields; i++) {
			cout << row[i] << ' ';
			vlist.push_back(row[i]);
		}
		cout << endl;
	}
	cout << endl;

	for (iter = vlist.begin(); iter != vlist.end(); ++iter) {
		cout << *iter << ' ';
	}
	mysql_free_result(res);
	mysql_close(&mysql);
}
int main()
{
	char Path[100] = "C:\\Users\\sjms1\\Desktop\\Video\\";
	char filePath[100] = "C:\\Users\\sjms1\\Desktop\\Video";
	
	strcat(Path, "\*.*");
	FileList(Path, filePath);
}