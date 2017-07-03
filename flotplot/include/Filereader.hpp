#include <string>
#include <vector>


std::vector< std::string > splitLine(std::string line, char delim);



class Filereader
{
    public:
        Filereader(std::string);
        bool readFile();
        int getNumberOfColums();
        std::vector< std::string > getColumNames();
    private:
        std::string m_fileName;
        std::vector< std::string > m_columnNames;
};
