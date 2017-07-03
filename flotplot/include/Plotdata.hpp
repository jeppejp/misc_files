#include <vector>
#include "types.hpp"
class Plotdata
{


    public:
        Plotdata(timedata);
        void setPlotSize(int, int);
        void setPlotOffset(int, int);
        plotdata getPointData();
        plotdata getInterpolated();
    private:
        timedata m_tdata;
        bool m_interpolated;
        int m_plotWidth;
        int m_plotHeight;
        int m_colOffset;
        int m_rowOffset;

};
