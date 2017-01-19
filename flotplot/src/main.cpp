#include <iostream>
#include <curses.h>
#include <vector>
#include <algorithm>
#include "Plotdata.hpp"
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
    v.push_back(std::make_pair(11,40));
    
    return v;
}



int main(void)
{
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, true);
    curs_set(0);
    timedata tdata;
    tdata = test_data(); 
    Plotdata pd(tdata);
    while (true)
    {    

        int max_height , max_width;
        getmaxyx(stdscr, max_height ,max_width);


        plotdata pdata;


        pdata = pd.getInterpolated(); 

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
