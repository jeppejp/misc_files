#include "Filereader.hpp"
#include <fstream>

Filereader::Filereader(std::string fpath) : m_fileName(fpath)
{

}

bool Filereader::readFile()
{
    std::ifstream infile(m_fileName.c_str(), std::ifstream::in);
    if (!infile)
        return false;
    return true;
}
int getNumberOfColums()
{
    return 0;
}
