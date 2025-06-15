#include <graphics.h>
#include <conio.h>

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "c:\\TurboC\\WinRoot\\TURBOC3\\BGI");

    // Draw a rectangle
    rectangle(100, 100, 300, 200); // (left, top, right, bottom)

    // Draw a circle
    circle(200, 300, 50); // (centerX, centerY, radius)

    getch();      // Wait for key press
    closegraph(); // Close graphics window
    return 0;
}