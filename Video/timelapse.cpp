#include  <iostream>
#include  <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

#define input 'input video'
#define output 'output video'
#define startFrame 125
#define endFrame 325

int main()
{

	int iCurrentFrame = 0;

	VideoCapture vc = VideoCapture(input);

	if (!vc.isOpened())
	{
		cerr << "fail to open the video" << endl;
		return EXIT_FAILURE;
	}

	double fps = vc.get(CAP_PROP_FPS);
	int width = (int)vc.get(CAP_PROP_FRAME_WIDTH);
	int height = (int)vc.get(CAP_PROP_FRAME_HEIGHT);

	VideoWriter vw(output,cv::VideoWriter::fourcc('D', 'I', 'V', 'X'), fps, Size(width, height));

	if ((startFrame < 0 || startFrame >= vc.get(CAP_PROP_FRAME_COUNT)) ||
		(endFrame < 0 || endFrame >= vc.get(CAP_PROP_FRAME_COUNT)))
	{
		cerr << "wrong frame" << endl;
		return EXIT_FAILURE;
	}
	vc.set(CAP_PROP_POS_FRAMES, startFrame);
	while (true)
	{
		if (iCurrentFrame > (endFrame - startFrame))
			break;
		iCurrentFrame++;

		Mat frame;
		vc >> frame;
		cout << frame << endl;
		if (frame.empty())
			break;

		vw.write(frame);
		imshow("image", frame);
		waitKey(1);
	}

	vw.release();

	return EXIT_SUCCESS;
}


