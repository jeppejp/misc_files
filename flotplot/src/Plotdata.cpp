#include <algorithm>
#include "Plotdata.hpp"

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

Plotdata::Plotdata(timedata tdata) : m_tdata(tdata), m_interpolated(false), m_plotWidth(100), m_plotHeight(40), m_colOffset(2), m_rowOffset(2)
{
}

void Plotdata::setPlotSize(int width, int height)
{
    m_plotHeight = height;
    m_plotWidth = width;
}

void Plotdata::setPlotOffset(int col, int row)
{
    m_colOffset = col;
    m_rowOffset = row;
}

plotdata Plotdata::getPointData()
{

    int xmin, xmax, ymin, ymax;
    getMinMax(m_tdata, xmin, xmax, ymin, ymax);



    int plot_height = ymax - ymin;
    int plot_length = xmax - xmin;
    float yscale = float(m_plotHeight) / float(plot_height);
    float xscale = float(m_plotWidth) / float(plot_length);

    std::vector< std::pair<int,int> >::iterator it;
    plotdata pdata;
    int px, py;
    for (it = m_tdata.begin(); it != m_tdata.end(); ++it)
    {
        px = ((*it).first-xmin);
        py = ((*it).second-ymin);
        pdata.push_back(std::make_pair(
                    int(float(px) * xscale) + m_colOffset 
                    ,m_plotHeight - int(float(py) * yscale) + m_rowOffset
                    ));
    }
    return pdata;
}

plotdata Plotdata::getInterpolated()
{
    plotdata pdata = getPointData();
    int startx = pdata.front().first;
    int stopx = pdata.back().first;

    plotdata newData;

    plotdata::iterator it, nx;
    
    for (unsigned int i=startx; i<=stopx; ++i)
    {
        // two things can happen
        // we are in between
        // we are on a point
        for (it=pdata.begin(); it!=pdata.end();++it)
        {
            nx = it;
            ++nx;
            if ((*it).first == i)
            {
                newData.push_back(*it);
            }else if( (*it).first < i && (*nx).first > i)
            {
                float alpha = float((*nx).second-(*it).second)/float((*nx).first-(*it).first);
                float dist = float(i)-float((*it).first);
                int newP = int(dist*alpha)+(*it).second;
                newData.push_back(std::make_pair(i,newP));
            }
        }
    }
    
    
    return newData;
}
