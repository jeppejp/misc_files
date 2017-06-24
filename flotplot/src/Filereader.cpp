#include "Filereader.hpp"
#include <fstream>
#include <sstream>



std::vector< std::string >
splitLine(std::string line, char delim)
{
    std::stringstream ss;
    ss.str(line);
    std::vector< std::string > elems;
    std::string item;


    while (std::getline(ss, item, delim)) {
        elems.push_back(item);
    }

    return elems;
}




Filereader::Filereader(std::string fpath) : m_fileName(fpath)
{

}

bool Filereader::readFile()
{
    std::ifstream infile(m_fileName.c_str(), std::ifstream::in);
    if (!infile)
        return false;

    std::string line;

    if (!std::getline(infile, line))
    {
        return false;
    }

    // check if line could be column headers
    //



    return true;
}
int getNumberOfColums()
{
    return 0;
}

std::vector< std::string > Filereader::getColumNames()
{
    return m_columnNames;
}
