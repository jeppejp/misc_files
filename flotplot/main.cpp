#include <iostream>
#include <curses.h>
#include <vector>
#include <algorithm>


typedef std::vector< std::pair<int, int> > timedata;
typedef std::vector< std::pair<int, int> > plotdata;

timedata test_data(void)
{
    timedata v;
    v.push_back(std::make_pair(1,10));
    v.push_back(std::make_pair(2,40));
    v.push_back(std::make_pair(3,30));
    v.push_back(std::make_pair(4,40));
    v.push_back(std::make_pair(5,60));
    v.push_back(std::make_pair(6,40));
    v.push_back(std::make_pair(7,40));
    
    return v;
}

void getMinMax(timedata td, int& xmin, int& xmax, int& ymin, int& ymax)
{
    // PLEASE FIX THIS HORRIBLE SLOW FUNCTION    
    std::vector<int> x,y;
    std::vector< std::pair<int,int> >::iterator it; 
    for (it = td.begin(); it != td.end(); ++it)
    {
        x.push_back((*it).first);
        y.push_back((*it).second);
    }
    xmin = *std::min_element(x.begin(), x.end());
    xmax = *std::max_element(x.begin(), x.end());
    ymin = *std::min_element(y.begin(), y.end());
    ymax = *std::max_element(y.begin(), y.end());
}

plotdata genPlotData(timedata tdata)
{

    int xmin, xmax, ymin, ymax;
    getMinMax(tdata, xmin, xmax, ymin, ymax);


    int offset = 48;
    int max_width = 150;

    int plot_height = ymax - ymin;
    int plot_length = xmax - xmin;
    float yscale = float(offset) / float(plot_height);
    float xscale = float(max_width) / float(plot_length);

    std::vector< std::pair<int,int> >::iterator it;
    plotdata pdata;
    int px, py;
    for (it = tdata.begin(); it != tdata.end(); ++it)
    {
        px = ((*it).first-xmin);
        py = ((*it).second-ymin);
        pdata.push_back(std::make_pair(int(float(px) * xscale),offset - int(float((py) * yscale))));
    }
    return pdata;
}

int main(void)
{
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, true);
    curs_set(0);
    while (true)
    {    
    
    int max_height , max_width;
    getmaxyx(stdscr, max_height ,max_width);
    
    timedata tdata;
    plotdata pdata;

    tdata = test_data(); 
    pdata = genPlotData(tdata);   
    
    std::vector< std::pair<int, int> >::iterator it;
    for (it=pdata.begin(); it != pdata.end(); ++it)
    {
        mvwaddch(stdscr, (*it).second, (*it).first, '+');
    } 
    
    int ch = getch();
    if(ch==113)
        break;
    }


    endwin();

}
