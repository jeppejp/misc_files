#include <string>

class Filereader
{
    public:
        Filereader(std::string);
        bool readFile();
        int getNumberOfColums();
        
    private:
        std::string m_fileName;




};
